# -*- coding:utf-8 -*-

__author__ = 'yfx'
import configparser
from .log import MyLogger


class ConfigInfo():
    
    def __init__(self, conf_file):
        self.config = configparser.ConfigParser()
        self.config.read(conf_file, encoding='utf-8')
        
    def get_mode(self):
        """
        返回测试接口的列表[图像集合对象，视频片段集合对象]
        """
        mode = []
        try:
            image = self.config.get('RUNMODE','image')
            videoslice = self.config.get('RUNMODE','videoslice')
        except Exception as error:
            logger = MyLogger()
            logger.error('测试运行模式读取失败：%s' % error)
            exit()
        mode.append(int(image))
        mode.append(int(videoslice))
        return mode

    def get_image(self):
        """
        返回图片配置信息的列表[图片个数，是否包含Data信息]
        """
        image = []
        try:
            img = self.config.get('IMAGE','image')
            data = self.config.get('IMAGE','data')
        except Exception as error:
            logger = MyLogger()
            logger.error('图片配置信息读取失败：%s' % error)
            exit()
        image.append(int(img))
        image.append(int(data))
        return image
    
    def get_videoslice(self):
        """
        返回视频片段配置信息的列表[视频片段个数,]
        """
        videoslice = []
        try:
            video = self.config.get('VIDEOSLICE','videoslice')
        except Exception as error:
            logger = MyLogger()
            logger.error('视频片段配置信息读取失败：%s' % error)
            exit()
        videoslice.append(int(video))
        return videoslice
    
    def get_person(self):
        pass

    def get_face(self):
        pass

    def get_motor(self):
        pass

    def get_report(self):
        """
        返回测试报告信息的列表[测试报告路径,测试报告名称]
        """
        try:
            report = self.config.get('REPORT', 'report')
        except Exception as error:
            logger = MyLogger()
            logger.error('测试报告信息读取失败：%s' % error)
        return report

    def get_host(self):
        """
        返回服务器地址
        """
        try:
            host = self.config.get('REPORT', 'report')
        except Exception as error:
            logger = MyLogger()
            logger.error('服务器地址信息读取失败：%s' % error)
        return host
