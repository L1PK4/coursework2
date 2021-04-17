#!/usr/bin/env python3

import rospy
import pickle as pkl
from sensor_msgs.msg import LaserScan
import numpy as np

d = []
f = open("../data/data.pickle", "wb")

def clean_from_inf(x, y):
	temp = list(zip(x, y))
	temp = list(filter(lambda x: not np.isinf(x[1]), temp))
	temp = zip(*temp)
	temp = list(temp)
	return temp

def callback(data):
	y = list(data.ranges)
	x = [i for i in range(len(y))]
	print(len(x), len(y))
	x, y = clean_from_inf(x, y)
	d.append((x[::3], y[::3]))
	
	
def listener():
	rospy.init_node('listener', anonymous=True)
	rospy.Subscriber("scan", LaserScan, callback)
	rospy.spin()

if __name__ == '__main__':
	listener()
	pkl.dump(d, f)
	f.close()