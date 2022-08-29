#! /usr/bin/env python3
import rospy
from udp import RosUDP
from serial_port import McuSerial
from subscribe import Listener
from ros_thread import RosThead

if __name__ == '__main__':
    try:
        ## Initialize LAN UDP Communication
        # udp = RosUDP('1.145.14.19', 8888)
        ## Initialize Serial Port Communication
        serial = McuSerial()

        ## Initialize ROS node
        rospy.init_node('MCU', anonymous=False)

        ## Subscribe ROS topic
        sub = Listener()
        spin = RosThead()
        sub.create_subscriber()

        ## Set control rate
        ctl_rate = rospy.Rate(100) # (Unit: Hz)
    
        spin.start() # Start listener node
        time_cnt = 0 # time counter

        ## Loop
        while not rospy.is_shutdown():
            ## Limit logging rate to 1 Hz
            if(time_cnt < 100):
                time_cnt += 1
            elif(time_cnt == 100):
                rospy.loginfo(sub.twist_msg)
                time_cnt = 0

            ## Send ROS msg through UDP port
            # udp.TransmitRosMsg(twist)
            ## Send ROS msg through Serial port
            serial.TransmitRosMsg(sub.twist_msg)

            ctl_rate.sleep()

    except rospy.ROSInterruptException:
        pass