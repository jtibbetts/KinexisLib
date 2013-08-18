
import sys
import logging

from logging.handlers import SysLogHandler

LOG_SERVER_ADDR = 'kinexis.com'
LOG_SERVER_PORT = 514

logger = logging.getLogger('KinexisLogger')

# LOCAL5 --> kinex.log
# LOCAL6 --> logserver.log
handler = SysLogHandler((LOG_SERVER_ADDR, LOG_SERVER_PORT), facility=SysLogHandler.LOG_LOCAL5)
formatter = logging.Formatter('%(name)s: %(levelname)s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)

argString = ' '.join(sys.argv)
logger.info("Test")
