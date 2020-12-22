import os
import glob
import keras
import numpy as np
import pandas as pd
from keras.models import *
from keras.layers import *
from keras.losses import *
from keras.optimizers import *
from keras.callbacks import ModelCheckpoint


def load_data(dir_path=None):
    # x_train, y_train = 
    # x_test, y_test = 
    pass


def build_model():
    # input shape, not sure now
    x, y, z = (64, 48, 3)

    model = Sequential()
    model.add(InputLayer(input_shape=(None, x, y, z)))
    model.add(TimeDistributed(Conv2D(32, (3, 3), activation="relu")))
    model.add(TimeDistributed(MaxPool2D()))
    model.add(TimeDistributed(Conv2D(64, (3, 3), activation="relu")))
    model.add(TimeDistributed(MaxPool2D()))
    model.add(TimeDistributed(Flatten()))
    model.add(TimeDistributed(Dense(32, activation="relu")))

    ## sth here

    model.add(TimeDistributed(Activation("sigmoid")))

    model.summary()
    model.compile(
        optimizer=Adam(),
        loss=SparseCategoricalCrossentropy(),
    )
    return model


def train_model(model, batch_size, epochs):

    checkpoint = ModelCheckpoint(
        "best_model.hdf5",
        monitor='loss',
        verbose=1,
        save_best_only=True,
        mode='auto',
        period=1
    )

    model.fit(
        x_train,
        y_train,
        batch_size=batch_size,
        epochs=epochs,
        verbose=1,
        validation_data=(x_test, y_test),
        callbacks=[checkpoint]
    )


if __name__ == "__main__":
    model = build_model()
