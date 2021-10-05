# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 21:40:41 2020

@author: win10
"""

# 1. Library imports
import uvicorn
from fastapi import FastAPI
from models import YeildPrediction
import numpy as np
import pickle
import pandas as pd
# 2. Create the app object
app = FastAPI()
model = pickle.load(open("yield_prediction.pkcls", "rb"))
classifier=pickle.load(model)

# 3. Index route, opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
    return {'message': 'Hello, World'}

# 3. Expose the prediction functionality, make a prediction from the passed
#    JSON data and return the predicted Crop Yeild.
@app.post('/predict')
def predict_yeild(data:YeildPrediction):
    data = data.dict()
    state=data['state']
    local_gov=data['local_gov']
    crop=data['crop']
    area=data['area']
   # print(classifier.predict([[state,local_gov,crop,area]]))
    prediction = classifier.predict([[state,local_gov,crop,area]])
    if(prediction[0]>0.5):
        prediction=prediction[0]
    else:
        prediction="Something went wrong!"
    return {
        'prediction': prediction
    }

# 5. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
    
#uvicorn app:app --reload