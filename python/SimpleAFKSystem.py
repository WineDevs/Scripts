from ctypes import windll, Structure, c_long, byref
import time

class POINT(Structure):
    _fields_ = [("x", c_long), ("y", c_long)]

def getMousePosition():
    pt = POINT()
    windll.user32.GetCursorPos(byref(pt))
    return {'x': pt.x, 'y': pt.y}

def ifAfk(seconds_to_check: int,debug):#Return true if user in afk, else false
    last_x = getMousePosition()['x']
    last_y = getMousePosition()['y']
    if debug:
        print('Last X: '+str(last_x), 'Last Y: '+str(last_y))
    for wait in range(seconds_to_check):
        time.sleep(1)
        x = getMousePosition()['x']
        y = getMousePosition()['y']
        if debug:
            print('X: '+str(x),'Y: '+str(y))

    if x in range(last_x-10,last_x+10) and y in range(last_y-10,last_y+10):#If user in afk
        return True
    else:
        return False

print(ifAfk(5,True))