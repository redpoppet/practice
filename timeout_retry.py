import random
import signal
import time

from retrying import retry


def retry_when_timeout(retries=3, timeout=2):
    def decor(func):
        def timeout_handle(signum, frame):
            raise RetryTimeOutException("Time out...")

        @retry(stop_max_attempt_number=retries, retry_on_exception=retry_if_timeout)
        def run(*args, **kwargs):
            signal.signal(signal.SIGALRM, timeout_handle)  # 设置信号和回调函数
            signal.alarm(timeout)  # 设置 num 秒的闹钟
            print('start alarm signal.')
            r = func(*args, **kwargs)
            print('close alarm signal.')
            signal.alarm(0)  # 关闭闹钟
            return r

        return run

    return decor


class RetryTimeOutException(Exception):
     def __init__(self, msg):
        super(RetryTimeOutException, self).__init__()
        self.msg = msg


def retry_if_timeout(exception):
    """Return True if we should retry (in this case when it's an IOError), False otherwise"""
    return isinstance(exception, RetryTimeOutException)


@retry_when_timeout(retries=3,timeout=1)
def do_process():
    print("begin request...")
    sleep_time = 1
    print("request sleep time: %s." % sleep_time)
    time.sleep(sleep_time)
    print("end request...")
    return True


if __name__ == "__main__":
    do_process()