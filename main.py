from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()

# ✅ Define Input Schema
class TextRequest(BaseModel):
    text: str

@app.get("/")
def read_root():
    return {"message": f"Hows life ?"}  # Dummy response for testing

@app.get("/predict")
def read_root():
    return {"message": f"Make it post dear..."} 

@app.post("/predict")
def predict_intent_and_entities(request: TextRequest):
    text = request.text  # Extract text correctly from JSON request
    return {"message": f"You entered: {text}"}  # Dummy response for testing
