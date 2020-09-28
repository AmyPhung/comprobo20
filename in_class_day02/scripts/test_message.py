#!/usr/bin/env python
""" This script explores publishing ROS messages in ROS using Python """
from geometry_msgs.msg import PointStamped
from std_msgs.msg import Header
from geometry_msgs.msg import Point
import rospy


rospy.init_node('test_message')    # initialize ourselves with roscore

my_point_stamped = PointStamped(header=Header(stamp=rospy.Time.now(),
                                              frame_id="odom"),
                                point=Point(1.0, 2.0, 0.0))
print(my_point_stamped)

publisher = rospy.Publisher('/my_point', PointStamped, queue_size=10)
# rospy.Rate specifies the rate of the loop (in this case 2 Hz)
r = rospy.Rate(2)
while not rospy.is_shutdown():
    my_point_stamped.header.stamp = rospy.Time.now()    # update timestamp
    publisher.publish(my_point_stamped)
    r.sleep()
