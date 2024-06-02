#!/usr/bin/env python3

##
## EPITECH PROJECT, 2024
## Worshop-IA-Python
## File description:
## train_model
##

import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split

data_set = pd.read_csv("data_set/cancer.csv")
x = data_set.drop(columns=["diagnosis(1=m, 0=b)"])
y = data_set["diagnosis(1=m, 0=b)"]

x_train, x_test, y_train, y_test = train_test_split(x, y , test_size=0.2)

model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Dense(256, input_shape = (x_train.shape[1],), activation="sigmoid"))
model.add(tf.keras.layers.Dense(256, activation="sigmoid"))
model.add(tf.keras.layers.Dense(1, activation="sigmoid"))
model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])

model.fit(x_train, y_train, epochs=100)

model.save("model.h5")
np.savez("test_data.npz", x_test=x_test, y_test=y_test)
