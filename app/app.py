from fastapi import FastAPI

app = FastAPI()

@app.get("/hello-world")
def hello_world():
    return {"message": "Hello World"} # we use python dictionary because fastapi automatically converts it to json ( JavaScript Object Notation)


