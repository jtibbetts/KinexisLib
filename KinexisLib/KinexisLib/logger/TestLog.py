
import logging

from logger import LoggerFactory


logger = LoggerFactory.getDefaultLogger()
logger = LoggerFactory.getDefaultLogger()
logger.setLevel(logging.INFO) #@UndefinedVariable
logger.info('Here is info')
logger.warning('Here is a warning')



