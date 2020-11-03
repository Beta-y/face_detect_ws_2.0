#!/usr/bin/env python
#encoding:utf-8
#?  Instructions :
#?  rosrun face_detector main_loop.py 
#?  注意使用笔记本前置摄像头作了图像镜像处理


import rospy
import face_recognition
import cv2
import numpy as np
from face_detector.msg import face_msgs
from face_detector.msg import my_list
from face_detector.msg  import EnableSignal
from sensor_msgs.msg import Image
from cv_bridge import CvBridge,CvBridgeError
from std_msgs.msg import Header


#初始化  turty_face_detector  消息发布节点
rospy.init_node('main_node')
main_pub = rospy.Publisher('Main_Enable_Msgs', EnableSignal, queue_size=1)
rate = rospy.Rate(10)

# ? 订阅人脸位置的回调函数
def face_locate_callback(msgs):
    global face_locate_msgs
    face_locate_msgs = msgs  
    print(face_locate_msgs)

#? 订阅Kinect图像的回调函数
def kinect_callback(data):
    bridge = CvBridge()
    kinect_image = bridge.imgmsg_to_cv2(data,"rgb8")
    try:
        # 绘制矩形框
        #TODO 这里好像不同回调函数由于时间片不同时，所以全局变量face_locate_msgs会出现无内容的情况，
        #TODO 不过主节点应该能够解决这个问题嘻嘻
        # cv2.rectangle(kinect_image, (face_locate_msgs.location[0].left , face_locate_msgs.location[0].top), (face_locate_msgs.location[0].right , face_locate_msgs.location[0].bottom ), (0, 0, 255), 2)
        cv2.imshow('main_loop', kinect_image)
        cv2.waitKey(1)
        #发布人脸识别使能信号
        enable_face_recognizer = 1
        main_pub.publish(enable_face_recognizer)
    except Exception as e:
        print("main loop error :")
        print(e)

rospy.Subscriber('Topic_Recognition_Msg', face_msgs, face_locate_callback)
rospy.Subscriber('Kinect_Image_Msgs', Image, kinect_callback)
# rospy.spin()
while not rospy.is_shutdown():
    rate.sleep()

