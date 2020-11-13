import asyncio
from typing import Optional


async def _handler(event: Optional[dict], context: Optional[dict]):
    body = event and event['body']

    return {
        'statusCode': 200,
        'headers': {'Content-Type': 'application/json'},
        'body': body,
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
