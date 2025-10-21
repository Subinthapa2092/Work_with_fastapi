#### Program in the python to work with the fastapi 

from fastapi import FastAPI

#### fastapi instance 
app = FastAPI()

#### Showing the Information like saying hellow Wellcome to the Facebook: 
@app.get("/")

### Defing the saying Hellow 
def say_hello():
    return {"message":"Wellcome to The FastAPI"}
#### Displaying the Name of the Person on it 
@app.get("/hello/{name}")
def name(name:str):
    return{
        "name":name,
        "message":f"Hellow ! {name} What you are doing?"
    }
