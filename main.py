from flask import Flask
import config

app = Flask(__name__)
app.config.from_object(config)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/demo")
def demo():
    return {"id": "1001"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
