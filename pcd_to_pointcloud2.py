#!/usr/bin/env python

import rospy
import pcl
from sensor_msgs.msg import PointCloud2
from sensor_msgs import point_cloud2
import sensor_msgs.point_cloud2 as pc2

def pcd_to_pointcloud2(pcd_file):
    # 读取PCD文件
    cloud = pcl.load(pcd_file)
    
    # 创建PointCloud2消息
    header = rospy.Header()
    header.stamp = rospy.Time.now()
    header.frame_id = 'map'
    
    points = []
    for point in cloud:
        points.append([point[0], point[1], point[2]])
    
    pointcloud2_msg = pc2.create_cloud_xyz32(header, points)
    
    return pointcloud2_msg

def main():
    rospy.init_node('pcd_to_pointcloud2_node')
    pub = rospy.Publisher('/pointcloud2', PointCloud2, queue_size=10)
    
    pcd_file = '/home/rabbit.pcd'
    pointcloud2_msg = pcd_to_pointcloud2(pcd_file)
    
    rate = rospy.Rate(1)  # 1 Hz
    while not rospy.is_shutdown():
        pub.publish(pointcloud2_msg)
        print("111")
        rate.sleep()

if __name__ == '__main__':
    main()