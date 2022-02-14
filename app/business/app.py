import json
import uuid
import os
import requests
import logging
from cloudevents.http import CloudEvent, to_binary, from_http
from app.models.cloud_event_model import CloudEventModel
from fastapi import FastAPI, Request, Response

logging.basicConfig(
    filename='logfile.log',
    level=logging.DEBUG,
    format='%(asctime)s:%(levelname)s:%(message)s'
)

app = FastAPI()

@app.post("/")
async def service_process(event_received: CloudEventModel, request: Request, response: Response):

    return {"msg": "Hi - " + event_received.msg}
