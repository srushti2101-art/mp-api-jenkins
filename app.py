from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello Srushti 🎉"}

@app.get("/predict")
def predict(value: int):
    return {"prediction": 0}