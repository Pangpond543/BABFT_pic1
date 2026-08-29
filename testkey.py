import keyboard
import time

# ปุ่มแทนแต่ละบิต
BIT_KEYS = ["b", "v", "c", "x", "z"]
CLOCK_KEY = "h"

print("เริ่มในอีก 3 วินาที...")
time.sleep(3)

for j in range(32):
    for color in range(32):
        
        if keyboard.is_pressed("f5"):
            print("หยุดการทดสอบ")
            break

        # แยกเป็น 5 บิต
        bit0 = (color >> 0) & 1
        bit1 = (color >> 1) & 1
        bit2 = (color >> 2) & 1
        bit3 = (color >> 3) & 1
        bit4 = (color >> 4) & 1

        bits = [bit0, bit1, bit2, bit3, bit4]

        # ตั้งค่าบิต
        for i in range(5):
            if bits[i]:
                keyboard.press(BIT_KEYS[i])
            else:
                keyboard.release(BIT_KEYS[i])
        
        # รอให้ข้อมูลนิ่ง
        time.sleep(0.5)
        

        # Clock
        keyboard.press(CLOCK_KEY)
        time.sleep(0.05)
        keyboard.release(CLOCK_KEY)
        
        time.sleep(0.7)
        
        # ปล่อยบิตทั้งหมด
        for key in BIT_KEYS:
            keyboard.release(key)

        # เวลาระหว่าง Pixel
        time.sleep(0.1)

print("เสร็จแล้ว")