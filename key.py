import keyboard
import time

time.sleep(3)
for i in range(0, 32, 1):
        keyboard.press("h")
        keyboard.release("h")
        time.sleep(0.2)