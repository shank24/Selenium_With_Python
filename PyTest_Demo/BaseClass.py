import inspect
import logging


class BaseClass:

    def getLogger():
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)

        # file handler object is required in addHandler
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s :%(lineno)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.INFO)
        return logger
