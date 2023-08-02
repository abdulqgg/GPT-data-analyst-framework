import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from dotenv import load_dotenv

load_dotenv()

slack_token = os.getenv("SLACK_API_TOKEN")

client = WebClient(token=slack_token)

try:
    # Call the conversations.history method using the WebClient
    # conversations.history returns the first 100 messages from a channel
    result = client.conversations_history(channel="channel_id")

    messages = result.data['messages']

    for msg in messages:
        print(msg['text'])

except SlackApiError as e:
    print(f"Error fetching messages: {e}")
