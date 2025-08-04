import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class MinimalPublisher(Node):
    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher=self.create_publisher(Twist,'/turtle1/cmd_vel',10)
        t_p=0.5
        self.timer=self.create_timer(t_p,self.timer_callback)
        self.get_logger().info(f'Node Started')
        

    def timer_callback(self):
        msg=Twist()
        msg.linear.x=2.0
        msg.linear.y=msg.linear.z=msg.angular.z=msg.angular.x=msg.angular.y=0.0
       
        self.publisher.publish(msg)
        

def main(args=None):
    rclpy.init(args=args)
    node=MinimalPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__=='__main__':
    main()
    
    
