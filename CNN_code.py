
#CNN code
model = Sequential()
model.add(Conv2D(32,3,padding="same", activation="relu", input_shape=(224,224,1)))
model.add(MaxPool2D())

model.add(Conv2D(32, 3, padding="same", activation="relu"))
model.add(MaxPool2D())

model.add(Conv2D(64, 3, padding="same", activation="relu"))
model.add(MaxPool2D())
model.add(Dropout(0.4))

model.add(Flatten())
model.add(Dense(128,activation="relu"))
model.add(Dense(2, activation="softmax"))


#model.summary()

#opt = Adam(learning_rate=0.000001)
opt = Adam(learning_rate=0.001)
model.compile(optimizer = opt , loss = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True) , metrics = ['accuracy','mae'])
epochsNum=15
