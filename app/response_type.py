from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi import HTTPException
import uvicorn


app = FastAPI()

@app.get("/nested-Json")
async def nestedJson():
    return {
        "name":"Salauddin",
        "age":23,
        "marrital status":False,
        "address":{
            "village":"Char Nurnagar",
            "Distic":"Sirajganj"
        },
        "Degree":["PSC","JSC","SSC","HSC","BSC going on"]
    }

@app.get("/html-data")
async def htmlDataShow():
    return '''
<h1>Title</h1>
<button>Submit</button>
'''

@app.get("/Custom-JsonResponse")
async def customJsonResponse():
    return JSONResponse(
        status_code=201,
        content={
            "Name":"Salauddin",
            "Status":"Learner"
        }
    )

@app.get("/httpException")
async def HttpExceptionHandling():
    return HTTPException(
        status_code=404,
        detail="Give Error the server"
    )