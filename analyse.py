from convert import *
from getpacket import *


class fullPacket:
    def __init__(self, packetbits):
        self.sourceIP = []
        self.destinationIP = [] 

        self.version = binToInt(packetbits[0:4])
        self.ihl = binToInt(packetbits[4:8])
        self.dscp = binToInt(packetbits[8:14])
        self.ecn = binToInt(packetbits[14:16])
        self.length = binToInt(packetbits[16:32])
        self.identification = binToInt(packetbits[32:48])
        self.flags = packetbits[48:51]
        self.fragmentOffset = binToInt(packetbits[51:64])
        self.ttl = binToInt(packetbits[64:72])
        self.protocol = binToInt(packetbits[72:80])
        self.headerChecksum = binToInt(packetbits[80:96])
        self.rawSourceIP = binToInt(packetbits[96:128])
        self.rawDestinationIP = binToInt(packetbits[128:160])
        self.data = packetbits[160:]

        self.sourceIP.append(binToInt(packetbits[96:104]))
        self.sourceIP.append(binToInt(packetbits[104:112]))
        self.sourceIP.append(binToInt(packetbits[112:120]))
        self.sourceIP.append(binToInt(packetbits[120:128]))

        self.destinationIP.append(binToInt(packetbits[128:136]))
        self.destinationIP.append(binToInt(packetbits[136:144]))
        self.destinationIP.append(binToInt(packetbits[144:152]))
        self.destinationIP.append(binToInt(packetbits[152:160]))


