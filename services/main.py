from fastapi import FastAPI
import uvicorn

from services.maneger.maneger import Manager
app = FastAPI()

@app.get('/process')
def process_data():
    try:
        processing = Manager.manager()
        return {'result': processing}
    except Exception as ex:
        print('Error:',ex)