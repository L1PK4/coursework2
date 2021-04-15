#!/usr/bin/env python3

import rospy
import pickle as pkl
from sensor_msgs.msg import LaserScan

d = []
f = open("../data/data.pickle", "wb")

def callback(data):
	y = data.ranges
	x = [i for i in range(len(y))]
	d.append((x[::3], y[::3]))
	
	
def listener():
	rospy.init_node('listener', anonymous=True)
	rospy.Subscriber("scan", LaserScan, callback)
	rospy.spin()

if __name__ == '__main__':
	listener()
	pkl.dump(d, f)
	f.close()