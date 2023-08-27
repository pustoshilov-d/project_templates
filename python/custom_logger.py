import logging
import os
import sys
from pathlib import Path

LOG_FILE = "warnings.log"
FORMAT_STYLE = "%(asctime)s - %(levelname)s - %(message)s (%(filename)s:%(funcName)s:%(lineno)d)"
# FORMAT_STYLE="%(asctime)s - %(name)s - %(levelname)s
# - %(message)s (%(filename)s:%(funcName)s:%(lineno)d)"


def addLoggingLevel(levelName, levelNum, methodName=None):
    # https://stackoverflow.com/a/35804945
    if not methodName:
        methodName = levelName.lower()
    if hasattr(logging, levelName):
        raise AttributeError("{} already defined in logging module".format(levelName))
    if hasattr(logging, methodName):
        raise AttributeError("{} already defined in logging module".format(methodName))
    if hasattr(logging.getLoggerClass(), methodName):
        raise AttributeError("{} already defined in logger class".format(methodName))

    def logForLevel(self, message, *args, **kwargs):
        if self.isEnabledFor(levelNum):
            self._log(levelNum, message, args, **kwargs)

    def logToRoot(message, *args, **kwargs):
        logging.log(levelNum, message, *args, **kwargs)

    logging.addLevelName(levelNum, levelName)
    setattr(logging, levelName, levelNum)
    setattr(logging.getLoggerClass(), methodName, logForLevel)
    setattr(logging, methodName, logToRoot)


addLoggingLevel("SUCCESS", logging.WARNING - 5)


def configure_logger(logger_name="custom_logger", temp_dir: Path | str = "./"):
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)
    log_path = os.path.join(temp_dir, LOG_FILE)
    # if os.path.isfile(LOG_PATH):
    #     os.remove(log_path)

    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)

    fileout = logging.FileHandler(log_path)
    fileout.setLevel(logging.WARNING)
    fileout.setFormatter(FileoutFormatter())
    logger.addHandler(fileout)

    stdout = logging.StreamHandler(sys.stdout)
    stdout.setFormatter(StdoutFormatter())
    stdout.setLevel(logging.DEBUG)
    logger.addHandler(stdout)


class StdoutFormatter(logging.Formatter):
    blue = "\x1b[38;5;39m"
    green = "\x1b[32;20m"
    grey = "\x1b[38;20m"
    yellow = "\x1b[33;20m"
    red = "\x1b[31;20m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"

    FORMATS = {
        logging.DEBUG: grey + FORMAT_STYLE + reset,
        logging.INFO: blue + FORMAT_STYLE + reset,
        logging.WARNING: yellow + FORMAT_STYLE + reset,
        logging.SUCCESS: green + FORMAT_STYLE + reset,
        logging.ERROR: red + FORMAT_STYLE + reset,
        logging.CRITICAL: bold_red + FORMAT_STYLE + reset,
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


class FileoutFormatter(logging.Formatter):
    def format(self, record):
        formatter = logging.Formatter(FORMAT_STYLE)
        return formatter.format(record)
