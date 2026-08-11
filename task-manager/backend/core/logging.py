"""Logging configuration for the backend application."""

import logging


def configure_logging(log_level: str) -> None:
    """Configure process-wide structured-enough logging for local and container runs."""

    logging.basicConfig(
        level=log_level.upper(),
        format="%(asctime)s %(levelname)s [%(name)s] %(message)s",
    )
