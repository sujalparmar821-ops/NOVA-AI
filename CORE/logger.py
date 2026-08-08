"""
CORE/logger.py
--------------
Logging system for NOVA.
"""

import logging
from pathlib import Path

# Ensure the LOGS folder exists
Path("LOGS").mkdir(exist_ok=True)

logging.basicConfig(
    filename="LOGS/nova.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

logger = logging.getLogger("NOVA")


def info(message: str):
    logger.info(message)


def warning(message: str):
    logger.warning(message)


def error(message: str):
    logger.error(message)