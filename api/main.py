from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
import json

app = FastAPI()

templates = Jinja2Templates(directory="../ui/build")
app.mount('/static', StaticFiles(directory="../ui/build/static"), 'static')


@app.get("/{rest_of_path:path}")
async def react_app(req: Request, rest_of_path: str):
    print(f'Rest of path: {rest_of_path}')
    return templates.TemplateResponse(
        'index.html',
        {
            'request': req
        }
    )

@app.post("/generate")
async def generate(
    req: Request,
    message: dict
):
    print("Model endpoint call")
    # Dummy chatbot - replies what you asked :)
    payload = jsonable_encoder(
        {
            "answer": f"BEEP BEEP - you asked: " + message["question"],
            "chat_history_ids": message["chat_history_ids"] + ["#" + message["question"]]
        })
    response = JSONResponse(content=payload)
    return response

