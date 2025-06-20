import json
from tools import getmyagent
from tools import tools_list
import logging
from utils import get_secret
import os
import boto3

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    logger.info(f"Received event: {event}")

    body = event.get('query')

    response_message = getmyagent(body) 
    
    return {
        "response": response_message 
    }