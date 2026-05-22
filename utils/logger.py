import logging
from datetime import datetime


def setup_logger():

    logger = logging.getLogger("automation_logger")

    logger.setLevel(logging.INFO)

    if not logger.handlers:

        timestamp = datetime.now().strftime(
            "%Y%m%d_%H%M%S"
        )

        logfile = f"logs/automation_{timestamp}.log"

        file_handler = logging.FileHandler(logfile)

        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )

        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)

    return logger