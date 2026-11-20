from fastapi import FastAPI

app = FastAPI(
    title="Cloud AI Service",
    description="Python REST API for cloud deployment",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "Welcome to Cloud AI Service",
        "status": "Running"
    }

@app.get("/health")
def health_check():
    return {
        "status": "Healthy",
        "service": "Cloud AI Service"
    }

@app.post("/predict")
def predict(data: dict):
    value = data.get("value", 0)

    return {
        "input": value,
        "result": value * 2,
        "message": "Demo inference completed"
    }