from example_interfaces.srv import AddTwoInts
import rclpy
from rclpy.node import Node

class MinimalService(Node):
    def __init__(self):
        super().__init__('minimal_service')
        self.srv=self.create_service(AddTwoInts,'/add_two_ints',self.add_callback)

    def add_callback(self,request,response):
        response.sum=request.a-request.b
        return response

def main(args=None):
    rclpy.init(args=args)
    node=MinimalService()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__=='__main__':
    main()