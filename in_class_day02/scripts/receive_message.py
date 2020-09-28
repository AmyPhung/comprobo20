#!/usr/bin/env python

""" Investigate receiving a message using a callback function """
from geometry_msgs.msg import PointStamped
import rospy

class ReceiveMessage():
    def __init__(self):
        rospy.init_node('receive_message')
        rospy.Subscriber("/my_point", PointStamped, process_point)

    def process_point(self, msg):
        print(msg.header)

if __name__ == "__main__":
    ReceiveMessage()
    rospy.spin()
