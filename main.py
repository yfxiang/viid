# -*- coding:utf-8 -*-

__author__ = 'yfx'
import ddt
import unittest
import requests
import datetime
from viid_project.module.HTMLTestRunner_2 import HTMLTestRunner
from viid_project.module.config import RunConfig
from viid_project.module.dict_to_json import JsonData
from viid_project.module.logger import MyLogger

logger = MyLogger(r"config/logger.conf")

common = RunConfig(r'config/commoncfg.conf')
# 运行模式: 1 - 图像集合，2 - 视频片段集合
RUN_MODE = int(common.get_run_mode())
# 每个PersonList中包含的Person个数
PERSON_NUM = int(common.get_person_num())
# 每个FaceList中包含的Face个数
FACE_NUM = int(common.get_face_num())
# 每个MotorVehicleList中包含的MotorVehicle个数
MOTORVEHICLE_NUM = int(common.get_motorvehicle_num())
# 是否包含图片: 1 - 包含，0 - 不包含
DATA_TYPE = int(common.get_data_type())
# 测试报告的路径
REPORT_PATH = common.get_report_path()
# 接口的HOST
HOST = common.get_host()
# PersonList、FaceList、MotorVehicleList中子图个数
SUB_NUM = int(common.get_sub_num())

jsondata = JsonData(r'data/data.xlsx')

if RUN_MODE == 2:
    url = HOST + '/VIID/VideoSlices'
    test_data = jsondata.get_video_list()
elif RUN_MODE == 1:
    url = HOST + '/VIID/Images'
    test_data = jsondata.get_image_list(person_num=PERSON_NUM, face_num=FACE_NUM, motor_num=MOTORVEHICLE_NUM, sub_image_num=SUB_NUM, data_type=DATA_TYPE)


@ddt.ddt
class VIIDTest(unittest.TestCase):

    def _post(self, body):
        headers = {"Content-Type": "application/json"}
        rsp = requests.request(method='POST', url=url, headers=headers, data=body)
        rsp_json = rsp.json()
        if rsp.status_code == 200:
            content = rsp_json["ResponseStatusListObject"]["ResponseStatusObject"]
            logger.info("保存成功：%s" % content)
        elif rsp.status_code == 400:
            content = rsp_json["ResponseStatusListObject"]["ResponseStatusObject"]
            logger.info("保存失败：%s" % content)

    @ddt.data(*test_data)
    def test_viid(self, file):
        logger.info(file)
        print(file)


if __name__ == "__main__":
    logger.info("程序开始执行")
    now = datetime.datetime.now().strftime("%Y-%m-%d %H_%M_%S")
    suite = unittest.TestLoader().loadTestsFromTestCase(VIIDTest)
    REPORT_NAME = REPORT_PATH + now + ' Report.html'
    fp = open(REPORT_NAME, 'wb')
    # 生成报告的Title,描述
    runner = HTMLTestRunner(stream=fp)
    runner.run(suite)
