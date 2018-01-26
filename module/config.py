# -*- coding:utf-8 -*-

__author__ = 'yfx'
import logging.config
import configparser


class RunConfig():
    
    def __init__(self, conf_file):
        config = configparser.ConfigParser()
        config.read(conf_file, encoding='utf-8')

        try:
            self.run_mode = config['RUNMODE']['runmode']
            self.person_num = config['SUB']['person_num']
            self.face_num = config['SUB']['face_num']
            self.motorvehicle_num = config['SUB']['motorvehicle_num']
            self.data_type = config['SUB']['data_type']
            self.sub_num = config['SUB']['sub_num']
            self.host = config['HOST']['host']
            self.report_file = config['REPORT']['report_file']
        except Exception as e:
            logging.config.fileConfig('../config/logger.conf')
            logger = logging.getLogger('test')
            logger.error('读取配置文件失败: %s' % e)
            exit()

    def get_run_mode(self):
        return self.run_mode

    def get_person_num(self):
        return self.person_num

    def get_face_num(self):
        return self.face_num

    def get_motorvehicle_num(self):
        return self.motorvehicle_num

    def get_data_type(self):
        return self.data_type

    def get_report_path(self):
        return self.report_file

    def get_host(self):
        return self.host

    def get_sub_num(self):
        return self.sub_num