from cv2 import *
def capturePic():
    cam_port = 0
    cam = VideoCapture(cam_port)
    result, image = cam.read()
    if result:  
        imshow("Alan Biju", image)  
        result=imwrite("./data/trashPic.png", image)
        # delay is to show the pic in the screen for refernce purpose remove it maga when added to rasPI os
        waitKey(delay=1500)
        #in mili Seconds
        destroyWindow("Alan Biju")
        return True
    else:
        print("No image detected. Please! try again")
        return False