from fastapi import FastAPI
from services.maneger.maneger import Manager
app = FastAPI()

@app.post('/process')
def process_data():
    try:
        Manager.manager()
    except Exception as ex:
        print('Error:',ex)