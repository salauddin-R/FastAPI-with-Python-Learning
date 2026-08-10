from fastapi import FastAPI,Response

app = FastAPI()

@app.get("/hellow")
async def hellow(response:Response):
    response.set_cookie(
        key="key001",
        value="value001",
        domain="127.0.0.1",
        path="/",
        expires=3600,
        httponly=True,
        secure=True
    )
    return {
        "message":"Hello world!"
    }

"""
key==>name
value==>vlue
domain==>which domain
path ==> //hello,/,/
expires ==> Till valid
httponly ==>True  javascrip fontend a kaj korba na so false kora dita hoba
secure=True sudu matro https a kaj korba
"""