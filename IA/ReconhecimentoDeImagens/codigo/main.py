from IPython.display import Image

import tensorflow as tf
print("Versão do TensorFlow:", tf.__version__)

import keras as k
print("Versão do Keras:", k.__version__)

#imports
from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense

classifier = Sequential()
classifier.add(Conv2D(32, (3, 3), input_shape = (64, 64, 3), activation = 'relu'))
classifier.add(MaxPooling2D(pool_size = (2,2)))
classifier.add(Conv2D(32, (3, 3), activation = 'relu'))
classifier.add(MaxPooling2D(pool_size = (2,2)))
classifier.add(Flatten())
classifier.add(Dense(units = 128, activation = 'relu'))
classifier.add(Dense(units = 1, activation = 'sigmoid'))
classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy',
metrics = ['accuracy'])
from keras.preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(rescale = 1./255, shear_range = 0.2, zoom_range = 0.2, horizontal_flip = True)

validation_datagen = ImageDataGenerator(rescale = 1./255)
training_set = train_datagen.flow_from_directory('./dataset_treino', target_size = (64, 64), batch_size = 32, class_mode = 'binary')

validation_set = validation_datagen.flow_from_directory('./dataset_validation', target_size = (64, 64), batch_size = 32, class_mode = 'binary')
classifier.fit_generator(training_set, steps_per_epoch = 4000, epochs = 5, validation_data = validation_set, validation_steps = 1000)