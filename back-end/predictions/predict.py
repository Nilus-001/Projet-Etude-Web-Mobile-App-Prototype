import pandas as pd
import torch
import torch.nn as nn
from math import ceil

CONTEXT_WINDOW = 288
PREDICT_HOURS = 24

HUM_SAVE_PATH = "ai_models/humidity_model.pt"
TEMP_SAVE_PATH = "ai_models/temp_model.pt"

temp_history = []
predicted_temps = []
humidity_history = []
predicted_humidity = []

current = 0

weights_humidity = torch.load(HUM_SAVE_PATH, weights_only=True)# loads model
weights_temp = torch.load(TEMP_SAVE_PATH, weights_only=True) # loads model


# Define the model
model_humidity = nn.Sequential(
    nn.Linear(CONTEXT_WINDOW * 2 + 1, 384),
    nn.ReLU(),
    nn.Linear(384, 192),
    nn.ReLU(),
    nn.Linear(192, 96),
    nn.ReLU(),
    nn.Linear(96, 48),
    nn.ReLU(),
    nn.Linear(48, 24),
    nn.ReLU(),
    nn.Linear(24, 12),
    nn.ReLU(),
    nn.Linear(12, 6),
    nn.ReLU(),
    nn.Linear(6, 1)
)

model_temp = nn.Sequential(
    nn.Linear(CONTEXT_WINDOW * 2 + 1, 384),
    nn.ReLU(),
    nn.Linear(384, 192),
    nn.ReLU(),
    nn.Linear(192, 96),
    nn.ReLU(),
    nn.Linear(96, 48),
    nn.ReLU(),
    nn.Linear(48, 24),
    nn.ReLU(),
    nn.Linear(24, 12),
    nn.ReLU(),
    nn.Linear(12, 6),
    nn.ReLU(),
    nn.Linear(6, 1)
)



model_humidity.load_state_dict(weights_humidity)
model_temp.load_state_dict(weights_temp)
model_humidity.eval()
model_temp.eval()

data = pd.read_csv("data/sensors.csv", sep=",")
data["timestamp"] = pd.to_datetime(data["timestamp"]).astype(int) / 10**9 % 31536


for i in range(CONTEXT_WINDOW):
    temp_history.append(data["temperature_c"][i])
    humidity_history.append(data["humidity_pct"][i])

for i in range(PREDICT_HOURS):
    temp = temp_history[current:current + CONTEXT_WINDOW]
    humidity = humidity_history[current:current + CONTEXT_WINDOW]
    inputs = []
    for i in range(CONTEXT_WINDOW):
        inputs.append(temp[i])
        inputs.append(humidity[i])
    inputs.append((data["timestamp"][CONTEXT_WINDOW] + current * 3.6) % 31536)
    X = torch.tensor(inputs, dtype=torch.float32)
    y_pred_hum = model_humidity(X)
    y_pred_temp = model_temp(X)
    res_temp = ceil(float(y_pred_temp[0]))
    res_hum = ceil(float(y_pred_hum[0]))
    humidity_history.append(res_hum)
    temp_history.append(res_temp)
    predicted_humidity.append(res_hum)
    predicted_temps.append(res_temp)
    current += 1