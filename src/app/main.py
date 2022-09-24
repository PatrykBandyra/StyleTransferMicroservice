from fastapi import FastAPI
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(name)s: %(message)s')
file_handler = logging.FileHandler('log/app.log', mode='w')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


app = FastAPI()


@app.get('/hello')
async def get_hello():
    logger.info('Hello called!')
    return 'hello'
