#Numpy for numerical operations
import numpy as np
#Keras from tensorflow for neural networks
import tensorflow.keras as kr
#Pandas for dataframes
import pandas as pd

#import and clean the dataset, removing unwanted zero records.
df = pd.read_csv("powerproduction.csv")
#Remove the unreasonable power values
zeroVals = df[(df["speed"] > 10) & (df["power"] == 0)].index
df.drop(zeroVals, inplace=True)
#Assinging z & y to speed & power
x = np.array(df["speed"])
y = np.array(df["power"])

#Linear regression model class.
class linear_model:

    #__init__ function creates model and adds appropriate layers.
    def __init__(self, speed, power):
        self.model = kr.models.Sequential()
        self.model.add(kr.layers.Dense(1, input_shape=(1,), activation="linear", kernel_initializer='ones', bias_initializer='zeros'))
        self.model.compile('adam', loss='mean_squared_error')
        self.x = speed
        self.y = power
    
    #fitting the model over 1500 epochs
    def train(self):
        # Train the neural network on our dataset.
        self.model.fit(x, y, epochs=1500)

    #returns the single predicted value
    def predict(self, val):
        prediction = self.model.predict([val])
        return prediction.item(0)

#Polynomial regression model class.
class polynomial_model:

    #__init__ function creates model and adds appropriate layers.
    def __init__(self, speed, power):
        self.model = kr.models.Sequential()
        self.model.add(kr.layers.Dense(30, input_shape=(1,), activation='sigmoid'))
        self.model.add(kr.layers.Dense(1, activation='linear'))
        self.model.compile(kr.optimizers.Adam(lr=0.001), loss='mean_squared_error')
        self.x = speed
        self.y = power
    
    #fitting the model over 300 epochs
    def train(self):
        # Train the neural network on our dataset.
        self.model.fit(x, y, epochs=300, batch_size=5)

    #returns the single predicted value
    def predict(self, val):
        prediction = self.model.predict([val])
        return prediction.item(0)



#Create instances of each of the classes, passing them x & y.
linmodel = linear_model(x, y)
polymodel = polynomial_model(x, y)