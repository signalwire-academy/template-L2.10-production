#!/usr/bin/env python3
"""Production-ready agent with health checks.

Lab 2.10 Deliverable: Demonstrates production deployment patterns
including environment configuration, logging, and health endpoints.
"""

import os
import logging
from datetime import datetime
from signalwire_agents import AgentServer, AgentBase, SwaigFunctionResult

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # dotenv not required

# Configure logging
log_level = os.getenv("LOG_LEVEL", "INFO").upper()
logging.basicConfig(
    level=log_level,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class ProductionAgent(AgentBase):
    """Production-ready agent with configuration from environment."""

    def __init__(self):
        super().__init__(name=os.getenv("AGENT_NAME", "production-agent"))

        # Prompt configuration
        self.prompt_add_section(
            "Role",
            os.getenv("AGENT_ROLE", "You are a helpful production assistant.")
        )

        self.prompt_add_section(
            "Guidelines",
            bullets=[
                "Keep responses concise",
                "Be helpful and professional",
                "Escalate if needed"
            ]
        )

        self.add_language("English", "en-US", "rime.spore")

        self._setup_functions()
        logger.info(f"Agent initialized: {self.get_name()}")

    def _setup_functions(self):
        @self.tool(description="Get system status")
        def get_status() -> SwaigFunctionResult:
            logger.info("Status check requested")
            return SwaigFunctionResult("All systems operational.")

        @self.tool(description="Get current time")
        def get_time() -> SwaigFunctionResult:
            now = datetime.now().strftime("%I:%M %p")
            return SwaigFunctionResult(f"The current time is {now}.")

        @self.tool(description="Get help or support information")
        def get_help() -> SwaigFunctionResult:
            support_email = os.getenv("SUPPORT_EMAIL", "support@company.com")
            return SwaigFunctionResult(
                f"For additional help, contact {support_email}."
            )


def create_app():
    """Create the application with health endpoints."""
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", "3000"))

    logger.info(f"Creating server on {host}:{port}")

    server = AgentServer(host=host, port=port)
    server.register(ProductionAgent())

    # Health endpoint
    @server.app.get("/health")
    async def health():
        return {
            "status": "healthy",
            "timestamp": datetime.utcnow().isoformat(),
            "version": os.getenv("APP_VERSION", "1.0.0")
        }

    # Readiness endpoint
    @server.app.get("/ready")
    async def ready():
        return {"ready": True}

    # Info endpoint
    @server.app.get("/info")
    async def info():
        return {
            "name": os.getenv("AGENT_NAME", "production-agent"),
            "version": os.getenv("APP_VERSION", "1.0.0"),
            "environment": os.getenv("ENVIRONMENT", "production")
        }

    return server


if __name__ == "__main__":
    server = create_app()
    server.run()
