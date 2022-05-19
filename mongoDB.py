from pymongo import MongoClient
import datetime
from bson.binary import Binary
client = MongoClient("mongodb+srv://Alan:asdfghjkl238@cluster0.asu1c.mongodb.net/?retryWrites=true&w=majority")

print("*******")
# print(Binary("/data/bottle.jpg"))
print("*******")
def addTrash(type,label,sub_label,prob):
    db = client.get_database('smartBin')
    data_colection = db.waste_Data
    new_waste_Details = {
        'type': type,
        'label':label ,
        "sub_label":sub_label,
        'date': datetime.datetime.now().strftime("%x"),
        "time":datetime.datetime.now().strftime("%X"),
        "prob":prob,
        }
    print(data_colection.insert_one(new_waste_Details))
  