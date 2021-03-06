#Netowrk-in-network model

from __future__ import print_function
from keras.datasets import cifar10
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Convolution2D, MaxPooling2D
from keras.optimizers import SGD
from keras.utils import np_utils
from keras.models import model_from_json
from keras import initializations
from keras.regularizers import l2, activity_l2

from keras.regularizers import WeightRegularizer, ActivityRegularizer 


from keras.models import Sequential, Model
from keras.layers import Flatten, Dense, Dropout, Reshape, Permute, Activation, \
    Input, merge
from keras.layers.convolutional import Convolution2D, MaxPooling2D, ZeroPadding2D
from keras.optimizers import SGD
import numpy as np
from scipy.misc import imread, imresize, imsave
from keras.preprocessing.image import ImageDataGenerator
import keras

from keras.layers.advanced_activations import LeakyReLU, PReLU, ParametricSoftplus


import h5py 
#from keras.applications.vgg16 import VGG16


def keras_eg_nodrop():
    model = Sequential()

    model.add(Convolution2D(32, 3, 3, border_mode='same',
                                input_shape=(32,32,3)))
    model.add(Activation('relu'))
    model.add(Convolution2D(32, 3, 3))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Convolution2D(64, 3, 3, border_mode='same'))
    model.add(Activation('relu'))
    model.add(Convolution2D(64, 3, 3))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Flatten())
    model.add(Dense(512))
    model.add(Activation('relu'))
    model.add(Dense(10))
    model.add(Activation('softmax'))

    return model

def keras_eg_ipdrop():
    model = Sequential()

    model.add(Convolution2D(32, 3, 3, border_mode='same',
                                input_shape=(32,32,3)))
    model.add(Activation('relu'))
    model.add(Convolution2D(32, 3, 3))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Convolution2D(64, 3, 3, border_mode='same'))
    model.add(Activation('relu'))
    model.add(Convolution2D(64, 3, 3))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Flatten())
    model.add(Dense(512))
    model.add(Activation('relu'))
    model.add(Dropout(0.5))
    model.add(Dense(10))
    model.add(Activation('softmax'))

    return model

def keras_eg_alldrop():
    model = Sequential()

    model.add(Convolution2D(32, 3, 3, border_mode='same',
                                input_shape=(32,32,3)))
    model.add(Activation('relu'))
    model.add(Convolution2D(32, 3, 3))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))

    model.add(Convolution2D(64, 3, 3, border_mode='same'))
    model.add(Activation('relu'))
    model.add(Convolution2D(64, 3, 3))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))

    model.add(Flatten())
    model.add(Dense(512))
    model.add(Activation('relu'))
    model.add(Dropout(0.5))
    model.add(Dense(10))
    model.add(Activation('softmax'))

    return model

def small_lenet_nodrop():
    model = Sequential()

    model.add(Convolution2D(32, 3, 3, border_mode='same',
                            input_shape=(32,32,3)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    
    model.add(Convolution2D(64, 3, 3, border_mode='same'))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    
    model.add(Flatten())
    model.add(Dense(500))
    model.add(Activation('relu'))
    model.add(Dense(10))
    model.add(Activation('softmax'))
   
    return model

def small_lenet_alldrop():
    model = Sequential()

    model.add(Convolution2D(32, 3, 3, border_mode='same',
                            input_shape=(32,32,3)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.5))
    
    model.add(Convolution2D(64, 3, 3, border_mode='same'))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.5))
    
    model.add(Flatten())
    model.add(Dense(500))
    model.add(Activation('relu'))
    model.add(Dropout(0.5))
    model.add(Dense(10))
    model.add(Activation('softmax'))
   
    return model

def small_lenet_ipdrop():
    model = Sequential()

    model.add(Convolution2D(32, 3, 3, border_mode='same',
                            input_shape=(32,32,3)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    
    model.add(Convolution2D(64, 3, 3, border_mode='same'))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    
    model.add(Flatten())
    model.add(Dense(500))
    model.add(Activation('relu'))
    model.add(Dropout(0.5))
    model.add(Dense(10))
    model.add(Activation('softmax'))
   
    return model

def cifar_ipython():
    model = Sequential()

    model.add(Convolution2D(32, 3, 3,border_mode = 'same',
                            input_shape=(32,32,3)))
    model.add(LeakyReLU(alpha=0.2))
    model.add(Convolution2D(32, 3, 3))
    model.add(LeakyReLU(alpha=0.2))
    model.add(MaxPooling2D(pool_size=(2,2)))
    model.add(Dropout(0.2))

    model.add(Convolution2D(64, 3,3,border_mode = 'same' ))
    model.add(LeakyReLU(alpha=0.2))
    model.add(Convolution2D(64, 3, 3))
    model.add(LeakyReLU(alpha=0.2))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.3))

    model.add(Convolution2D(128, 3, 3, border_mode = 'same'))
    model.add(LeakyReLU(alpha=0.2))
    model.add(Convolution2D(128, 3, 3))
    model.add(LeakyReLU(alpha=0.2))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.4))

    model.add(Flatten())
    model.add(Dense(512))
    model.add(Activation('relu'))
    model.add(Dropout(0.5))

    model.add(Dense(10))
    model.add(Activation('softmax'))

    return model

def lenet_norelu_nodrop():
   
    model = Sequential()

    model.add(Convolution2D(192, 5, 5, border_mode='same',
                            input_shape=(32,32,3)))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    
    model.add(Convolution2D(192, 5, 5, border_mode='same'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    
    model.add(Flatten())
    model.add(Dense(1000))
    model.add(Activation('relu'))
    model.add(Dense(10))
    model.add(Activation('softmax'))
   
    return model


def lenet_norelu_ipdrop():

    model = Sequential()

    model.add(Convolution2D(192, 5, 5, border_mode='same',
                            input_shape=(32,32,3)))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    
    model.add(Convolution2D(192, 5, 5, border_mode='same'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    
    model.add(Flatten())
    model.add(Dense(1000))
    model.add(Activation('relu'))
    model.add(Dropout(0.5))
    model.add(Dense(10))
    model.add(Activation('softmax'))
   
    return model

def lenet_norelu_alldrop():
    model = Sequential()

    model.add(Convolution2D(192, 5, 5, border_mode='same',
                            input_shape=(32,32,3)))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.5))
    
    model.add(Convolution2D(192, 5, 5, border_mode='same'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.5))
    
    model.add(Flatten())
    model.add(Dense(1000))
    model.add(Activation('relu'))
    model.add(Dropout(0.5))
    model.add(Dense(10))
    model.add(Activation('softmax'))
   
    return model

def lenet_nodrop():
   
    model = Sequential()

    model.add(Convolution2D(192, 5, 5, border_mode='same',
                            input_shape=(32,32,3)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    
    model.add(Convolution2D(192, 5, 5, border_mode='same'))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    
    model.add(Flatten())
    model.add(Dense(1000))
    model.add(Activation('relu'))
    model.add(Dense(10))
    model.add(Activation('softmax'))
   
    return model


def lenet_ipdrop():

    model = Sequential()

    model.add(Convolution2D(192, 5, 5, border_mode='same',
                            input_shape=(32,32,3)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    
    model.add(Convolution2D(192, 5, 5, border_mode='same'))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    
    model.add(Flatten())
    model.add(Dense(1000))
    model.add(Activation('relu'))
    model.add(Dropout(0.5))
    model.add(Dense(10))
    model.add(Activation('softmax'))
   
    return model

def lenet_alldrop():
    model = Sequential()

    model.add(Convolution2D(192, 5, 5, border_mode='same',
                            input_shape=(32,32,3)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.5))
    
    model.add(Convolution2D(192, 5, 5, border_mode='same'))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.5))
    
    model.add(Flatten())
    model.add(Dense(1000))
    model.add(Activation('relu'))
    model.add(Dropout(0.5))
    model.add(Dense(10))
    model.add(Activation('softmax'))
   
    return model

def vgg_like(weights=None):
    '''
    VGG like model with two convolution blocks and two dense layers
    no pretraining
    '''
    # Image dimensions ordering should follow the Theano convention
    if keras.backend.image_dim_ordering() != 'th':
        keras.backend.set_image_dim_ordering('th')

    model = Sequential()
    # input: 64x64 images with 3 channels -> (3, 64, 64) tensors.
    # this applies 32 convolution filters of size 3x3 each.
    model.add(Convolution2D(64, 3, 3, border_mode='valid', input_shape=(3,64,64)))
    model.add(Activation('relu'))
    model.add(Convolution2D(64, 3, 3))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    #model.add(Dropout(0.25))

    model.add(Convolution2D(64, 3, 3, border_mode='valid'))
    model.add(Activation('relu'))
    model.add(Convolution2D(64, 3, 3))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    #model.add(Dropout(0.50))

    model.add(Flatten())
    # Note: Keras does automatic shape inference.
    model.add(Dense(256,W_regularizer=WeightRegularizer(l1=1e-6,l2=1e-6)))
    model.add(Activation('relu'))
    #model.add(Dropout(0.50))

    model.add(Dense(200,W_regularizer=WeightRegularizer(l1=1e-5,l2=1e-5)))
    model.add(Activation('softmax'))
    if weights!=None: 
        model.load_weights(weights) 
    return model 


def VGG_16add_pretrain():

    '''
    VGG_16 model with pre-trained weights for all convolutional blocks
    Only two dense layers as opposed to the conventional 3
    '''
    
    # Image dimensions ordering should follow the Theano convention
    if keras.backend.image_dim_ordering() != 'th':
        keras.backend.set_image_dim_ordering('th')


    # build the VGG16 network
    model = Sequential()
    model.add(ZeroPadding2D((1, 1), input_shape=(3, 64, 64)))
    
    model.add(Convolution2D(64, 3, 3, activation='relu', name='conv1_1'))
    model.add(ZeroPadding2D((1, 1)))
    model.add(Convolution2D(64, 3, 3, activation='relu', name='conv1_2'))
    model.add(MaxPooling2D((2, 2), strides=(2, 2)))
    
    model.add(ZeroPadding2D((1, 1)))
    model.add(Convolution2D(128, 3, 3, activation='relu', name='conv2_1'))
    model.add(ZeroPadding2D((1, 1)))
    model.add(Convolution2D(128, 3, 3, activation='relu', name='conv2_2'))
    model.add(MaxPooling2D((2, 2), strides=(2, 2)))

    model.add(ZeroPadding2D((1, 1)))
    model.add(Convolution2D(256, 3, 3, activation='relu', name='conv3_1'))
    model.add(ZeroPadding2D((1, 1)))
    model.add(Convolution2D(256, 3, 3, activation='relu', name='conv3_2'))
    model.add(ZeroPadding2D((1, 1)))
    model.add(Convolution2D(256, 3, 3, activation='relu', name='conv3_3'))
    model.add(MaxPooling2D((2, 2), strides=(2, 2)))
    
    model.add(ZeroPadding2D((1, 1)))
    model.add(Convolution2D(512, 3, 3, activation='relu', name='conv4_1'))
    model.add(ZeroPadding2D((1, 1)))
    model.add(Convolution2D(512, 3, 3, activation='relu', name='conv4_2'))
    model.add(ZeroPadding2D((1, 1)))
    model.add(Convolution2D(512, 3, 3, activation='relu', name='conv4_3'))
    model.add(MaxPooling2D((2, 2), strides=(2, 2)))
    
    model.add(ZeroPadding2D((1, 1)))
    model.add(Convolution2D(512, 3, 3, activation='relu', name='conv5_1'))
    model.add(ZeroPadding2D((1, 1)))
    model.add(Convolution2D(512, 3, 3, activation='relu', name='conv5_2'))
    model.add(ZeroPadding2D((1, 1)))
    model.add(Convolution2D(512, 3, 3, activation='relu', name='conv5_3'))
    model.add(MaxPooling2D((2, 2), strides=(2, 2)))
    
    # load the weights of the VGG16 networks
    # (trained on ImageNet, won the ILSVRC competition in 2014)
    # note: when there is a complete match between your model definition
    # and your weight savefile, you can simply call model.load_weights(filename)
    #assert os.path.exists(weights_path), 'Model weights not found (see "weights_path" variable in script).'
    f = h5py.File('models/samples/vgg16_weights.h5')
    for k in range(f.attrs['nb_layers']):
        if k >= len(model.layers):
            # we don't look at the last (fully-connected) layers in the savefile
            break
        g = f['layer_{}'.format(k)]
        weights = [g['param_{}'.format(p)] for p in range(g.attrs['nb_params'])]
        model.layers[k].set_weights(weights)
    f.close()
    print('Model loaded.')
    
    # build a classifier model to put on top of the convolutional model
    top_model = Sequential()
    top_model.add(Flatten(input_shape=model.output_shape[1:]))
    top_model.add(Dense(512, activation='relu'))
    top_model.add(Dropout(0.5))
    top_model.add(Dense(200, activation='softmax'))


    # set the first 25 layers (up to the last conv block)
    # to non-trainable (weights will not be updated)
    for layer in model.layers[:25]:

        layer.trainable = False

    return model



def VGG16_keras():

    '''
    VGG_16 model with pre-trained weights for all convolutional blocks
    (using VGG16 from keras.applications.vgg16) 
    '''
    import sys
    sys.path.append("/dccstor/dlw/ambrish/examples/deep-learning-models/")
    from vgg16 import VGG16
    base_model = VGG16(weights="imagenet")
    initial_model = Model(input=base_model.input, output=base_model.get_layer('fc2').output)
    last = initial_model.output
    for layer in initial_model.layers:
        layer.trainable = False
    #x = Flatten()(last)
    #x = Dense(1024, activation='relu', name = 'fc1')(x)
    #x = Dropout(0.5)(x)
    #x = Dense(1024, activation='relu', name = 'fc2')(x)
    x = Dropout(0.5)(last)
    x = Dense(200, activation='softmax', name = 'predictions')(x)

    model = Model(initial_model.input, x)

    return model



def VGG_16_like():
    '''
    Fully trainable VGG19 model
    '''

    model = Sequential()

    model.add(ZeroPadding2D((1,1),input_shape=(64,64,3)))
    model.add(Convolution2D(64, 3, 3, activation='relu', name='conv1_1'))
    model.add(ZeroPadding2D((1,1)))
    model.add(Convolution2D(64, 3, 3, activation='relu', name='conv1_2'))
    model.add(MaxPooling2D((2,2), strides=(2,2)))
    model.add(Dropout(0.5))

    model.add(ZeroPadding2D((1,1)))
    model.add(Convolution2D(128, 3, 3, activation='relu', name='conv2_1'))
    model.add(ZeroPadding2D((1,1)))
    model.add(Convolution2D(128, 3, 3, activation='relu', name='conv2_2'))
    model.add(MaxPooling2D((2,2), strides=(2,2)))
    model.add(Dropout(0.5))

    model.add(Flatten())
    model.add(Dense(512, activation='relu', name='dense_2'))
    model.add(Dropout(0.5))
    model.add(Dense(200, name='dense_3'))
    model.add(Activation("softmax"))

    return model

def VGG_16():
    '''
    Fully trainable VGG19 model
    '''

    model = Sequential()

    model.add(ZeroPadding2D((1,1),input_shape=(64,64,3)))
    model.add(Convolution2D(64, 3, 3, activation='relu', name='conv1_1'))
    model.add(ZeroPadding2D((1,1)))
    model.add(Convolution2D(64, 3, 3, activation='relu', name='conv1_2'))
    model.add(MaxPooling2D((2,2), strides=(2,2)))

    model.add(ZeroPadding2D((1,1)))
    model.add(Convolution2D(128, 3, 3, activation='relu', name='conv2_1'))
    model.add(ZeroPadding2D((1,1)))
    model.add(Convolution2D(128, 3, 3, activation='relu', name='conv2_2'))
    model.add(MaxPooling2D((2,2), strides=(2,2)))

    model.add(ZeroPadding2D((1,1)))
    model.add(Convolution2D(256, 3, 3, activation='relu', name='conv3_1'))
    model.add(ZeroPadding2D((1,1)))
    model.add(Convolution2D(256, 3, 3, activation='relu', name='conv3_2'))
    model.add(ZeroPadding2D((1,1)))
    model.add(Convolution2D(256, 3, 3, activation='relu', name='conv3_3'))
    model.add(ZeroPadding2D((1,1)))
    model.add(Convolution2D(256, 3, 3, activation='relu', name='conv3_4'))
    model.add(MaxPooling2D((2,2), strides=(2,2)))

    model.add(ZeroPadding2D((1,1)))
    model.add(Convolution2D(512, 3, 3, activation='relu', name='conv4_1'))
    model.add(ZeroPadding2D((1,1)))
    model.add(Convolution2D(512, 3, 3, activation='relu', name='conv4_2'))
    model.add(ZeroPadding2D((1,1)))
    model.add(Convolution2D(512, 3, 3, activation='relu', name='conv4_3'))
    model.add(ZeroPadding2D((1,1)))
    model.add(Convolution2D(512, 3, 3, activation='relu', name='conv4_4'))
    model.add(MaxPooling2D((2,2), strides=(2,2)))

    model.add(Flatten())
    model.add(Dense(512, activation='relu', name='dense_2'))
    model.add(Dropout(0.5))
    model.add(Dense(200, name='dense_3'))
    model.add(Activation("softmax"))

    return model

