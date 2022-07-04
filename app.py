import joblib
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
from fastapi import FastAPI
import numpy as np
import joblib

app = FastAPI()

data = pd.read_csv('data/train.csv')

class scaler:
    def __init__(self, df):
        self.max = df.max()
        self.min = df.min()
        self.std = df.std()
    def minmax_scaler(self, x):
        return (x - self.min) / (self.max - self.min)
    def standard_scaler(self, x):
        return (x - self.min) / self.std

cols = list(data.columns[:-1])
all_scalers = {}

for c in cols:
    all_scalers[c] = scaler(data[c])

rf_model = joblib.load('model/rf_model.joblib')

def transformer(inp):
    output = {}
    for c in cols:
        output[c] = all_scalers[c].minmax_scaler(inp[c])
    return output

def make_prediction(model, inp):
    inp = [list(inp.values())]
    prediction = int(model.predict(inp))
    return prediction

@app.get('/predict')
def predict_item(battery_power : float = 0.0, blue : float = 0.0, clock_speed : float = 0.0, dual_sim : float = 0.0, 
                 fc : float = 0.0, four_g : float = 0.0, int_memory : float = 0.0, m_dep : float = 0.0, mobile_wt : float = 0.0, 
                 n_cores : float = 0.0, pc : float = 0.0, px_height : float = 0.0, px_width : float = 0.0, ram : float = 0.0, 
                 sc_h : float = 0.0, sc_w : float = 0.0, talk_time : float = 0.0, three_g : float = 0.0, 
                 touch_screen : float = 0.0, wifi : float = 0.0):
    inp = {}
    for c in cols:
        inp[c] = eval(c)
    model_used = str(rf_model)
    inp_transform = transformer(inp)
    prediction = make_prediction(rf_model, inp_transform)

    # return {'model':model_used, 'output':inp_dict, 'prediction':prediction}
    return {'cols': cols, 'values':inp, 'prediction':prediction}
