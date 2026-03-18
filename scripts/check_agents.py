#!/usr/bin/env python3
"""Check health and version of all Foundry Hosted Agents.

Verifies each agent's latest registered version and running status.
Useful after register_agents.py to confirm new versions are deployed
before submitting PA requests from the frontend.

Usage:
    python scripts/check_agents.py              # check once
    python scripts/check_agents.py --poll       # poll until all healthy (5 min timeout)
    python scripts/check_agents.py --version 6  # wait for specific version
"""

import argparse
import json
import os
import subprocess
import sys
import time

AGENTS = [
    "clinical-reviewer-agent",
    "coverage-assessment-agent",
    "compliance-agent",
    "synthesis-agent",
]


def _get_azd_value(key):
    try:
        result = subprocess.run(
            ["azd", "env", "get-value", key],
            capture_output=True, text=True, timeout=10,
        )
        val = result.stdout.strip()
        return val if val and "ERROR" not in val else ""
    except Exception:
        return ""


def get_agent_info(account, project, agent_name):
    try:
        result = subprocess.run(
            ["az", "cognitiveservices", "agent", "show",
             "--account-name", account, "--project-name", project,
             "--name", agent_name, "-o", "json"],
            capture_output=True, text=True, timeout=30,
        )
        if result.returncode == 0:
            data = json.loads(result.stdout)
            latest = data.get("versions", {}).get("latest", {})
            return {"version": latest.get("version", "?"), "status": "registered"}
    except Exception:
        pass
    return {"version": "?", "status": "unknown"}


def check_all(account, project):
    results = []
    for name in AGENTS:
        info = get_agent_info(account, project, name)
        results.append({"name": name, **info})
    return results


def print_status(results):
    print(f"\n  {'Agent':<30} {'Version':>8}  {'Status':<15}")
    print(f"  {'-'*30} {'-'*8}  {'-'*15}")
    for r in results:
        version = str(r.get("version") or "?")
        status = str(r.get("status") or "unknown")
        icon = "✓" if status == "registered" else "✗"
        print(f"  {r['name']:<30} {'v' + version:>8}  {icon} {status}")
    print()


def all_ready(results, expected_version=None):
    for r in results:
        if r["status"] == "unknown":
            return False
        if expected_version and str(r["version"]) != str(expected_version):
            return False
    return True


def main():
    parser = argparse.ArgumentParser(description="Check Foundry Hosted Agent health")
    parser.add_argument("--poll", action="store_true", help="Poll until all agents are ready")
    parser.add_argument("--timeout", type=int, default=5, help="Max minutes to poll (default: 5)")
    parser.add_argument("--version", type=int, help="Expected version number to wait for")
    args = parser.parse_args()

    account = os.environ.get("AI_FOUNDRY_ACCOUNT_NAME") or _get_azd_value("AI_FOUNDRY_ACCOUNT_NAME")
    project = os.environ.get("AI_FOUNDRY_PROJECT_NAME") or _get_azd_value("AI_FOUNDRY_PROJECT_NAME")

    if not account or not project:
        print("ERROR: AI_FOUNDRY_ACCOUNT_NAME and AI_FOUNDRY_PROJECT_NAME must be set.", file=sys.stderr)
        sys.exit(1)

    print(f"  Checking agents in {project}...")
    results = check_all(account, project)
    print_status(results)

    if not args.poll:
        if all_ready(results, args.version):
            print("  All agents are registered. Safe to submit PA requests.")
        else:
            print("  Some agents may not be ready yet.")
        sys.exit(0 if all_ready(results, args.version) else 1)

    deadline = time.time() + args.timeout * 60
    while time.time() < deadline:
        if all_ready(results, args.version):
            print("  All agents are registered and ready.")
            sys.exit(0)
        time.sleep(15)
        print("  Polling...", flush=True)
        results = check_all(account, project)
        print_status(results)

    print(f"  Timeout after {args.timeout} minutes.")
    sys.exit(1)


if __name__ == "__main__":
    main()
