from strands import tool, Agent
from strands.tools.mcp import MCPClient
from strands.models import BedrockModel
from mcp import StdioServerParameters, stdio_client
from strands_tools import use_aws
import logging
import os
import atexit
from typing import Dict

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# aws_docs_mcp_client = MCPClient(lambda: stdio_client(
#     StdioServerParameters(command="uvx", args=["awslabs.aws-documentation-mcp-server@latest"])
# ))
# aws_docs_mcp_client.start()

# aws_diagram_mcp_client = MCPClient(lambda: stdio_client(
#     StdioServerParameters(command="uvx", args=["awslabs.aws-diagram-mcp-server@latest"])
# ))
# aws_diagram_mcp_client.start()

# docs_tools = aws_docs_mcp_client.list_tools_sync()
# diagram_tools = aws_diagram_mcp_client.list_tools_sync()

# @tool
# def send_reponse_on_email(result: str)
#     try:
#         message = {"Html": {"Data": body}} if is_html else {"Text": {"Data": body}}
#         ses_client = boto3.client("ses")
#         FROM_EMAIL = os.getenv("EMAIL_FROM", "agent@mockify.com")
#         response = ses_client.send_email(
#             Source=FROM_EMAIL,
#             Destination={"ToAddresses": [to_email]},
#             Message={
#                 "Subject": {"Data": subject},
#                 "Body": message,
#             },
#         )
#         return f"Email sent successfully! Message ID: {response['MessageId']}"

#     except Exception as e:
#         return f"Error sending email: {str(e)}"

# tools_list = [use_aws]

    # Create a BedrockModel with system inference profile
def getmyagent(_query):

    bedrock_model = BedrockModel(
        model_id="anthropic.claude-3-sonnet-20240229-v1:0",  # System inference profile ID
        region_name="ap-south-1",
        temperature=0.1,
    )

    with open("agent_prompt.txt", "r", encoding="utf-8") as file:
        system_prompt = file.read()

    agent = Agent(
        tools=[use_aws],
        model=bedrock_model,
        system_prompt=system_prompt
    )

    response = agent(_query)

    logger.info(f'Response Received from LLM: {response}')

    return str(response)