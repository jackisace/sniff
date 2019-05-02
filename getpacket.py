import socket
import unittest



def getpacket():
    out = open("out.txt", "a+")
    HOST = socket.gethostbyname(socket.gethostname())
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
    s.bind((HOST, 0))
    s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
    s.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
    a = s.recvfrom(65565)
    out.write(str(a))
    s.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)
    return a

class TestGetSocketMethods(unittest.TestCase):
    def test_get(self):
        a = None
        a = getpacket()
        self.assertIsNotNone(a)


if __name__ == '__main__':
    unittest.main()

