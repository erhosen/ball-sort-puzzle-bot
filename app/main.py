import json
from typing import Optional

import numpy as np
from client import TelegramClientError, telegram_client
from image import ImageParser, ImageParserError
from solver import BallSortPuzzle


def handler(event: Optional[dict], context: Optional[dict]):
    body = json.loads(event['body'])  # type: ignore
    print(body)
    message = body['message']
    chat_id = message['chat']['id']

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
                puzzle = BallSortPuzzle(colors)  # type: ignore
                puzzle.solve()
                text = puzzle.get_telegram_repr()
    else:
        return {
            'statusCode': 200,
            'headers': {'Content-Type': 'application/json'},
            'body': '',
            'isBase64Encoded': False,
        }

    msg = {
        'method': 'sendMessage',
        'chat_id': chat_id,
        'text': text,
        'parse_mode': 'Markdown',
        'reply_to_message_id': message['message_id'],
    }

    return {
        'statusCode': 200,
        'headers': {'Content-Type': 'application/json'},
        'body': json.dumps(msg, ensure_ascii=False),
        'isBase64Encoded': False,
    }


if __name__ == "__main__":
    handler(None, None)
