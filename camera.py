import cv2
import time
import random


print(time.time())
print(random.randint(0,9))

def snapshot():
   
    vCO=cv2.VideoCapture(0,cv2.CAP_DSHOW)
    result=True
    while(result):
        
        ret,frame=vCO.read()
        cv2.imwrite("testpic.jpg",frame)

        result=False

    vCO.release()
    cv2.destroyAllWindows()

snapshot()

