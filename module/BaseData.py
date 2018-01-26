# -*- coding:utf-8 -*-

__author__ = 'yfx'

import base64
from viid_project.module.excel_to_dict import ExcelToDict


class BaseData(object):
    def __init__(self, excel_file):
        try:
            self.sheet_image = ExcelToDict(excel_file, 'ImageInfo')
            self.sheet_video = ExcelToDict(excel_file, 'VideoSliceInfo')
            self.sheet_person = ExcelToDict(excel_file, 'Person')
            self.sheet_face = ExcelToDict(excel_file, 'Face')
            self.sheet_motorvehicle = ExcelToDict(excel_file, 'MotorVehicle')
            self.sheet_sub = ExcelToDict(excel_file, 'SubImage')
            self.sheet_data = ExcelToDict(excel_file, 'Data')
        except Exception as e:
            from viid_project.module.logger import MyLogger
            logger = MyLogger('../config/logger.conf')
            logger.error('读取配置文件[%s]失败: %s' % (excel_file, e))
            exit()

    def get_image_info(self):
        # 返回一个列表，列表中每个元素为一个数据类型为字典的ImageInfo
        return self.sheet_image.next()

    def get_video_info(self):
        # 返回一个列表，列表中每个元素为一个数据类型为字典的VideoSliceInfo
        return self.sheet_video.next()

    def get_person(self):
        # 返回一个列表，列表中每个元素为一个数据类型为字典的PersonObject
        return self.sheet_person.next()

    def get_face(self):
        # 返回一个列表，列表中每个元素为一个数据类型为字典的FaceObject
        return self.sheet_face.next()

    def get_motorvehicle(self):
        # 返回一个列表，列表中每个元素为一个数据类型为字典的MotorVehicleObject
        return self.sheet_motorvehicle.next()

    def get_data(self):
        data = []
        for i in self.sheet_data.next():
            filename = i['FileName']
            with open(filename, 'rb') as f:
                img_bytes = base64.b64encode(f.read())
                img_string = img_bytes.decode('UTF-8')
            data.append(img_string)
        return data

    def get_sub_image_info(self):
        return self.sheet_sub.next()

