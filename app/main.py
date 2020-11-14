import json
from typing import Optional


def handler(event: Optional[dict], context: Optional[dict]):
    body = event['body']  # type: ignore
    body = json.loads(body)

    msg = {'method': 'sendMessage', 'chat_id': body['message']['chat']['id'], 'text': body['message']['text']}

    return {
        'statusCode': 200,
        'headers': {'Content-Type': 'application/json'},
        'body': json.dumps(msg),
        'isBase64Encoded': False,
    }


if __name__ == "__main__":
    handler(None, None)
