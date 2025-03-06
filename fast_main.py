import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
import pickle

class bank_node(BaseModel):
    variance:float
    skewness:float
    curtosis:float
    entropy:float

app = FastAPI()
pickle_in = open("bank_note_classifier.pkl", "rb")
classifier = pickle.load(pickle_in)

@app.post("/predict")
def predict_note(data: bank_node):
    data = data.dict()
    variance = data['variance']
    skewness = data['skewness']
    curtosis = data['curtosis']
    entropy = data['entropy']
    print(classifier.predict([[variance, skewness, curtosis, entropy]]))

