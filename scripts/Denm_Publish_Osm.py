import rclpy
from rclpy.node import Node
from v2xvf_interfaces.msg import MapObject
from ros_etsi_its_msgs.msg import DENM

class DenmPublisher(Node):
    def __init__(self):
        super().__init__('denm_node')
        self.publisher_ = self.create_publisher(MapObject, 'map_manager_denm',10)  #change this 10 to 1000 when doing real
        timer_period = 0.5 #seconds
        self.timer = self.create_timer(timer_period, self.Mapped_data)
        self.i = 0

        #Subcriber
        self.subscription = self.create_subscription(DENM,'/dummy_DENM',Denm_Callback,10)
        self.subscription # prevent unused variable warning

    def Denm_Callback(self,data):
        print("Inside listener callback")

    def Mapped_data(self):
        map_object = MapObject()
        map_object.source = 1 #doesnt take source after . automatically
        self.publisher_.publish(map_object)
        self.get_logger().info('Publishing: "%s"' %map_object.source)  #incomplete : need to mention %map_object.source
        self.i += 1

def main(args=None):
    rclpy.init(args=args)

    denm_node = DenmPublisher()
    
    rclpy.spin(denm_node)

    denm_node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()