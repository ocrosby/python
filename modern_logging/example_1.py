"""
Use dictConfig to configure logging
"""

import logging
import logging.config

logger = logging.getLogger("my_app")

logging_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "simple": {
            "format": "%(levelname)s - %(message)s",
        },
    },
    "handlers": {
        "stdout": {
            "class": "logging.StreamHandler",
            "formatter": "simple",
            "stream": "ext://sys.stdout",
        },
    },
    "loggers": {
        "root": {
            "level": "DEBUG",
            "handlers": ["stdout"]
        },
    },
}

def main():
    logging.config.dictConfig(config=logging_config)
    logger.debug("This is a debug message")
    logger.info("This is an info message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")
    logger.critical("This is a critical message")

    try:
        1 / 0
    except ZeroDivisionError:
        logger.exception("You can't divide by zero")

if __name__ == "__main__":
    main()
