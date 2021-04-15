#!/usr/bin/env python3

import rospy
import pickle as pkl
from sensor_msgs.msg import LaserScan


d = []
i = 0
f = open("data.pickle", "wb")
def callback(data):
	#f.write(str(list(enumerate(data.ranges))))
	a = data.ranges
	b = [i for i in range(len(a))]
	print(b, a)
	d.append((b[::30], a[::30]))
	
	
	
def listener():
	rospy.init_node('listener', anonymous=True)
	rospy.Subscriber("scan", LaserScan, callback)
	rospy.spin()

if __name__ == '__main__':
	listener()
	pkl.dump(d, f)
	f.close()