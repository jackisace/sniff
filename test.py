def hex_bits(a):
    b = bytearray(a)
    for i in b:
        print(i, bin(i))


def analyse():
    test = b'E\x00\xFF\x00)\xdaH@\x00\x80\x06\x9a\xbc\xc0\xa8\x01D\xac\xd9\x17\x04\x07\xc5\x01\xbbJ:\xa87bGa?P\x10\x80\x00\xea\x90\x00\x00\x00'

    print(hex_bits(test))


analyse()
print("hw")
