#!/usr/bin/env python
import rospy
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion
from geometry_msgs.msg import Twist
import math


class turtlebot:

    def __init__(self):
        
        self.roll = 0
        self.pitch = 0
        self.yaw = 0

        # Assuming Polaris to be at 90 degrees wrt world always
        self.target = 90

        # Weight for proportional controller
        self.Kp = 0.5

        self.sub = rospy.Subscriber('/odom', Odometry,self.get_rotation)
        self.pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)   
                
    # Call back function for subscriber

    def get_rotation (self,msg):
        
        orientation_q = msg.pose.pose.orientation
        orientation_list = [orientation_q.x, orientation_q.y, orientation_q.z, orientation_q.w]
        (self.roll, self.pitch, self.yaw) = euler_from_quaternion (orientation_list)
    
    # Function to initiate twist    
    def twist_bot(self):
        
        self.command = Twist()
        r = rospy.Rate(10)  

        # Deg to rad         
        target_rad = self.target * math.pi/180

        # Proportional control to allow for controlled twist along yaw   
        self.command.angular.z = self.Kp * (target_rad - self.yaw)

        self.pub.publish(self.command)
        print("Target={}    Current:{}".format(target_rad,self.yaw))
        r.sleep()   
   
if __name__ == '__main__':
    
    rospy.init_node('rotate_robot',anonymous=True)
    x = turtlebot()
    while not rospy.is_shutdown():
        x.twist_bot()
