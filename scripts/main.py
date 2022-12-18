#! /usr/bin/env python3
import rospy
from udp import RosUDP
from serial_port import McuSerial
from subscribe import Listener
from ros_thread import RosThead

if __name__ == '__main__':
    try:
        rate = 200 # control frequency in Hz
        time_cnt = 0 # time counter

        ## Initialize LAN UDP Communication
        udp = RosUDP('1.145.14.19', 8888)
        
        ## Initialize Serial Port Communication
        # serial = McuSerial()

        ## Initialize ROS node
        rospy.init_node('MCU', anonymous=False)

        ## Subscribe ROS topic
        sub = Listener()
        spin = RosThead()
        sub.create_subscriber()

        ## Set control rate
        ctl_rate = rospy.Rate(rate) # (Unit: Hz)
    
        spin.start() # Start listener node

        ## Loop
        while not rospy.is_shutdown():
            ## Limit logging rate to 1 Hz
            if(time_cnt < rate):
                time_cnt += 1
            else:
                rospy.loginfo(sub.twist_msg)
                time_cnt = 0

            ## Send ROS msg through UDP port
            udp.TransmitRosMsg(sub.twist_msg)

            ## Send ROS msg through Serial port
            # serial.TransmitRosMsg(sub.twist_msg)

            ctl_rate.sleep()

    except rospy.ROSInterruptException:
        pass