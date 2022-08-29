from io import BytesIO
import serial

class McuSerial:
    def __init__(self) -> None:
        self.serial = serial.Serial()

    def OpenPort(self):
        self.serial.port = "/dev/ttyACM0"
        self.serial.baudrate = 115200
        self.serial.bytesize = 8
        self.serial.stopbits = 1
        self.serial.parity = "N"
        self.serial.timeout = 5
        self.serial.open()

    def ClosePort(self):
        self.serial.close()

    def Transmit(self, data):
        self.OpenPort()
        if(self.serial.isOpen()):
            self.serial.write(data)
        else:
            print('Sending message failed, please check your connection')
        self.ClosePort()

    def TransmitRosMsg(self, ros_msg):
        temp_bytes = BytesIO()

        temp_bytes.seek(0)
        ros_msg.serialize(temp_bytes)
        temp_bytes.seek(0)

        self.Transmit(temp_bytes.read())
