from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def home():
    return {"message":
             "Welcome to the FastAPI application! Start workign with me and get ultra level experiance"}


@app.put("/putData")
def putData():
    return True

@app.patch("/patchData")
def patchData():
    return [
        "Rahim","Karim",12,14.2,True,False
    ]
@app.delete("/deleteDat")
def deleteDat():
    return{
        "message","delete data"
    }

@app.get("/readData")
def readData():
    return( 
        "message","Read the message"
    )