import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    AZURE_FOUNDRY_API_KEY: str = os.getenv("AZURE_FOUNDRY_API_KEY", "")
    AZURE_FOUNDRY_ENDPOINT: str = os.getenv("AZURE_FOUNDRY_ENDPOINT", "")
    CLAUDE_MODEL: str = os.getenv("CLAUDE_MODEL", "claude-sonnet-4-6")
    FRONTEND_ORIGIN: str = os.getenv("FRONTEND_ORIGIN", "http://localhost:3000")

    # Agent runtime mode
    # false = current local/in-process ClaudeAgent execution
    # true  = backend invokes externally hosted agents over HTTP
    USE_HOSTED_AGENTS: bool = os.getenv("USE_HOSTED_AGENTS", "false").lower() in (
        "true",
        "1",
        "yes",
    )

    # Hosted agent endpoints (used only when USE_HOSTED_AGENTS=true)
    HOSTED_AGENT_CLINICAL_URL: str = os.getenv("HOSTED_AGENT_CLINICAL_URL", "")
    HOSTED_AGENT_COMPLIANCE_URL: str = os.getenv("HOSTED_AGENT_COMPLIANCE_URL", "")
    HOSTED_AGENT_COVERAGE_URL: str = os.getenv("HOSTED_AGENT_COVERAGE_URL", "")
    HOSTED_AGENT_SYNTHESIS_URL: str = os.getenv("HOSTED_AGENT_SYNTHESIS_URL", "")
    HOSTED_AGENT_TIMEOUT_SECONDS: float = float(
        os.getenv("HOSTED_AGENT_TIMEOUT_SECONDS", "180")
    )

    # Optional auth/header configuration for hosted-agent calls
    HOSTED_AGENT_AUTH_HEADER: str = os.getenv(
        "HOSTED_AGENT_AUTH_HEADER", "Authorization"
    )
    HOSTED_AGENT_AUTH_SCHEME: str = os.getenv(
        "HOSTED_AGENT_AUTH_SCHEME", "Bearer"
    )
    HOSTED_AGENT_AUTH_TOKEN: str = os.getenv("HOSTED_AGENT_AUTH_TOKEN", "")

    # Skills-based approach toggle (default: True)
    # When True, agents use SKILL.md files via MAF native skill discovery.
    # When False, agents use inline system prompt instructions.
    USE_SKILLS: bool = os.getenv("USE_SKILLS", "true").lower() in ("true", "1", "yes")

    # Healthcare MCP Server endpoints (from anthropics/healthcare)
    MCP_NPI_REGISTRY: str = os.getenv(
        "MCP_NPI_REGISTRY", "https://mcp.deepsense.ai/npi_registry/mcp"
    )
    MCP_ICD10_CODES: str = os.getenv(
        "MCP_ICD10_CODES", "https://mcp.deepsense.ai/icd10_codes/mcp"
    )
    MCP_CMS_COVERAGE: str = os.getenv(
        "MCP_CMS_COVERAGE", "https://mcp.deepsense.ai/cms_coverage/mcp"
    )
    MCP_PUBMED: str = os.getenv(
        "MCP_PUBMED", "https://pubmed.mcp.claude.com/mcp"
    )
    MCP_CLINICAL_TRIALS: str = os.getenv(
        "MCP_CLINICAL_TRIALS", "https://mcp.deepsense.ai/clinical_trials/mcp"
    )

    # Azure Application Insights (observability)
    APPLICATION_INSIGHTS_CONNECTION_STRING: str = os.getenv(
        "APPLICATION_INSIGHTS_CONNECTION_STRING", ""
    )


settings = Settings()
