import libmeritlilin
import serial

ser = serial.Serial('COM5', 9600, serial.EIGHTBITS, serial.PARITY_NONE, serial.STOPBITS_ONE)
ptz = libmeritlilin.LILIN_STDFunctions()
pan_tilt_speed = [1, 1]
cmd = ptz.pantilt_up_pressed(pan_tilt_speed)
print("CMD = ", cmd)
ser.write(cmd)
s = ser.read(1)
print(s)
ser.close()
