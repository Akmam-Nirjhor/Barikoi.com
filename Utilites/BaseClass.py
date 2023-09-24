import logging
import pytest
@pytest.mark.usefixtures("setup")
class BassClass:
    def getLogger(self):
        logger = logging.getLogger(__name__)

        fileHandler = logging.FileHandler("logfile.log")
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)
        logger.setLevel(logging.DEBUG)

        logger.debug("A debug statement is ececuted")
        logger.info("Information statement")
        logger.warning("Somthing is warning mode")
        logger.error("A major error has happend")
        logger.critical("Critical issue")
        return logger



