#!/usr/bin/env python3

##
## EPITECH PROJECT, 2024
## Worshop-IA-Python
## File description:
## test_model
##

import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

model = tf.keras.models.load_model("model.h5")
test_data = np.load("test_data.npz")
x_test = test_data['x_test']
y_test = test_data['y_test']

model.evaluate(x_test, y_test)

predictions = model.predict(x_test)

plt.figure(figsize=(10, 6))
plt.plot(y_test, color='blue', label='Actual values')
plt.plot(predictions, color='red', label='Predicted values')
plt.title('Actual vs Predicted Values')
plt.xlabel('Test Data Index')
plt.ylabel('Target Value')
plt.legend()
plt.show()
