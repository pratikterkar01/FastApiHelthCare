import logging.handlers
import sys
import logging
#get logger 
logger = logging.getLogger()


# create a formattor
formattor = logging.Formatter(fmt="%(asctime)s - %(levelname)s - %(message)s")

# create Handller 
stream_handler = logging.StreamHandler(sys.stdout)
file = logging.FileHandler('C:\\Innoshri\\FastApi\\Logger\\logger.log')
stream_handler.setFormatter(formattor)

# add handller to logger
logger.handlers = [stream_handler,file]

# set formattors
stream_handler.setFormatter(formattor)
file.setFormatter(formattor)

logger.setLevel(logging.INFO)
