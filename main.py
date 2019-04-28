#import getpacket
#getpacket.get()


def convert(a):
    print(a)
    print(bin(a))
    
#convert(23)






def hex_bits(a):
    b = bytearray(a)
    l = 0
    for i in b:
        newstr = bin(i)[2:]
        print(len(newstr))
        while len(newstr) < 8:
            newstr = "0" + newstr
        print(newstr)
            
        print(a[l],i,bin(i))
        l = l + 1


def analyse():
    test = b'E\x00\x00)\xdaH@\x00\x80\x06\x9a\xbc\xc0\xa8\x01D\xac\xd9\x17\x04\x07\xc5\x01\xbbJ:\xa87bGa?P\x10\x80\x00\xea\x90\x00\x00\x00'

    print(hex_bits(test))


analyse()













