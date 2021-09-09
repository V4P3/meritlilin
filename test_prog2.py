import serial
import serial.rs485
#import struct
#import us

def addCheckSum(barray):
    barray.append(sum(barray[1:]) % 256)
    return barray


ser = serial.Serial('com5', 9600)
ser.rs485_mode = serial.rs485.RS485Settings(rts_level_for_tx=True, rts_level_for_rx=False, loopback=False, delay_before_tx=None, delay_before_rx=None)
print(ser.isOpen())

panL = bytearray.fromhex('DC 01 40 42 11 00')
stop = bytearray.fromhex('DC 01 40 00 00 FF')
apan = bytearray.fromhex('DC 01 40 06 00 00')
thestring = addCheckSum(apan)

print(thestring)

ser.write(thestring)
s = ser.read(1)
print(s)
ser.close()
