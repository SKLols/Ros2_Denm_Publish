#!/usr/bin/env python3 

import rclpy
from rclpy.node import Node
from v2xvf_interfaces.msg import MapObject
from ros_etsi_its_msgs.msg import DENM

class DenmPublisher(Node):

    def __init__(self):
        #calling constructor of the node class
        super().__init__('denm_node')
        self.denm_subscriber_= self.create_subscription(DENM, "/dummy_DENM", self.denm_data, 10)
        self.denm_publisher_= self.create_publisher (MapObject, "/map_manager", 10)
        #self.counter_= 0
        #self.timer=self.create_timer(0.5, self.Mapped_data)
        self.get_logger().info("Dummy Node for DENM_Publish")
    
    def denm_data (self, ros_denm_msg : DENM):
        denm_msg = MapObject()
        denm_msg.position.latitude = ros_denm_msg.management.event_position.latitude
        denm_msg.position.longitude = ros_denm_msg.management.event_position.longitude
        denm_msg.type = "test_1"
        denm_msg.source = "test_2"
        denm_msg.source_id = ros_denm_msg.situation.linked_cause.cause_code
        denm_msg.id = "test_3"
        #denm_msg.s = ros_denm_msg.

        self.denm_publisher_.publish(denm_msg)

def main(args=None):
    
    #initialise ros2 communication
    rclpy.init(args=args)

    #create a node
    denm_node = DenmPublisher()

    #spin the node
    rclpy.spin(denm_node)
    rclpy.shutdown()

#To run file directly from the terminal
if __name__ == '__main__':
    main()