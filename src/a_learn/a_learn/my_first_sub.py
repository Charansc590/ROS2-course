import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class MinimalSubscriber(Node):
    def __init__(self):
        super().__init__('minimal_subscriber')
        self.subscriber=self.create_subscription(String,'topic',self.print_callback,10)
        
    def print_callback(self,msg):
        self.get_logger().info(f'Data : {msg.data}')

def main(args=None):
    rclpy.init(args=args)
    node=MinimalSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
    main()
    
    
