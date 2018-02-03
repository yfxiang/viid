# -*- coding:utf-8 -*-


__author__ = 'yfx'

import logging
import logging.config


class MyLogger():
    def __init__(self, conf="../config/logger.conf"):
        logging.config.fileConfig(conf)
        self.logger = logging.getLogger("test")

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)

