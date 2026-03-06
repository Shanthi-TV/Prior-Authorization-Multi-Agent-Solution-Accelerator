# Foundry Hosted Agents Migration Plan

## Target architecture

- Frontend remains in Azure Container Apps.
- FastAPI backend and orchestrator remain in Azure Container Apps.
- The four AI runtimes move to true Microsoft Foundry hosted agents:
  - `compliance`
  - `clinical`
  - `coverage`
  - `synthesis`

## Why this is the lower-risk path

- Preserves the frontend API contract and SSE flow.
- Preserves the backend decision endpoint, audit generation, and response normalization.
- Limits the main runtime change to the agent execution layer.

## Implementation checkpoints

1. Add a hosted-agent runtime abstraction in the backend.
2. Keep local execution as a fallback during migration.
3. Update infrastructure to provide hosted-agent endpoints and auth settings.
4. Refresh documentation and architecture diagrams after runtime parity is validated.
5. Keep App Insights for backend telemetry; use Foundry for hosted-agent evaluation and control-plane monitoring.

## Key gotchas

- Hosted agents improve native Foundry evaluation and lifecycle management, but do not automatically fix the current `ClaudeAgent` tool-level tracing limitation.
- Backend App Insights is still required while the backend/orchestrator remains in ACA.
- The backend must keep ownership of SSE progress events, review persistence, decision handling, and PDF generation.
- MCP/skill ownership may need additional adaptation when moving from local `.claude` skill discovery to hosted-agent configuration.