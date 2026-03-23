import pandas as pd
import random
import time
from sklearn.ensemble import RandomForestClassifier

# Generate training data
data = []
for _ in range(200):
    temp = random.randint(20, 100)
    gas = random.randint(100, 500)
    speed = random.randint(0, 120)
    risk = 1 if temp > 70 or gas > 400 or speed > 100 else 0
    data.append([temp, gas, speed, risk])

df = pd.DataFrame(data, columns=["temp", "gas", "speed", "risk"])

# Train model
X = df[["temp", "gas", "speed"]]
y = df["risk"]

model = RandomForestClassifier()
model.fit(X, y)

print("AI Safety Model Trained")
print("Starting Real-Time Monitoring...")

while True:
    temp = random.randint(20, 100)
    gas = random.randint(100, 500)
    speed = random.randint(0, 120)

    prediction = model.predict([[temp, gas, speed]])[0]

    print(f"Temp: {temp} | Gas: {gas} | Speed: {speed}")

    if prediction == 1:
        print("ALERT: Risk Detected!\n")
    else:
        print("Safe\n")

    time.sleep(2)
