from tqdm import tqdm
import shutil
from keras.preprocessing.image import ImageDataGenerator
import os
import numpy as np
from keras.applications.inception_v3 import InceptionV3
import pickle


maxlen = 192171
img_nums = {i:len(os.listdir('kaggle/iMaterialist/assets/train_224/'+ str(i) + '/')) for i in range(1,129)}
train_data_gen = ImageDataGenerator(rescale=1. / 255)
train_generator = train_data_gen.flow_from_directory(directory='kaggle/iMaterialist/assets/train_224/',
                                                     target_size=(224, 224),
                                                     batch_size=32,
                                                    class_mode='categorical', shuffle=False)

base_model = InceptionV3(weights='imagenet', include_top=False,input_shape=(224,224,3))

for b in tqdm(range(maxlen//32)):
    x = train_generator.next()
    z = base_model.predict_on_batch(x[0])
    with open('kaggle/iMaterialist/assets/bn_inception/' + str(b) + '.p','wb') as f:
        pickle.dump((z,x[1]),f)