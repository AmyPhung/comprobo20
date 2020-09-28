#!/usr/bin/env python3

import rospy
from gazebo_msgs.msg import ContactsState
from geometry_msgs.msg import Twist

class EStop():
    def __init__(self):
        rospy.init_node("estop")
        self.bump_sub = rospy.Subscriber("/bumper", ContactsState, self.bumpCB)
        self.twist_pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10)
        self.update_rate = rospy.Rate(10)
        self.activated = 1

    def bumpCB(self, msg):
        if len(msg.states) > 0:
            rospy.loginfo_once("E-stopped due to bumper")
            self.activated = 0

    def run(self):
        while not rospy.is_shutdown():
            if self.activated == 1:
                cmd = Twist()
                cmd.linear.x = 0.4
                self.twist_pub.publish(cmd)
            else:
                cmd = Twist()
                cmd.linear.x = 0
                self.twist_pub.publish(cmd)

            self.update_rate.sleep()


if __name__ == "__main__":
    es = EStop()
    es.run()
