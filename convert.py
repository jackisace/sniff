import unittest

#convert hex into bit string
def hex_bits(a):
    b = bytearray(a)
    endstr = ""
    l = 0
    for i in b:
        newstr = bin(i)[2:]
        #print(len(newstr))
        while len(newstr) < 8:
            newstr = "0" + newstr
        #print(newstr)
        endstr += newstr
        #print(a[l],i,bin(i))
        l = l + 1
    #print(endstr)
    return endstr




class TestConvertMethods(unittest.TestCase):
    def test_hexbits(self):
        test = b'E\x00\x00)\xdaH@\x00\x80\x06\x9a\xbc\xc0\xa8\x01D\xac\xd9\x17\x04\x07\xc5\x01\xbbJ:\xa87bGa?P\x10\x80\x00\xea\x90\x00\x00\x00'
        test = hex_bits(test)
        result = "0100010100000000000000000010100111011010010010000100000000000000100000000000011010011010101111001100000010101000000000010100010010101100110110010001011100000100000001111100010100000001101110110100101000111010101010000011011101100010010001110110000100111111010100000001000010000000000000001110101010010000000000000000000000000000"
        self.assertEqual(test, result)
    def test_singlehexbit(self):
        self.assertEqual(hex_bits("\x01"), "00000001")
    def test_twohexbits(self):
        self.assertEqual(hex_bits("\x01\x02"), "0000000100000010")
    def test_threehexbits(self):
        self.assertEqual(hex_bits("\x01\x02\x0A"), "000000010000001000001010")


        
        




if __name__ == '__main__':
    unittest.main()









