# -*- coding:utf-8 -*-

__author__ = 'yfx'

import json
from viid_project.module.BaseData import BaseData


class JsonData(object):
    def __init__(self, excel_file,):
        self.basedata = BaseData(excel_file)
        # 类初始化时，直接读取图片信息和子图结构化数据，防止人、人脸、车等重复调用函数，导致读取不到数据
        # 一个由图片经过base64编码后的数据组成的列表
        self.image_data = self.basedata.get_data()
        self.sub_image_info = self.basedata.get_sub_image_info()

    def _get_sub_image(self, sub_image_num):
        """
        返回一个子图列表，其中每一个列表元素由sub_image_num个子图组成
        :param sub_image_num:
        :return sub_image_list:
        """
        # 取结构化数据个数和图片个数的最小值，列表越界
        num = min(len(self.image_data), len(self.sub_image_info))

        # 把图片和结构化数据组合成一个完整的子图
        for i in range(num):
            self.sub_image_info[i]['Data'] = self.image_data[i]

        # 根据sub_image_num个数复制子图，组成子图列表，然后由子图列表做为元素重新组成最终的子图列表
        sub_image = []
        for i in self.sub_image_info:
            j = []
            for x in range(sub_image_num):
                j.append(i)
            sub_image.append({'SubImageInfoObject':j})
        return sub_image

    def _get_person(self, person_num, sub_image_num):
        """
        返回一个由PersonList组成的列表,其中每个PersonList由person_num个Person组成
        :param person_num:
        :param sub_image_num:
        :return: person_list：
        """
        sub_image = self._get_sub_image(sub_image_num)
        # 原始的person数据列表
        person_info = self.basedata.get_person()
        # 取结构化数据个数和子图个数的最小值，列表越界
        num = min(len(sub_image), len(person_info))

        # 把子图和Person结构化数据组成一个完整的Person
        for i in range(num):
            person_info[i]['SubImageList'] = sub_image[i]

        # 根据person_num个数复制Person，组成Person列表，然后由Person列表做为元素重新组成最终的Person列表
        person = []
        for i in person_info:
            j = []
            for x in range(person_num):
                j.append(i)
            person.append({'PersonObject':j})
        return person

    def _get_face(self, face_num, sub_image_num):
        """
        返回一个由FaceList组成的列表,其中每个Facelist有face_num个Face组成
        :param face_num:
        :param sub_image_num:
        :return: face_list：
        """
        sub_image = self._get_sub_image(sub_image_num)
        # 原始face数据列表
        face_info = self.basedata.get_face()
        # 取结构化数据个数和子图个数的最小值，列表越界
        num = min(len(sub_image), len(face_info))

        # 把子图和Face结构化数据组成一个完整的Face
        for i in range(num):
            face_info[i]['SubImageList'] = sub_image[i]

        # 根据face_num个数复制face，组成face列表，然后由face列表做为元素重新组成最终的face列表
        face = []
        for i in face_info:
            j = []
            for x in range(face_num):
                j.append(i)
            face.append({'FaceObject':j})
        return face

    def _get_motorvehicle(self, motorvehicle_num, sub_image_num):
        """
        返回一个由MotorVehicleList组成的列表,其中每个MotorVehicleList由num个MotorVehicle组成
        :param motorvehicle_num:
        :param sub_image_num:
        :return: motorvehicle:
        """
        sub_image = self._get_sub_image(sub_image_num)
        # 原始MotorVehicle数据列表
        motorvehicle_info = self.basedata.get_motorvehicle()
        # 取结构化数据个数和子图个数的最小值，列表越界
        num = min(len(sub_image), len(motorvehicle_info))

        # 把子图和MotorVehicle结构化数据组成一个完整的MotorVehicle
        for i in range(num):
            motorvehicle_info[i]['SubImageList'] = sub_image[i]

        # 根据MotorVehicle_num个数复制MotorVehicle，组成MotorVehicle列表，然后由MotorVehicle列表做为元素重新组成最终的MotorVehicle列表
        motorvehicle = []
        for i in motorvehicle_info:
            j = []
            for x in range(motorvehicle_num):
                j.append(i)
            motorvehicle.append({'MotorVehicleObject':j})
        return motorvehicle

    def get_image_list(self, image_num=1, person_num=1, face_num=1, motor_num=1, data_type=1, sub_image_num=1):
        """
        返回一个Image列表，每一个Image元素可能包含图片、人、人脸、车、Data
        :param image_num:
        :param person_num:
        :param face_num:
        :param motor_num:
        :param data_type:
        :param sub_image_num:
        :return: image_list
        """

        # 一个由ImageInfo组成的列表
        image_info_list = self.basedata.get_image_info()
        # num 为当前表格数据可以组成多少个ImageInfo的结构化数据
        num = len(image_info_list)
        # 获取由Person组成的列表,调整num为Image和Person中的最小值
        if person_num:
            person = self._get_person(person_num, sub_image_num)
            num = min(num, len(person))
        else:
            pass
        # 获取由Face组成的列表,调整num为Image和Face中的最小值
        if face_num:
            face = self._get_face(face_num, sub_image_num)
            num = min(num, len(face))
        else:
            pass
        # 获取MotorVehicle组成的列表,调整num为Image和MotorVehicle中的最小值
        if motor_num:
            motor = self._get_motorvehicle(motor_num, sub_image_num)
            num = min(num, len(motor))
        else:
            pass
        # 获取data组成的列表,调整num为Image和Data中的最小值
        if data_type:
            data = self.image_data
            num = min(num, len(data))
        else:
            pass

        # imagelist为由Image组成的列表,包含1个或多个Image
        images = []
        for j in range(num):
            # image是由imageobject组成的列表，每个imageobject包含一个ImageInfo,0个或1个PersonList,0个或1个FaceList,0个或1个MotorVehicleList
            image_object = {}
            image = []
            image_object['ImageInfo'] = image_info_list[j]
            if person_num:
                image_object['PersonList'] = person[j]
            if face_num:
                image_object['FaceList'] = face[j]
            if motor_num:
                image_object['MotorVehicleList'] = motor[j]
            if data_type:
                image_object['Data'] = data[j]

            for i in range(image_num):
                image.append(image_object)

            json_data = json.dumps({"ImageListObject":{"Image":image}})
            images.append(json_data)
        return images

    def get_video_list(self, video_num=1):
        """
        返回一个Video列表，每一个Video元素仅包含Video的结构化数据
        :param video_num:
        :return: videos
        """
        # 获取一个由videoInfo组成的列表
        videoinfo = self.basedata.get_video_info()
        # num 为当前表格数据可以组成多少个消息体ImageListObject
        num = len(videoinfo)
        videos = []
        for j in range(num):
            video_object = {}
            video = []
            video_object["VideoSliceInfo"] = videoinfo[j]

            for i in range(video_num):
                video.append(video_object)

            json_data = json.dumps({"VideoSliceListObject":{"VideoSlice":video}})
            videos.append(json_data)
        return videos
