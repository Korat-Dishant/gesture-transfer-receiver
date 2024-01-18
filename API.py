

# from fastapi.middleware.cors import CORSMiddleware
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=False,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

import os
import sys

from fastapi import FastAPI , Header
from typing import Annotated, List, Union
# from fastapi.logger import logger
from pydantic_settings import BaseSettings

from controller import signal


class Settings(BaseSettings):
    BASE_URL: str = "http://localhost:8000"
    USE_NGROK: bool = True


settings = Settings()

app = FastAPI(title="GT receiver", description="gesture receiver")

    
def init_webhooks(base_url):
    # Update inbound traffic via APIs to use the public-facing ngrok URL
    pass


if settings.USE_NGROK:
    from pyngrok import ngrok
    port = "8000"
    tunnelAgent = ngrok.connect(port , basic_auth=["master:master123", "username2:password2"])
    public_url = tunnelAgent.public_url
    # logger.info("ngrok tunnel \"{}\" -> \"http://127.0.0.1:{}\"".format(public_url, port))
    print("\n\n\n\n\nngrok tunnel \"{}\" -> \"http://127.0.0.1:{}\"\n\n\n\n\n".format(public_url, port))

    # Update any base URLs or webhooks to use the public ngrok URL
    settings.BASE_URL = public_url
    init_webhooks(public_url)


# ... Initialize routers and the rest of our app
@app.get('/healthcheck')
def get_healthcheck():
    return {"server": "up"}

    
    
@app.get("/")
async def index():
    return {"message": "Hello World use //docs for swagger docs"}

@app.get("/actions")
async def get_actions(): 
    return {"actions" : ["up" , "down" , "left" , "right"]}


@app.post("/listening" ,  summary="pass value using header")
async def read_items(action: Annotated[Union[List[str], None], Header()] = None):
    # return {"response": str(ask_ai(action[0])) }
    print("\n\nreceived action \n" , action[0] )
    signal(action[0])
    return {"response": action[0] } 


   

