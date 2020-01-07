import logging

from django.conf import settings


def get_json_logger(name=None):
    return JsonLogger(logging.getLogger(name))


class JsonLogger:
    def __init__(self, logger):
        self.logger = logger

    def __encode_keys(self, **kwargs):
        reserved_keys = ['stack_info', 'exc_info']
        encoded_keys = {}
        for k, v in kwargs.items():
            if k not in reserved_keys:
                encoded_keys[k] = v
        for k in encoded_keys:
            kwargs.pop(k)

        encoded_keys['index'] = getattr(settings, 'LOG_INDEX', None)
        encoded_keys['source'] = getattr(settings, 'LOG_SOURCE', None)

        if len(encoded_keys) > 0:
            kwargs['extra'] = encoded_keys

        return kwargs

    def debug(self, ___msg, *args, **kwargs):
        self.logger.debug(___msg, *args, **self.__encode_keys(**kwargs))

    def info(self, ___msg, *args, **kwargs):
        self.logger.info(___msg, *args, **self.__encode_keys(**kwargs))

    def warning(self, ___msg, *args, **kwargs):
        self.logger.warning(___msg, *args, **self.__encode_keys(**kwargs))

    def warn(self, ___msg, *args, **kwargs):
        self.logger.warn(___msg, *args, **self.__encode_keys(**kwargs))

    def error(self, ___msg, *args, **kwargs):
        self.logger.error(___msg, *args, **self.__encode_keys(**kwargs))

    def exception(self, ___msg, *args, **kwargs):
        self.logger.exception(___msg, *args, **self.__encode_keys(**kwargs))

    def critical(self, ___msg, *args, **kwargs):
        self.logger.critical(___msg, *args, **self.__encode_keys(**kwargs))

    def log(self, ___level, ___msg, *args, **kwargs):
        self.logger.log(___level, ___msg, *args, **self.__encode_keys(**kwargs))
