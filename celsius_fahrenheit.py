# -*- coding: utf-8 -*-
"""celsius_fahrenheit.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YAxdoX7P-B4QdjdMQ-E5iGJ9ZaHPKBON
"""

# import os 
# os.environ['TF_CPP_MIN_LOG_LEVEL'] = 2
# нет необходимотси качать CUDA для GPU

import numpy as np 
import matplotlib.pyplot as plt 
from tensorflow import keras
from tensorflow.keras.layers import Dense

"""перевод градусов цельсия в грудсы фаренгейта

F = C * 1.8 + 32
"""

celsius = np.array([-40, -10, 0, 8, 15, 22, 38])
fahrenheit = np.array([-40, 14, 32, 46, 59, 72, 100])

model = keras.Sequential()
model.add(Dense(units = 1, input_shape = (1,), activation = 'linear'))

model.compile(loss = 'mean_squared_error', optimizer = keras.optimizers.Adam(0.1))

history = model.fit(celsius, fahrenheit, epochs = 700, verbose = False)

plt.plot(history.history['loss'])
plt.grid(True)
plt.show()

print(model.weights)

test =[100, 300, 28, 43, 0, 10]

for temp in test: 
  print(temp, model.predict([temp]))