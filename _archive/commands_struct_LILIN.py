# Everaerts V., 1 SEPT 2021
#
# Structures for Frame and Command Definitions for MERIT LILIN PROTOCOL 2 ( MLP2 )

class liblilin_structs():

	# Frame format:		|synch byte|address|command1|command2|param1|param2|checksum|
	# Bytes 2 - 6 are Payload Bytes
	_frame = {
		'synch_byte': 220, #'0xE0',	# Synch Byte, always E0            -    1 byte
		'address':    0, #'0x00',	# Address                          -    1 byte
        'command1':   0, #'0x00',	# Command1                         -    1 byte
		'command2':   0, #'0x00', 	# Command2                         -    1 byte
		'param1':	  0, #'0x00', 	# Param1	(PAN & TILT SPEED):    -    1 byte
		'param2':	  0, #'0x00', 	# Param2	(ZOOM SPEED):          -    1 byte
        'checksum':	  0, #'0x00'	# Checksum:                        -    1 byte
		 }


	# Format: Command Hex Code
	_function_code = {
		'DOWN':	'0x48',
		'UP':	'0x44',
		'LEFT':	'0x42',
		'RIGHT':'0x41'
		}

# END
