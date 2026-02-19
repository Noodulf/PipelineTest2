from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "Monitor is Online"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.get("/audit")
def audit_site(url: str):
    # INTENTIONAL BUG: Using os.system with user input is a security risk.
    # This is here so Bandit (the auditor) has something to catch.
    response = os.system(f"curl -I {url}")
    return {"url": url, "result_code": response} 
