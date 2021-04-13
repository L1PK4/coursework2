#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import LaserScan

f = open("data.txt", "wt")
def callback(data):
	f.write(str(list(enumerate(data.ranges))))
	
	
def listener():
	rospy.init_node('listener', anonymous=True)
	rospy.Subscriber("scan", LaserScan, callback)
	rospy.spin()

if __name__ == '__main__':
	listener()
	f.close()