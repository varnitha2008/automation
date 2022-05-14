
import cv2
import time
import random

import dropbox


print(time.time())
print(random.randint(0,9))

startTime=time.time

def snapshot():
    random=random.randint(0,100)
  
    vCO=cv2.VideoCapture(0,cv2.CAP_DSHOW)
    result=True
    while(result):
      
        ret,frame=vCO.read()
        imgName="testpic"+str(random)+".png"
        cv2.imwrite(imgName,frame)
        startTime=time.time

        result=False
       
    return imgName
    vCO.release()
    cv2.destroyAllWindows()

snapshot()



def uploadFile(imageName):
        accesstoken= "sl.BHGOnA9Mdvpi5gPP7mzZrE_Kty2IC_HYkPzPnykp5Q99D8pKhdlIrQYcxn7vXFqi10Pnd-DgwbA8Uri5frG1HIhkGuqrgEPX66Q0AQEXsv6Z2L9QhV1yReMt9QDZDZlk4YS8_AI"
        file=imageName
        file_to=imageName
        dbx =dropbox.Dropbox(accesstoken)
        f=open(file,"rb")
        dbx.files_upload(f.read(),file)


def main():
    while(True):
        
        if ((time.time()-startTime>=1)):
            name=snapshot()
            uploadFile(name)
main()            