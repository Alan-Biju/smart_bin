from prediction import *
from cam import *
#here path of the image is given and passed to the predction function
trashPic=capturePic()
if trashPic:
    result=predict("./data/trashPic.png")
    print(result)
else:
    print("somthing went worng")    