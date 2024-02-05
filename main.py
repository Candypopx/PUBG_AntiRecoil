import time
import win32api
import keyboard

# only jitter while ads
state_left = win32api.GetKeyState(0x01)  # leftButton Up = 0 or 1; Down = -127 or -128
# print("left initial state = {0}".format(state_left))
state_right = win32api.GetKeyState(0x02)  # rightButton Up = 0 or 1; Down = -127 or -128
# print("left initial state = {0}".format(state_right))
# Set the toggle button
flat_toggle = '6'


# last state for toggle button
last_state_flat = False

# Set whether the anti-recoil is enabled by default
enabled_flat = False


# module session
# module for m416 anti recoil
# toggle button = "6"
def m416(s_left, s_right, x):
    if x != s_right:  # action ads
        recoilNum = 5 # CHANGE value at here
        while x < 0:
            a = win32api.GetKeyState(0x01)  # always check the state of left click
            if a != s_left:
                if a < 0:
                    win32api.mouse_event(0x01, 0, recoilNum)
                    time.sleep(0.001)

            x = win32api.GetKeyState(0x02)  # check right button state

    a = win32api.GetKeyState(0x01)
    if a != s_left:
        while a < 0:
            win32api.mouse_event(0x01, 0, 2)
            time.sleep(0.01)
            a = win32api.GetKeyState(0x01)  # Check button state

# main part
# print for startup
print("PUBG Anti-recoil script started!")

while True:
    b = win32api.GetKeyState(0x02)

    # check state changed for toggle button
    key_down_flat = keyboard.is_pressed(flat_toggle)

    # FLAT LINE running script
    if key_down_flat != last_state_flat:
        last_state_flat = key_down_flat
        if last_state_flat:
            enabled_flat = not enabled_flat
            if enabled_flat:
                print("Anti-recoil m416 ON")
            else:
                print("Anti-recoil m416 OFF")

    if enabled_flat:
        m416(state_left, state_right, b)

    time.sleep(0.001)




