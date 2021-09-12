from pynput import keyboard
import serial
import serial.rs485

#declare pan and tilt speed
panSpeed = 1
tiltSpeed = 1

def PanTilt(_panSpeed, _tiltSpeed):
    #returns the pan & tilt speeds as hex string
    partA = '10'
    partB = format(_panSpeed, '03b')
    partC = format(_tiltSpeed, '03b')

    _speed = hex(int(partA + partB + partC,2))[2:]
    print('Part speed: {0}'.format(_speed))
    return _speed
    
def KeyToCode(_key):
    #translating the keyboard presses to actions for the PTZ camera
    global panSpeed
    global tiltSpeed
    
    _keycode = {
        keyboard.Key.right: '01',
        keyboard.Key.left: '02',
        keyboard.Key.up: '04',
        keyboard.Key.down: '08'
    }
    if _key not in _keycode:
        _command1 = '00'
        if _key == '+':
            panSpeed += 1
            tiltSpeed += 1
        elif _key == '-':
            panSpeed -= 1
            tiltSpeed -= 1
    else:
        _command1 = _keycode[_key]

    #Pan & Tiltspeed goes from 0 till 7
    panSpeed = max(min(7, panSpeed), 0)
    tiltSpeed = max(min(7, tiltSpeed), 0)
    _command2 = PanTilt(panSpeed, tiltSpeed)
    
    return (_command1,_command2)

def CodeToCam(_adress, _com1, _com2 = '89'):
    #_adress = '01'
    _stringCode = _adress + _com1 + _com2
    #DEBUG
    print('Full command {0} for camera'.format(_stringCode))
    return _stringCode
    

def on_press(key):
    code = ''
    try:
        #print('alphanumeric key {0} pressed, no action!'.format(key.char))
        code = KeyToCode(key.char)
    except AttributeError:
        #print('special key {0} pressed'.format(key))
        code = KeyToCode(key)
        #print('Code {0} to camera'.format(str(code)))
    if code != '':
        command = CodeToCam('01',code[0],code[1])
        byteCommand = bytearray.fromhex(command)
        ser.write(byteCommand)
        #s = ser.read(1)
        #print('Camera output: {0}'.format(s))

def on_release(key):
    print('{0} released'.format(key))
    if key == keyboard.Key.esc:
        # Stop listener
        ser.close()
        return False

ser = serial.Serial('com5', 9600)
ser.rs485_mode = serial.rs485.RS485Settings(rts_level_for_tx=True, rts_level_for_rx=False, loopback=False, delay_before_tx=None, delay_before_rx=None)


# Collect events until released
#with keyboard.Listener(
#       on_press=on_press,
#       on_release=on_release) as listener:
#   listener.join()

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()
