import logging
from utils import ContextFilter


from utils import ContextFilter
error_logger = logging.getLogger('errorLogger')
# error_logger.addFilter(ContextFilter())

logger = logging.getLogger('accessLogger')

def test():
    logger.error('hello world')
    error_logger.error('error error')

    