import json

import numpy as np
from client import TelegramClientError, telegram_client
from image import ImageParser, ImageParserError
from pydantic import BaseModel
from solver import BallSortPuzzle, get_telegram_repr


class WebhookResponse(BaseModel):
    statusCode: int
    headers: dict
    body: str
    isBase64Encoded: bool


def process_message(message: dict) -> WebhookResponse:
    if photos := message.get('photo'):
        # here photos is an array with same photo of different sizes
        hd_photo = max(photos, key=lambda x: x['file_size'])  # get one with the highest resolution
        try:
            file = telegram_client.download_file(hd_photo['file_id'])
        except TelegramClientError:
            text = "Cant download the image from TG :("
        else:
            file_bytes = np.asarray(bytearray(file.read()), dtype=np.uint8)
            try:
                image_parser = ImageParser(file_bytes)
                colors = image_parser.to_colors()
            except ImageParserError as exp:
                text = f"Cant parse image: {exp}"
            else:
                puzzle = BallSortPuzzle(colors)
                solved = puzzle.solve()
                if solved:
                    text = get_telegram_repr(puzzle)
                else:
                    text = "This lvl don't have a solution"
    else:
        return WebhookResponse(
            statusCode=200, headers={'Content-Type': 'application/json'}, body='', isBase64Encoded=False
        )

    msg = {
        'method': 'sendMessage',
        'chat_id': message['chat']['id'],
        'text': text,
        'parse_mode': 'Markdown',
        'reply_to_message_id': message['message_id'],
    }

    return WebhookResponse(
        statusCode=200,
        headers={'Content-Type': 'application/json'},
        body=json.dumps(msg, ensure_ascii=False),
        isBase64Encoded=False,
    )


def handler(event: dict | None, context) -> dict:
    body = json.loads(event['body'])  # type: ignore
    print(body)

    message = body['message']
    response = process_message(message)
    return response.dict()


if __name__ == "__main__":
    handler(None, None)
