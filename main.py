from fastapi import FastAPI


app = FastAPI()

@app.get("/")
async def myçfirst_api():
    return {"message": "first FastAPI example"}