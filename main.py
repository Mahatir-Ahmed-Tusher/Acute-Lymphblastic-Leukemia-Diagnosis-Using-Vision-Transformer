from typing import Optional
from fastapi import FastAPI, File, UploadFile, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import utils

# App object
app = FastAPI()

# Static and Template directories
app.mount("/static", StaticFiles(directory=r"E:\ML research\Capstone\FInalProject(BloodDetection)\static"), name="static")
template = Jinja2Templates(directory=r"E:\ML research\Capstone\FInalProject(BloodDetection)\templates")

@app.get("/")
def home(request: Request):
    return template.TemplateResponse("prediction.html", {"request": request})

@app.post("/")
def demo_home(request: Request, file: UploadFile = File(...)):
    result = None
    error = None
    try:
        result = utils.get_prediction(input_img=file)
    except Exception as e:
        error = e
    return template.TemplateResponse("prediction.html", {"request": request, "result": result, "error": error})

@app.post("/pred")
async def demo_predict(request: Request, file: UploadFile = File(...)):
    result = None
    error = None
    try:
        result = utils.get_prediction(input_img=file)
        print("it is in the if")
    except Exception as e:
        error = e
        print("it is in the else", error)
    return template.TemplateResponse("prediction.html", {"request": request, "result": result, "error": error})
