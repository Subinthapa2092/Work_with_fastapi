##### python in a program to do the work with the fastapi
from fastapi import FastAPI

app = FastAPI() ### Object instance : 

### python in a program to do the Wellcome the Person in that case: 
@app.get("/")
def say_hellow():
    return {"message":"Saying Hellow to the World of the Person! "}
