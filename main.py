import socket
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

def hex_bits(a):
    b = bytearray(a)
    for i in b:
        print(i, bin(i))


def what():
    pass

def we():
    pass


def analyse():

    test = b'E\x00\x00)\xdaH@\x00\x80\x06\x9a\xbc\xc0\xa8\x01D\xac\xd9\x17\x04\x07\xc5\x01\xbbJ:\xa87bGa?P\x10\x80\x00\xea\x90\x00\x00\x00'

    print(hex_bits(test))


analyse()



