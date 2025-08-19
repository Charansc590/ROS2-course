import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class MinimalPublisher(Node):
    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher=self.create_publisher(String,'topic',10)
        t_p=0.5
        self.timer=self.create_timer(t_p,self.timer_callback)
        self.get_logger().info(f'Node Started')
        self.i=0

    def timer_callback(self):
        msg=String()
        msg.data=f'Hello ROS2:{self.i}' 
        self.publisher.publish(msg)
        self.i+=1

def main(args=None):
    rclpy.init(args=args)
    node=MinimalPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__=='__main__':
    main()
    
    
