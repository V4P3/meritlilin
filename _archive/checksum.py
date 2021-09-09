#Adds checksum to end, first character (Sync byte) is excluded

def addCheckSum(barray):
    barray.append(sum(barray[1:]) % 256)
    return barray


#EXAMPLES MLP1
tiltU = bytearray.fromhex('DC 01 40 48 11 00')
tiltD = bytearray.fromhex('DC 01 40 44 11 00')
panL = bytearray.fromhex('DC 01 40 42 11 00')
panR = bytearray.fromhex('DC 01 40 41 11 00')
stop = bytearray.fromhex('DC 01 40 00 00 FF')
apan = bytearray.fromhex('DC 01 40 06 00 00')

#EXAMPLES MLP2
tiltU = bytearray.fromhex('E0 01 00 48 11 00')
tiltD = bytearray.fromhex('E0 01 00 44 11 00')
panL = bytearray.fromhex('E0 01 00 42 11 00')
panR = bytearray.fromhex('E0 01 00 41 11 00')
stop = bytearray.fromhex('E0 01 00 00 00 FF')



tiltUStr = addCheckSum(tiltU)
tiltDStr = addCheckSum(tiltD)
panLStr = addCheckSum(panL)
panRStr = addCheckSum(panR)
stopStr = addCheckSum(stop)
apanStr = addCheckSum(apan)

print('Tilt UP:',tiltUStr.hex())
print('Tilt DOWN:',tiltDStr.hex())
print('Pan LEFT:',panLStr.hex())
print('Pan RIGHT:',panRStr.hex())
print('STOP:',stopStr.hex())

#OUTPUT
#Tilt UP: e001004811005a
#Tilt DOWN: e0010044110056
#Pan LEFT: e0010042110054
#Pan RIGHT: e0010041110053
#STOP: e001000000ff00
