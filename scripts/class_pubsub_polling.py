#!/usr/bin/python

import rospy
from sensor_msgs.msg import LaserScan

import numpy as np
from rospy.numpy_msg import numpy_msg 

class LIDAR_RYCSV:
    
    def __init__(self):

        self.nameTopicSub = "/scan"
        self.nameTopicPub = "/scan_fixed"
        self.newMsg = LaserScan() # LaserScan msg

        # Subscribers
        rospy.Subscriber(self.nameTopicSub, numpy_msg(LaserScan), self.Lidar_Callback, queue_size=10 )

        # Publisher
        self.pub = rospy.Publisher(self.nameTopicPub, numpy_msg(LaserScan), queue_size=10)          

    #--------------------------------------------------------------------------------------#
    # Callback o interrupcion
    def Lidar_Callback(self, lidar_scan):
        
        new_msgLaserScan = lidar_scan
        new_msgRanges    = lidar_scan.ranges.copy()

        # Solution to exercise
        for ii in range(len(new_msgRanges)):
            if(new_msgRanges[ii] < 0.5 or new_msgRanges[ii] > 10.0):
                new_msgRanges[ii]=0.0

        new_msgLaserScan.ranges = new_msgRanges
        self.newMsg = new_msgLaserScan