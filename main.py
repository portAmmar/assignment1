from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {
            "name":"Task API"
            "version":"1.0"
            "enpoints":["/tasks"]
            }

@app.get("health")
def test_server_health():
    return {"status": "ok"}
