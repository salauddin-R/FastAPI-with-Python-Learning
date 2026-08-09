from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def home():
    return {"message":
             "Welcome to the FastAPI application! Start workign with me and get ultra level experiance"}


@app.put("/put")
def putData():
    return{
        "message":"This is Put Data"
    }

@app.patch("/patch")
def patchData():
    return{
        "message":"Patch Data"
    }
@app.delete("/delete")
def deleteDat():
    return{
        "message":"delete data"
    }

@app.get("/get")
def readData():
    return{
        "message":"Read the message"
    }