import numpy as np
import tensorflow.keras as kr
import pandas as pd

df = pd.read_csv("powerproduction.csv")
x = np.array(df["speed"])
y = np.array(df["power"])

class linear_model:

    def train(self):
        self.model.add(kr.layers.Dense(1, input_shape=(1,), activation="linear", kernel_initializer='ones', bias_initializer='zeros'))
        self.model.compile('adam', loss='mean_squared_error')
        # Train the neural network on our training data.
        self.model.fit(x, y, epochs=500)

    def __init__(self, speed, power):
        self.model = kr.models.Sequential()
        self.x = speed
        self.y = power
    
    def predict(self, val):
        prediction = self.model.predict([val])
        return prediction.item(0)

linmodel = linear_model(x, y)
linmodel.train()