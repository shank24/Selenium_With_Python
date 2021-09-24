import logging


def test_loggingDemo():
    logger = logging.getLogger(__name__)

    # file handler object is required in addHandler

    fileHandler = logging.FileHandler('logfile.log')
    formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s :%(lineno)s")

    fileHandler.setFormatter(formatter)

    logger.addHandler(fileHandler)

    logger.setLevel(logging.DEBUG)
    logger.debug("A debug statement")
    logger.info("A Information ")
    logger.warning("Warning")
    logger.critical("Critical")
    logger.error("Error !!")
