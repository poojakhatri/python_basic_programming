# Logging

# Purpose: Record progress and problems...

# Levels : Debug, Info, Warning, Error, Critical

import logging

# create and configure logger
logging.basicConfig(filename ="Lumberjack.log",level = logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s', filemode ='w')
logger = logging.getLogger()

# Test the messages

logger.debug("This is a harmless debug message.")
logger.info("Just some useful info")
logger.warning("I'am sorry but I can't do that, Dave.")
logger.error("Did you just try to divide by zero?")
logger.critical("The entire internet is down!")


