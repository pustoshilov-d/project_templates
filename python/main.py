import logging
import os

from dotenv import load_dotenv

from custom_logger import configure_logger

# load env vars
load_dotenv()

# Set up logger
configure_logger(logger_name="custom_logger")
logger = logging.getLogger("custom_logger")


def main():
    # run code
    logger.success("Hello World!")
    ENV = os.getenv("ENV")
    logger.info(f"{ENV=}")


if __name__ == "__main__":
    main()
