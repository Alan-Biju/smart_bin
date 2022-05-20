import pyrebase
import datetime
# import uuid
Config = {
  "apiKey": "AIzaSyAaVk_H6o6FNqRpM17QP7dxyQjTIMyBnZs",
  "authDomain": "smartbin-423e2.firebaseapp.com",
  "projectId": "smartbin-423e2",
  "storageBucket": "smartbin-423e2.appspot.com",
  "messagingSenderId": "498270460224",
  "appId": "1:498270460224:web:0b3ab49d8ff2377aac02a5",
  "serviceAccount": "./_Files/FireStorekey.json",
  "databaseURL":"https://smartbin-423e2.appspot.com"
}
# unique_filename = str(uuid.uuid4())
# print(unique_filename)
def uploadImage(label):
  firebase = pyrebase.initialize_app(Config)
  storage = firebase.storage()
  my_image = "data/trashPic.jpg"
  path=str(datetime.datetime.now().strftime("%d"))+str(datetime.datetime.now().strftime("%b"))
  name=label+"-"+str(str(datetime.datetime.now().strftime("%X")))+".jpg"
  storage.child(path+'/'+name).put(my_image)
  return storage.child(path+'/'+name).get_url("/_Files/FireStorekey.json")
  




