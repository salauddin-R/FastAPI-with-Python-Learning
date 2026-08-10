from fastapi import FastAPI,Response
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/headerExample1")
async def hello(response:Response):
    response.headers["key1"]="value1"
    response.headers["key2"]="value2"
    response.headers["key3"]="value3"
    response.headers["key4"]="value4"
    return "Hello FastAPI"

@app.get("/header2")
async def header2():
    return JSONResponse(
        status_code=200,
        content={
            "Status":"success"
        },
        headers={
            "key1":"value1",
            "key2":"value2",
            "key3":"value3",
            "key4":"value4",
        }
    )



