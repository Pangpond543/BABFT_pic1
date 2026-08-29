import cv2
import keyboard
import time
import numpy as np

cap = cv2.VideoCapture(3)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 360)

countdown = False
pic = False
cam = True

if not cap.isOpened():
    print("ไม่สามารถเปิดกล้องได้")
    exit()

print("F6เพื่อถ่ายรูป")

while True:
    ret, frame = cap.read()
    crop = frame[0:360, 140:500]
   
    if not ret:
        break
    
    if keyboard.is_pressed("f6") and not countdown:
        print("นับถอยหลัง3วิ")
        countdown = True
        start_time = time.time()
        
    if countdown:
        elapsed = time.time() - start_time
        count = 3 - int(elapsed)
        if count > 0:
            cv2.putText(
                frame,
                str(count),
                (250,200),
                cv2.FONT_HERSHEY_SIMPLEX,
                4,
                (255, 255, 255),
                5
            )
        
        if elapsed >= 3:
            cv2.imwrite("image.png", crop)
            print("บันทึก image.png แล้ว")
            countdown = False
            pic = True
            
    if cam:
        cv2.imshow("Camera", frame)  
    
    if pic:
        img = cv2.imread("image.png")

        cv2.destroyWindow("Camera")   # ปิดกล้องก่อน
        cv2.imshow("Image", img)      # แสดงรูปที่ถ่าย
        cv2.waitKey(1)

        break                         # ออกจาก while

    if cv2.waitKey(1) == 27:
        break

small = cv2.resize(img, (32, 32), interpolation=cv2.INTER_AREA)

result = np.zeros_like(small)

stop = False

print("กด E เพื่อเริ่มส่งข้อมูล")

while True:
    cv2.waitKey(1)

    if keyboard.is_pressed("e"):
        while keyboard.is_pressed("e"):
            pass
        break

for y in range(32):
    if stop:
        break
    for x in range(32):
        b, g, r = small[y,x]
        R = int(r // 64)
        G = int(g // 64)
        B = int(b // 128)
        print(x,y,"=",R,G,B)
        
        R_n = R * 64 + 32
        G_n = G * 64 + 32
        B_n = B * 128 + 64
        
        result[y, x] = [R_n, G_n, B_n]
        
        color = (R << 3) | (G << 1) | B
        print(
            f"R={R} G={G} B={B} "
            f"-> Color={color} "
            f"-> Binary={format(color,'05b')}"
        )
        
        if keyboard.is_pressed("f5"):
            stop = True
            break

cv2.imwrite(
    "result.png",
    cv2.cvtColor(result, cv2.COLOR_RGB2BGR)
)
cap.release()
cv2.destroyAllWindows()