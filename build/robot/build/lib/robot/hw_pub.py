"""
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import pigpio

# Motor GPIO configuration
LEFT_2 = 12     # PWM pin for left motor (GPIO12 - PWM0)
LEFT_1 = 5      # Direction pin for left motor
RIGHT_1 = 13    # PWM pin for right motor (GPIO13 - PWM1)
RIGHT_2 = 6     # Direction pin for right motor

MAX_PWM = 255     # Max PWM value

class DiffDriveNode(Node):
    def __init__(self):
        super().__init__('diff_drive_node')

        # Initialize pigpio
        self.pi = pigpio.pi()
        if not self.pi.connected:
            self.get_logger().error("Failed to connect to pigpio daemon!")
            exit(1)

        # Set GPIO modes
        self.pi.set_mode(LEFT_1, pigpio.OUTPUT)
        self.pi.set_mode(LEFT_2, pigpio.OUTPUT)
        self.pi.set_mode(RIGHT_1, pigpio.OUTPUT)
        self.pi.set_mode(RIGHT_2, pigpio.OUTPUT)

        # Subscribe to /cmd_vel
        self.create_subscription(Twist, '/cmd_vel', self.cmd_vel_callback, 10)
        self.get_logger().info("Differential Drive Node started (using pigpio)")

    def cmd_vel_callback(self, msg: Twist):
        linear = msg.linear.x
        angular = msg.angular.z

        # Convert Twist to left/right motor speed
        wheel_separation = 0.3  # distance between wheels in meters
        left_speed = linear - (angular * wheel_separation / 2.0)
        right_speed = linear + (angular * wheel_separation / 2.0)

        # Convert to PWM
        left_pwm = int(max(min(abs(left_speed) * MAX_PWM, MAX_PWM), 0))
        right_pwm = int(max(min(abs(right_speed) * MAX_PWM, MAX_PWM), 0))

        # Set direction
        self.pi.write(LEFT_DIR, 0 if left_speed >= 0 else 1)
        self.pi.write(RIGHT_DIR, 0 if right_speed >= 0 else 1)

        # Set PWM duty cycle (0-255)
        self.pi.set_PWM_dutycycle(LEFT_PWM, left_pwm)
        self.pi.set_PWM_dutycycle(RIGHT_PWM, right_pwm)

        self.get_logger().info(
            f"Linear: {linear:.2f}, Angular: {angular:.2f} | "
            f"Left: {left_speed:.2f} (PWM {left_pwm}), Right: {right_speed:.2f} (PWM {right_pwm})"
        )

    def destroy_node(self):
        # Stop motors on shutdown
        self.pi.set_PWM_dutycycle(LEFT_PWM, 0)
        self.pi.set_PWM_dutycycle(RIGHT_PWM, 0)
        self.pi.stop()
        super().destroy_node()

def main(args=None):
    rclpy.init(args=args)
    node = DiffDriveNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
"""


import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import pigpio

# Left motor
LEFT_IN1 = 5
LEFT_IN2 = 12
LEFT_EN = 23  # PWM

# Right motor
RIGHT_IN1 = 13
RIGHT_IN2 = 6
RIGHT_EN = 24  # PWM

MAX_PWM = 255

class DiffDriveNode(Node):
    def __init__(self):
        super().__init__('diff_drive_node')
        

        # Initialize pigpio
        self.pi = pigpio.pi()
        if not self.pi.connected:
            self.get_logger().error("Failed to connect to pigpio daemon!")
            exit(1)

        # Set GPIO modes
        self.pi.set_mode(LEFT_IN1, pigpio.OUTPUT)
        self.pi.set_mode(LEFT_IN2, pigpio.OUTPUT)
        self.pi.set_mode(LEFT_EN, pigpio.OUTPUT)
        self.pi.set_mode(RIGHT_IN1, pigpio.OUTPUT)
        self.pi.set_mode(RIGHT_IN2, pigpio.OUTPUT)
        self.pi.set_mode(RIGHT_EN, pigpio.OUTPUT)

        # Subscribe to /cmd_vel
        self.create_subscription(Twist, '/cmd_vel', self.cmd_vel_callback, 10)
        self.get_logger().info("Differential Drive Node started (L298N + pigpio)")


    def cmd_vel_callback(self, msg: Twist):
        linear = msg.linear.x
        angular = msg.angular.z

        if linear==1: #forward
            self.pi.write(LEFT_IN1, 0 )
            self.pi.write(LEFT_IN2, 1 )
            self.pi.write(RIGHT_IN1, 0 )
            self.pi.write(RIGHT_IN2, 1 )

        elif linear==-1:
            self.pi.write(LEFT_IN1, 1 )
            self.pi.write(LEFT_IN2, 0 )
            self.pi.write(RIGHT_IN1, 1 )
            self.pi.write(RIGHT_IN2, 0 )

        elif angular==1:
            self.pi.write(LEFT_IN1, 1 )
            self.pi.write(LEFT_IN2, 0 )
            self.pi.write(RIGHT_IN1, 0 )
            self.pi.write(RIGHT_IN2, 1 )


        elif angular==-1:
            self.pi.write(LEFT_IN1, 0 )
            self.pi.write(LEFT_IN2, 1 )
            self.pi.write(RIGHT_IN1, 1 )
            self.pi.write(RIGHT_IN2, 0 )

        else:
            self.pi.write(LEFT_IN1, 0 )
            self.pi.write(LEFT_IN2, 0 )
            self.pi.write(RIGHT_IN1, 0 )
            self.pi.write(RIGHT_IN2, 0 )


        self.get_logger().info(
            f"Linear: {linear:.2f}, Angular: {angular:.2f} | "
        )

    def destroy_node(self):
        # Stop motors on shutdown
        self.pi.set_PWM_dutycycle(LEFT_EN, 0)
        self.pi.set_PWM_dutycycle(RIGHT_EN, 0)
        self.pi.stop()
        super().destroy_node()

def main(args=None):
    rclpy.init(args=args)
    node = DiffDriveNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
