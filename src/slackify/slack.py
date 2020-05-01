import json
import requests


from .tasks import async_task


"""Acknowledge we received slack's interaction payload"""
OK = '', 200
ACK = OK

JSON_TYPE = {'Content-Type': 'application/json'}


def reply_text(text: str):
    """Return tuple response of simple text"""
    return json.dumps({'text': text}), 200, JSON_TYPE

def reply(body: dict):
    return json.dumps(body), 200, JSON_TYPE

def text_block(text: str, markdown=True):
    return {
        "type": "section",
        "text": {
            "type": "mrkdwn" if markdown else 'plain_text',
            "text": text
        }
    }


def block_reply(blocks: list):
    return json.dumps({'blocks': blocks}), 200, JSON_TYPE


@async_task
def respond(url: str, message: str):
    """Respond async to interaction to allow fast acknowledge of interactive message request"""
    return requests.post(url, json=message, timeout=5)