from prediction import *
from cam import *
from servo import *
from mongoDB import *

#here path of the image is given and passed to the predction function
trashPic=capturePic()
# trashPic=True
if trashPic:
    result=predict("./data/trashPic.jpg")
    Predication_result=result.split(" ")
    label=Predication_result[0]
    label_prob=int(float(Predication_result[1])*100)
    print(label_prob)
    if label in ['cardboard','paper'] and label_prob > 60:
        category = "Biodegradable"
        print(category)
        addTrash(category,label,"None",label_prob)
        # servoMotor(12.5)
    elif label in ['metal','glass','plastic','trash'] and label_prob > 60:
        category = "Non-Biodegradable"
        print(category)
        if label in ['glass','trash']:
            sub_category="Non-Recyclable"
            print(sub_category)
            # servoMotor(0.5)
            addTrash(category,label,sub_category,label_prob)
        else:
            sub_category="Recyclable"
            print(sub_category)
            # servoMotor(0.5)
            addTrash(category,label,sub_category,label_prob)

    else:
        category = "Categorizing Difficult"
        print(category) 
        # servoMotor(0.5)
        addTrash(category,label,"None",label_prob)

else:
    print("somthing went worng")    
