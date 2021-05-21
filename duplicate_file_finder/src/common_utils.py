# imports
import sys
import logging


# authors
__author__ = "zanza259"
__version__ = "1.0.0"


# constants
LOGGING_FORMATTER = logging.Formatter(fmt="%(asctime)s | %(levelname)s | %(message)s", datefmt="%Y-%m-%d %H:%M:%S")



def build_default_logger(name, level="WARN"):

    level_map = {
        "DEBUG": logging.DEBUG,
        "INFO": logging.INFO,
        "WARN": logging.WARN,
        "ERROR": logging.ERROR
    }

    logger = logging.getLogger()

    stream_handler = logging.StreamHandler(stream=sys.stdout)
    stream_handler.setFormatter(LOGGING_FORMATTER)

    logger.setLevel(level_map[level])
    logger.addHandler(stream_handler)
    logger.propagate = False

    return logger
    
def add_common_logger_args(argparser):

    argparser.add_argument("-v", "--verbose", action="store_true",
                        help="Flag for verbose logging.")

    argparser.add_argument("-d", "--debug", action="store_true",
                        help="Flag for debug logging and debug mode.")
