#!/usr/bin/env python3

import rospy
import pickle as pkl
from sensor_msgs.msg import LaserScan


d = []
f = open("data.pickle", "wb")
def callback(data):
	#f.write(str(list(enumerate(data.ranges))))
	d.append(data.ranges)
	
	
def listener():
	rospy.init_node('listener', anonymous=True)
	rospy.Subscriber("scan", LaserScan, callback)
	rospy.spin()

if __name__ == '__main__':
	listener()
	pkl.dump(d, f)
	f.close()