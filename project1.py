##### python in a  program to do the work 

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def saying_hello():
    return{
        "Message":"Wellcome to My Website"
    }