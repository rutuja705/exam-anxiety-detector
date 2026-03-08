from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import BertTokenizer, BertForSequenceClassification

model_path = "exam_anxiety_model"

tokenizer = BertTokenizer.from_pretrained(model_path)
model = BertForSequenceClassification.from_pretrained(model_path)

try:
    tokenizer = BertTokenizer.from_pretrained("exam_anxiety_model")
    model = BertForSequenceClassification.from_pretrained("exam_anxiety_model")
except:
    tokenizer = None
    model = None
import torch

app = FastAPI(title="AI Based Exam Anxiety Detector")

# Load model and tokenizer
# Make sure the 'saved_model' directory is in the same folder as this main.py
MODEL_PATH = "exam_anxiety_model"

try:
    tokenizer = BertTokenizer.from_pretrained(MODEL_PATH)
    model = BertForSequenceClassification.from_pretrained(MODEL_PATH)
    model.eval()  # Set model to evaluation mode
except Exception as e:
    print(f"Warning: Model not found at {MODEL_PATH}. Make sure to place the trained model there.")
    tokenizer = None
    model = None

# Define label mapping
label_mapping = {0: "Low", 1: "Medium", 2: "High"}

# Request Schema
class TextInput(BaseModel):
    text: str

# Response Schema
class PredictionOutput(BaseModel):
    text: str
    anxiety_level: str
    confidence: float

@app.get("/")
def read_root():
    return {"message": "Welcome to the AI Based Exam Anxiety Detector API"}

@app.post("/predict", response_model=PredictionOutput)
def predict_anxiety(input_data: TextInput):
    if model is None or tokenizer is None:
        raise HTTPException(status_code=500, detail="Model not loaded. Please ensure the model is trained and saved in the correct directory.")
    
    text = input_data.text
    if not text.strip():
        raise HTTPException(status_code=400, detail="Input text cannot be empty.")

    # Tokenize input
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=128)
    
    # Predict
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
        probabilities = torch.softmax(logits, dim=1)
        predicted_class = torch.argmax(probabilities, dim=1).item()
        confidence = probabilities[0][predicted_class].item()
        
    return PredictionOutput(
        text=text,
        anxiety_level=label_mapping.get(predicted_class, "Unknown"),
        confidence=confidence
    )
