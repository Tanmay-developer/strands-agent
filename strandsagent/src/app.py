import json
from tools import getmyagent
# from tools import tools_list
import base64
import logging
from utils import get_secret
import os
import boto3
import urllib.parse
from twilio.rest import Client

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
    
    logger.info(f"Final Answer: {response_message}")

    account_sid = get_secret("TWILIO_ACCOUNT_SID")
    auth_token = get_secret("TWILIO_AUTH_TOKEN")
    whatsapp_no = get_secret("MY_WHATSAPP_ID")

    client = Client(account_sid, auth_token)

    try: 
        message = client.messages.create(
            body=response_message,
            from_="whatsapp:+14155238886",
            to=f"whatsapp:{whatsapp_no}",
        )
        logger.info(f"Message sent: SID {message.sid}")
    except Exception as e:
        logger.error(f"Failed to send message: {e}")
        return {
            "statusCode": 500,
            "body": json.dumps({"error": "Failed to send message"})
        }

    return {
        "statusCode": 200,
        "body": json.dumps({"message": f"Here you go: {response_message}"})
    }