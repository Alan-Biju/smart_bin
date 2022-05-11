import cv2
def capturePic():
    cam_port = 0
    cam = cv2.VideoCapture(cam_port)
    result, image = cam.read()
    if result:  
        cv2.imshow("Alan Biju", image)  
        result=cv2.imwrite("./data/trashPic.jpg", image)
        # delay is to show the pic in the screen for refernce purpose remove it maga when added to rasPI os
        cv2.waitKey(delay=1500)
        #in mili Seconds
        cv2.destroyWindow("Alan Biju")
        return True
    else:
        print("No image detected. Please! try again")
        return False