#!/usr/bin/env python3 

import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts

class Talker(Node):
    def __init__(self):
        super().__init__('talker_node')
        
        self.srv=self.create_service(AddTwoInts,'/add_two_ints',self.add_callback)

        self.declare_parameter('topic_name','add')

        #self.publisher=self.create_publisher(String,topic_name,10)
        #timer=1.0
        #self.timer=self.create_timer(timer,self.timer_callback)
        #self.counter=0

    def add_callback(self,request,response):
        self.oper=self.get_parameter('topic_name').get_parameter_value().string_value
        if self.oper == 'add':
            response.sum=request.a + request.b
            return response
        else:
            response.sum=request.a - request.b
            return response

def main(args=None):
    rclpy.init(args=args)
    node=Talker()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__=='__main__':
    main()
