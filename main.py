from prediction import *
from cam import *
from servo import *

#here path of the image is given and passed to the predction function
trashPic=capturePic()
# trashPic=True
if trashPic:
    result=predict("./data/trashPic.jpg")
    Predication_result=result.split(" ")
    label=Predication_result[0]
    label_prob=int(float(Predication_result[1])*100)
    print(label_prob)
    if label in ['cardboard','paper'] and label_prob > 80:
        category = "Biodegradable"
        print(category)
    elif label in ['metal','glass','plastic','trash'] and label_prob > 80:
        category = "Non-Biodegradable"
        print(category)
        if label in ['glass']:
            sub_category="Non-Recyclable"
            print(sub_category)
    else:
        category = "Categorizing Difficult"
        print(category) 
else:
    print("somthing went worng")    