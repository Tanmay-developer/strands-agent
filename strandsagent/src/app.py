import json
from tools import getmyagent
# from tools import tools_list
import base64
import logging
from utils import get_secret
import os
import boto3

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    logger.info(f"Received event: {event}")

    # Decode and parse body
    body = event.get('body', '')
    if event.get('isBase64Encoded', False):
        body = base64.b64decode(body).decode('utf-8')

    try:
        body_json = json.loads(body)
    except Exception as e:
        logger.error(f"Error parsing body JSON: {e}")
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "Invalid JSON"})
        }

    query = body_json.get("query")
    logger.info(f"Query raised from user: {query}")

    response_message = getmyagent(query)
    
    final_answer = {
        "response": response_message 
    }
    logger.info(f"Final Answer: {final_answer}")

    return final_answer