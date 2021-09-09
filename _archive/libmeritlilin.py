from commands_struct_LILIN import *


class LILIN_STDFunctions():

	def __init__(self):
		global std_commands_struct
		std_commands_struct = liblilin_structs()

	# Returns: tuple (command, length of command)
	# Input: Address (optional), command2, pan_speed, tilt_speed
	def _construct_cmd(self, _command2, _pan_speed, _tilt_speed, _address = 1, _command1 = 0):

		# DEBUG
		print("DEBUG _construct_cmd: " + str(_command2) + " " + str(_pan_speed) + " " + str(_tilt_speed))

		# Synch Byte
		std_commands_struct._frame['synch_byte'] = "0x{:02x}".format(std_commands_struct._frame['synch_byte'])

		# Address
		std_commands_struct._frame['address'] = "0x{:02x}".format(_address)

		# Command1
		std_commands_struct._frame['command1'] = "0x{:02x}".format(_command1)

		# Command2
		if _command2 not in std_commands_struct._function_code:
			print( str(_command2) + " not in std_commands_struct._function_code")
			return False
		else:
			std_commands_struct._frame['command2'] = std_commands_struct._function_code[_command2]
			print("_command2 is: " + str(std_commands_struct._frame['command2']))

		# Param1: Tilt & Pan Speed
		print("_tilt_speed is: " + str(_tilt_speed))
		if _tilt_speed > 15:
			_hex_byte_tilt = 'f'
		else:
			_hex_byte_tilt = hex(_tilt_speed)[2:]

		print("_pan_speed is: " + str(_pan_speed))
		if _pan_speed > 15:
			_hex_byte_pan = 'f'
		else:
			_hex_byte_pan = hex(_pan_speed)[2:]

			_hex_byte_param1 = int(_hex_byte_tilt + _hex_byte_pan,16)

		std_commands_struct._frame['param1'] = hex(_hex_byte_param1)

		# Param2: Zoom Speed
		_hex_byte_zoom = 0
		std_commands_struct._frame['param2'] = "0x{:02x}".format(_hex_byte_zoom)

		# Checksum
		_payload_int = int(std_commands_struct._frame['address'],16) + int(std_commands_struct._frame['command1'],16) + \
			int(std_commands_struct._frame['command2'],16) + \
			int(std_commands_struct._frame['param1'],16) + int(std_commands_struct._frame['param2'],16)
		print("_payload_int", _payload_int)


		_checksum = _payload_int % 256
		std_commands_struct._frame['checksum'] = "0x{:02x}".format(_checksum)

		print("_checksum is: " + std_commands_struct._frame['checksum'])

		# assemble command
		_cmd = [int(std_commands_struct._frame['synch_byte'],16 ), int(std_commands_struct._frame['address'],16), int(std_commands_struct._frame['command1'],16) + \
			int(std_commands_struct._frame['command2'],16), \
			int(std_commands_struct._frame['param1'],16), int(std_commands_struct._frame['param2'],16), int(std_commands_struct._frame['checksum'],16)]

		print("Final _cmd:")
		for i in std_commands_struct._frame:
			print(i + " : " + std_commands_struct._frame[i], end=" ")
		print("")

		#return (_cmd, None)
		return (_cmd)

	############ Commands #################################################################

	### STOP #############################################
	#
	#def pantilt_stop(self):
	#	retval = self._construct_cmd('STOP', 0, 0)
	#	return retval


	### UP ###############################################

	def pantilt_up_pressed(self, _pan_tilt_speed):
		retval = self._construct_cmd('UP', int(_pan_tilt_speed[0]), int(_pan_tilt_speed[1]))
		return retval

	def pantilt_up_released(self, _pan_tilt_speed):
		retval = self.pantilt_stop()
		return retval


	### DOWN #########################################

	def pantilt_down_pressed(self, _pan_tilt_speed):
		retval = self._construct_cmd('DOWN', int(_pan_tilt_speed[0]), int(_pan_tilt_speed[1]))
		return retval

	def pantilt_down_released(self, _pan_tilt_speed):
		retval = self.pantilt_stop()
		return retval

	### LEFT #########################################

	def pantilt_left_pressed(self, _pan_tilt_speed):
		retval = self._construct_cmd('LEFT', int(_pan_tilt_speed[0]), int(_pan_tilt_speed[1]))
		return retval

	def pantilt_left_released(self, _pan_tilt_speed):
		retval = self.pantilt_stop()
		return retval

	### RIGHT #########################################

	def pantilt_right_pressed(self, _pan_tilt_speed):
		retval = self._construct_cmd('RIGHT', int(_pan_tilt_speed[0]), int(_pan_tilt_speed[1]))
		return retval

	def pantilt_right_released(self, _pan_tilt_speed):
		retval = self.pantilt_stop()
		return retval

class LILIN_EXTFunctions():

	def __init__(self):
		global ext_commands_struct
		pass #WORK IN PROGRESS

# EOF
