import rospy
from geometry_msgs.msg import Twist


class Listener:
    twist_msg = Twist()

    def __init__(self) -> None:
        pass

    def Callback(self, data):
        self.twist_msg = data
        rospy.loginfo(rospy.get_caller_id() + "\nReceived ROS msg: %s", data)

    def create_subscriber(self):
        rospy.Subscriber('/cmd_vel', Twist, self.Callback, queue_size=1, tcp_nodelay=True)