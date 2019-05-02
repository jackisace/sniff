from convert import *
from getpacket import *
from analyse import *
import binascii

newpacket = getpacket()

msg = newpacket[0]
ip = newpacket[1]


packetbits = hex_bits(msg)


thisPacket = fullPacket(packetbits)
print(thisPacket.sourceIP[0],thisPacket.sourceIP[1],thisPacket.sourceIP[2],thisPacket.sourceIP[3])









