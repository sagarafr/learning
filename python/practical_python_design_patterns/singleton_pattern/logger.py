# -*- coding: utf-8 -*-


class SingletonLogger:
    class __SingletonLogger:
        def __init__(self, filename: str ="log.log"):
            self.filename = filename

        def __write_log(self, gravity, text):
            with open(self.filename, 'a') as fd_log:
                fd_log.write("[{0}] {1}\n".format(gravity, text))

        def critical(self, text):
            self.__write_log("critical", text)

        def error(self, text):
            self.__write_log("error", text)

        def warning(self, text):
            self.__write_log("warning", text)

        def info(self, text):
            self.__write_log("info", text)

        def debug(self, text):
            self.__write_log("debug", text)

    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = SingletonLogger.__SingletonLogger(**kwargs)
        if "filename" in kwargs and kwargs["filename"] != cls.instance.filename:
            cls.instance = SingletonLogger.__SingletonLogger(**kwargs)

        return cls.instance

    def __getattr__(self, item):
        return getattr(self.instance, item)

    def __setattr__(self, key, value):
        return setattr(self.instance, key, value)
