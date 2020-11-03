#!/usr/bin/env python
#encoding:utf-8
#?  Instructions :
#?  rosrun face_detector turty_face_recognition.py 

import rospy
import face_recognition
import os
import cv2
import numpy as np
from face_detector.msg import face_msgs
from face_detector.msg import my_list
from face_detector.msg  import EnableSignal
from sensor_msgs.msg import Image
from cv_bridge import CvBridge,CvBridgeError

#初始化  turty_face_detector  消息发布节点
rospy.init_node('turty_face_recognizer')
pub = rospy.Publisher('Topic_Recognition_Msg', face_msgs, queue_size=1)
rate = rospy.Rate(10)
face_imgs_savepath = r"./known_face_imgs" #人脸图片保存路径

def cv_imread(filePath):
    cv_img = cv2.imdecode(np.fromfile(filePath, dtype=np.uint8), -1)
    # imdecode读取的是rgb，如果后续需要opencv处理的话，需要转换成bgr，转换后图片颜色会变化
    # cv_img=cv2.cvtColor(cv_img,cv2.COLOR_RGB2BGR)
    return cv_img

# 导入图片
IMG_MAXCOUNT = 5
def load_images(path, amout=IMG_MAXCOUNT):
    img_list = []
    img_name_list = []
    for filename in os.listdir(path):
          if(os.path.splitext(filename)[-1] == '.jpg'):
                  img_name_list.append(os.path.splitext(filename)[0] )
                  img = cv_imread(os.path.join(path, filename))
                  img_list.append(img)
                  amout -= 1
                  if amout <= 0:  # 控制读取图片的数量
                        break
    return img_list,img_name_list

def save_images(img,path, name,format):
    number  = 0
    filename = name +str(number) + format
    file_name_tmp = os.path.join(path, filename)
    while(os.path.isfile(file_name_tmp)):
        number +=  1
        filename = name +str(number) + format
        file_name_tmp = os.path.join(path, filename)
    cv2.imwrite(file_name_tmp,img)
    return name +str(number)

#? 人脸识别函数 kinect_image:kinect原图  known_person_img：已知人的人脸ROI区域图像  known_person_name：已知人的人名字符串
def face_recognize_function(kinect_image):
    msg = face_msgs()
    rect = my_list()
    Unknown_name = 'Unknown'
    Known_name = 'Person'
    msg.index = 0
    face_names = []  #待保存的人脸名称
    # 裁剪图像。减少计算量
    frame_resize_bgr = cv2.resize(kinect_image, (0, 0), fx=0.25, fy=0.25)
    # BGR转RGB
    frame_resize_rgb  =  frame_resize_bgr [:, :, ::-1]
    #检测人脸并获取特征描述符
    face_locations = face_recognition.face_locations(frame_resize_rgb)

    known_person_encodings = []
    face_encodings = []
    # 本地图像
    known_face_list,known_face_names_list= load_images(face_imgs_savepath)
    #仅在库里面有人脸时才进行匹配
    if(len(known_face_list ) > 0):
        #获取已知人脸的特征描述符
        for known_face_img  in known_face_list:
             #人脸匹配函数要求备选特征描述符为数组
            face_encoding_tmplist = face_recognition.face_encodings(known_face_img)
            if(len(face_encoding_tmplist) > 0):
                known_person_encodings.append(face_encoding_tmplist[0])
        #计算当前画面的人脸特征描述子
        face_encodings = face_recognition.face_encodings(frame_resize_rgb, face_locations)
       #人脸比对
        for face_encoding,(top, right , bottom, left)  in zip(face_encodings,face_locations):
                # 默认为unknown
                matches = face_recognition.compare_faces(known_person_encodings, face_encoding)
                name = Unknown_name
                #如果匹配上了，就以匹配的人脸名作为命名
                if True in matches:
                    first_match_index = matches.index(True)
                    name =known_face_names_list[first_match_index]
                else:
                    #如果没匹配上，说明是新人，保存图像，命名为Known_name加自增序号
                    img_roi = kinect_image[top*4:bottom*4,left*4:right*4]
                    name = Known_name
                    name = save_images(img_roi,face_imgs_savepath,name, ".jpg" )
                face_names.append(name)
    #本地没有人脸库时直接保存当前人脸
    else:
        for  (top, right , bottom, left)  in face_locations:
            img_roi = kinect_image[top*4:bottom*4,left*4:right*4]
            name = Known_name
            name =  save_images(img_roi,face_imgs_savepath,name, ".jpg" )
            face_names.append(name)
   
    # 将捕捉到的人脸显示出来
    for (rect.top, rect.right , rect.bottom, rect.left),name in zip(face_locations,face_names):
        # 恢复裁剪之前的坐标
        msg.index +=1
        rect.lable = name
        rect.top *= 4
        rect.right *= 4
        rect.bottom *= 4
        rect.left *= 4
        msg.location.append(rect)
        # 绘制矩形框
        cv2.rectangle(kinect_image, (rect.left , rect.top), (rect.right , rect.bottom ), (0, 0, 255), 2)
        # 加上标签
        cv2.rectangle(kinect_image, (rect.left , rect.bottom  ), (rect.right , rect.bottom  + 35), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(kinect_image, name, (rect.left  + 6, rect.bottom  +29), font, 1.0, (255, 255, 255), 1)
    # 显示
    cv2.imshow('face_recognition', kinect_image)
    # cv2.imshow('face_recohnition', known_person_img)
    cv2.waitKey(1)
    pub.publish(msg)
    print(msg)

#? 订阅Kinect图像的回调函数
def kinect_callback(data):
    bridge = CvBridge()
    global  kinect_img
    kinect_img= bridge.imgmsg_to_cv2(data,"rgb8")

#? 订阅主控节点消息的回调函数    
def Main_callback(data):
    #接受使能信号
    if(data.enable):
        try:
            face_recognize_function(kinect_img)
        except Exception as e:
            print("face_recognizer error :")
            print(e)
    # else:
    #     print("等待使能\n")
    
#初始化 Kinect消息订阅节点
rospy.Subscriber('Kinect_Image_Msgs', Image, kinect_callback)
#初始化 主控函数消息订阅节点
rospy.Subscriber('Main_Enable_Msgs', EnableSignal, Main_callback)

while not rospy.is_shutdown():
    rate.sleep()


