import cv2
import time
import serial

capture = cv2.VideoCapture(0)

#print(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
#capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
#capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
#print(capture.get(cv2.CAP_PROP_FRAME_WIDTH))

#height = 720,width = 1280

cv2.namedWindow("window", cv2.WINDOW_NORMAL)
cv2.resizeWindow('window', 720, 1280)
cv2.moveWindow('window', 360, 640)

mergin = 50
large_line_width =30
height = 720
width = 1280
height_center = int(height/2)
width_center = int(width/2)
reticle_width = 2


glay = (128, 128, 128)
bar_length = 90
hp_max = 10
now_hp = 10


start = time.time()


while(True):
    ret, frame = capture.read()
    cv2.circle(frame, (width_center, height_center), 5, (0,0,255), thickness=-1)
    if time.time() - start > 1.0:
        now_hp -= 1
        start = time.time()
    #verticle reticle
    cv2.rectangle(frame, (width_center - reticle_width, height_center - 100), (width_center + reticle_width, height_center - 20), color=(0,0,0), thickness=-1)
    cv2.rectangle(frame, (width_center - reticle_width, height_center + 20), (width_center + reticle_width, height_center + 100), color=(0,0,0), thickness=-1)

    #horizontal_reticle
    cv2.rectangle(frame, (width_center - 100, height_center - reticle_width), (width_center - 20, height_center + reticle_width), color=(0,0,0), thickness=-1)
    cv2.rectangle(frame, (width_center + 20, height_center - reticle_width), (width_center + 100, height_center + reticle_width), color=(0,0,0), thickness=-1)



    #set HP bar

    #upper hp
    if now_hp == hp_max:
        for i in range(5):
            cv2.rectangle(frame, (30 + 100 * i , height - 150), (30 + 100 * i + bar_length, height - 125), color=(128,128,128), thickness=-1)

    elif now_hp >=5:
        for i in range(now_hp % 5):
            cv2.rectangle(frame, (30 + 100 * i , height - 150), (30 + 100 * i + bar_length, height - 125), color=(128,128,128), thickness=-1)

    #lower_hp
    if now_hp >=5:
        for i in range(5):
            cv2.rectangle(frame, (30 + 100 * i , height - 100), (30 + 100 * i + bar_length, height - 75), color=(128,128,128), thickness=-1)

    elif now_hp == 0:
        while(True):
            ret, frame = capture.read()
            cv2.circle(frame, (width_center, height_center), 20, (255,0,255), thickness=-1)
            cv2.imshow('DEFEATED:(', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break


    else:
        for i in range(now_hp):
            cv2.rectangle(frame, (30 + 100 * i , height - 100), (30 + 100 * i + bar_length, height - 75), color=(128,128,128), thickness=-1)

    cv2.imshow('Team SATSUMA',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
