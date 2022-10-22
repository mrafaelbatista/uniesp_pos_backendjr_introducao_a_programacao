from loguru import logger

try:
    print(40/0)
except ZeroDivisionError as error:
    logger.error(error)