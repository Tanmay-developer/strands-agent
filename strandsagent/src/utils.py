import boto3
import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def get_secret(SecName):
    logger.info(f"Retreiving secrets of: {SecName}")
    client = boto3.client("secretsmanager")
    try:
        response = client.get_secret_value(SecretId=SecName)
        # result = json.loads(response['SecretString'])
        return str(response['SecretString'])
    except Exception as e:
        logger.info(f"Error fetching secret: {e}")
        return None