#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

class DistanceEStop():
    def __init__(self):
        rospy.init_node("distance_estop")
        self.scan_sub = rospy.Subscriber("/scan", LaserScan, self.scanCB)
        self.twist_pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10)
        self.update_rate = rospy.Rate(10)
        self.activated = 1

    def scanCB(self, msg):
        if msg.range_min < 0.5: # e-stop if something is close
            self.activated = 0
        else:
            self.activated = 1

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
    d_estop = DistanceEStop()
    d_estop.run()
