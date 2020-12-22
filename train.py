import os
import glob
import numpy as np
import pandas as pd
import keras
from keras.models import *
from keras.layers import *
# from keras.losses import *
# from keras.optimizers import *
from keras.callbacks import ModelCheckpoint


def load_data(dir_path=None):
    a = np.load("AAL.npz")

    print(a['x'].shape)
    print(a['y'].shape)
    return a['x'], a['y']


def build_model(X, Y):
    # input shape, not sure now

    model = Sequential()

    model.add(TimeDistributed(Conv1D(16, 3, activation='relu'), batch_input_shape=(3, None, 4, 1)))
    model.add(TimeDistributed(MaxPool1D(pool_size=2)))
    # model.add(TimeDistributed(Conv1D(32, 3, activation='relu')))
    # model.add(TimeDistributed(MaxPool1D(pool_size=2)))
    model.add(TimeDistributed(Flatten()))

    model.add(LSTM(128, stateful=True, return_sequences=True))
    model.add(LSTM(32, stateful=True))
    model.add(Dense(1, activation="sigmoid"))


    # model.add(InputLayer(input_shape=(3, 10, 300)))

    # model.add(Conv2D(32, (1, 1), activation="relu", data_format="channels_first"))
    # model.add(MaxPool2D((2,2), data_format="channels_first"))
    # model.add(Conv2D(64, (1, 1), activation="relu", data_format="channels_first"))
    # model.add(MaxPool2D((2,2), data_format="channels_first"))
    # # model.add(Conv2D(128, (3, 3), activation="relu", data_format="channels_first"))
    # # model.add(MaxPool2D((2,2), data_format="channels_first"))
    # model.add(Flatten())
    # # model.add(Dense(512, activation="relu"))
    # model.add(LSTM(128, activation="relu", return_sequences=True))
    # model.add(LSTM(32, activation="relu"))
    # model.add(Dense(1, activation="sigmoid"))

    model.summary()
    model.compile(
        loss='binary_crossentropy',
        optimizer='rmsprop',
        metrics=['accuracy']
    )
    return model

    # regressor.compile(optimizer = 'adam', loss = 'mean_squared_error')
    # regressor.fit(X_train, y_train, epochs = 100, batch_size = 32)

    # # sth here

    # model.add(TimeDistributed(Dense(1)))

    # model.summary()
    # model.compile(
    #     loss='mse',
    #     optimizer='adam',
    #     metrics=['accuracy']
    # )
    # return model


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
        X,
        Y,
        batch_size=batch_size,
        epochs=epochs,
        verbose=1,
        # validation_data=(x_test, y_test),
        callbacks=[checkpoint]
    )


if __name__ == "__main__":
    X, Y = load_data()
    model = build_model(X, Y)
    
    train_model(model, 16, 100)

