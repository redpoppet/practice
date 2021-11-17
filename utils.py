import logging
class MyLoggerAdapter(logging.LoggerAdapter):

    def process(self, msg, kwargs):
        if 'extra' not in kwargs:
            kwargs["extra"] = self.extra
        return msg, kwargs


class ContextFilter(logging.Filter):

        request_id = '23333333333333'

        def filter(self, record):
            record.request_id = self.request_id
            return True


def init_log():
    logging.config.fileConfig("logging.ini")
    logging.getLogger('root').addFilter(ContextFilter())
    logging.getLogger('accessLogger').addFilter(ContextFilter())
    logging.getLogger('errorLogger').addFilter(ContextFilter())



    
