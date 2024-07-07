#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math
import sys 

class GoToCoordinate(Node):
    
    def __init__(self):
        super().__init__('go_to_coordinate')
        self.get_logger().info('go_to_coordinate node has been started')
        self.cmd_vel_pub_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.pose_sub_ = self.create_subscription(Pose, '/turtle1/pose', self.getCurrentPosition, 10)
        self.timer = self.create_timer(0.1, self.goToCoordinate)
        self.pose = Pose()
        self.destination_reached = False


    def getCurrentPosition(self, data):
        self.pose = data

    def findAngle(self, target_x, target_y):
        return math.atan2(target_y - self.pose.y, target_x - self.pose.x)

    def goToCoordinate(self):

        dest_pos = Pose()
        dest_pos.x = float(sys.argv[1])
        dest_pos.y = float(sys.argv[2])
        dest_pos.theta = self.findAngle(dest_pos.x, dest_pos.y)

        msg = Twist()

        angle_to_goal = dest_pos.theta
        if abs(angle_to_goal - self.pose.theta) > 0.1:
            if angle_to_goal - self.pose.theta > 0:
                msg.angular.z = 1.0
            else:
                msg.angular.z = -1.0
        else:
            distance_to_goal = math.sqrt((dest_pos.x - self.pose.x) ** 2 + (dest_pos.y - self.pose.y) ** 2)
            if distance_to_goal > 0.1:
                msg.linear.x = distance_to_goal
            else:
                self.destination_reached = True
                self.get_logger().info('Destination reached.')
                self.cmd_vel_pub_.publish(Twist())  # Stop the turtle
                quit()

        self.cmd_vel_pub_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = GoToCoordinate()
    rclpy.spin(node)

