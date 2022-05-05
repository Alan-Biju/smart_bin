from prediction import *
from cam import *
from servo import *

#here path of the image is given and passed to the predction function
trashPic=capturePic()
if trashPic:
    result=predict("./data/paper2.jpg")
    print(result)
else:
    print("somthing went worng")    