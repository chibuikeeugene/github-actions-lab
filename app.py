from fastapi import FastAPI

from calculator import add

# create a FastAPI app object
app = FastAPI(title="Calculator API")


# Define status check endpoint
@app.get("/health")
def health_status() -> dict[str, str]:
    """return the health status of the api"""
    return {"status": "ok"}


@app.get("/add")
def add_numbers(a: float, b: float) -> dict[str, float]:
    """add two numbers"""
    result = add(a, b)
    return {"Ressult": result}
