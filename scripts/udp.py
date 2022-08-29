#! /usr/bin/env python3
import socket
from io import BytesIO


class RosUDP:
    def __init__(self, ip, port) -> None:
        self.ip = ip
        self.port = port

    def TransmitStr(self, buff):
        udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, True)
        udp_socket.sendto(buff, (self.ip, self.port))

        udp_socket.close()

    def TransmitRosMsg(self, ros_msg):
        bytes = BytesIO()

        bytes.seek(0)
        ros_msg.serialize(bytes)
        bytes.seek(0)

        self.TransmitStr(bytes.read())

