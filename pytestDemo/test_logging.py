import logging
logger = logging.getLogger("test_logging") #__name__ will print complete path in logger

filehandler = logging.FileHandler("test.log")
format = logging.Formatter("%(asctime)s: %(levelname)s : %(name)s : %(message)s")
filehandler.setFormatter(format)
logger.addHandler(filehandler)

logger.setLevel(logging.INFO)


def test_logging():
    logger.info("this is info")
    logger.debug("this is debug level")
    logger.warning("this is warning level")
    logger.error("This is error level")

#to print on console also run from cli -> pytest test_logging.py --log-cli-level=INFO
#this will print in test.log(acc to level set from file) and cli also(set from log cli level)
#other way is to create pytest.ini file and have log_cli=true




