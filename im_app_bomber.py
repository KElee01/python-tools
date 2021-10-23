from pykeyboard.mac import PyKeyboard
import time

# Initiation
keyboard = PyKeyboard()

# Wait for manually focusing
time.sleep(3)
a = 0
for a in range(0,100): # Number of messages
    keyboard.type_string("?") # Content of the messages
    a += 1
    keyboard.tap_key("RETURN")
print("finish")