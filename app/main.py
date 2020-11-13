import asyncio
import json
from typing import Optional


async def _handler(event: Optional[dict], context: Optional[dict]):
    body = event['body']  # type: ignore

    msg = {'method': 'sendMessage', 'chat_id': body['message']['chat']['id'], 'text': body['message']['text']}

    return {
        'statusCode': 200,
        'headers': {'Content-Type': 'application/json'},
        'body': json.dumps(msg),
        'isBase64Encoded': False,
    }


def handler(event: Optional[dict], context: Optional[dict]):
    """
    Synchronous wrapper of `_handler`, that can be called trough command line
    Yandex.Function do it so.
    """
    asyncio.run(_handler(event, context))


if __name__ == "__main__":
    handler(None, None)
