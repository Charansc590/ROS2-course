import sys

from example_interfaces.srv import AddTwoInts
import rclpy
from rclpy.node import Node

class MinimalClientService(Node):
    def __init__(self):
        super().__init__('minimal_service')
        self.client=self.create_client(AddTwoInts,'/add_two_ints')
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available')
        self.req=AddTwoInts.Request()

    def send_request(self,a,b):
        self.req.a=a
        self.req.b=b
        self.future=self.client.call_async(self.req)
        rclpy.spin_until_future_complete(self,self.future)
        return self.future.result()


def main(args=None):
    rclpy.init(args=args)
    minimal_client=MinimalClientService()
    response=minimal_client.send_request(int(sys.argv[1]),int(sys.argv[2]))
    minimal_client.get_logger().info(
        'result of ints =%d' % response.sum
    )
    minimal_client.destroy_node()
    rclpy.shutdown()


if __name__=='__main__':
    main()