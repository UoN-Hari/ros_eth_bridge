#! /usr/bin/env python3
import rospy
from threading import Thread


class RosThead:
    def __init__(self) -> None:
        self.thread_ros_spin = Thread(target=self.thread_job_spin)
    
    def start(self):
        self.thread_ros_spin.start()

    def thread_job_spin(self):
        rospy.spin()