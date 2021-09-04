import serial
import serial.rs485
#import struct
#import us
 
ser = serial.Serial('com5', 9600)
ser.rs485_mode = serial.rs485.RS485Settings(rts_level_for_tx=True, rts_level_for_rx=False, loopback=False, delay_before_tx=None, delay_before_rx=None)
print(ser.isOpen())
#thestring = bytearray.fromhex('DC 01 00 44 11 00 56')
thestring = bytearray.fromhex("DC014006000047")
 
print(thestring)
 
ser.write(thestring)
s = ser.read(1)
print(s)
ser.close()
