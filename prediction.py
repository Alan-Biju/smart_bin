import os
import tensorflow as tf
import numpy as np
from keras.preprocessing import image

def predict(img_path):
     print(img_path)
     labels={0: 'cardboard', 1: 'paper', 2: 'metal', 3: 'glass', 4: 'plastic', 5: 'trash'}


     img = image.load_img(img_path, target_size=(300, 300))
     img = image.img_to_array(img, dtype=np.uint8)
     img=np.array(img)/255.0
#plt.imshow(img.squeeze())
     
     model = tf.keras.models.load_model("./weights/weights_2000.h5")
     p=model.predict(img[np.newaxis, ...])
     pro=np.max(p[0], axis=-1)
     print("p.shape:",p.shape)
     print("prob",pro)
     predicted_class = labels[np.argmax(p[0], axis=-1)]
     # comment the below line to stop deletinf the image 
     #os.remove(img_path)
     #----------------------------------------------------------->>>>>>>>>>>>>>>>>>>
     print("classified label:",predicted_class)
     return(str(predicted_class) + " "+str(pro))
#print(predict(img_path = 'C:\\Users\\--\\Downloads\\dataset-original\\dataset-original\\metal\\metal1.jpg'))
