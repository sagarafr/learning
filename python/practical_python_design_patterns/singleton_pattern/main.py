# -*- coding: utf-8 -*-

from logger import SingletonLogger


def debug():
    log = SingletonLogger(yolo='testing')
    log.debug("Debugging message")


if __name__ == "__main__":
    log = SingletonLogger()
    log.error("Error message")
    log.critical("Critical message")

    log_2 = SingletonLogger(filename='testing.log')
    log_2.warning("Warning message")
    log_2.info("Information message")

    debug()
