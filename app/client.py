from io import BytesIO

import requests
from requests import Response
from settings import settings


class TelegramClientError(Exception):
    pass


class TelegramClient:
    def __init__(self, token):
        self.token = token

    @staticmethod
    def _api_call(url, params=None) -> Response:
        try:
            resp = requests.get(url, params=params)
            resp.raise_for_status()
            return resp
        except requests.RequestException as exp:
            print(f"Unexpected error {exp}")
            raise TelegramClientError from exp

    def get_file_data(self, file_id: str) -> dict:
        url = f"https://api.telegram.org/bot{self.token}/getFile"
        resp = self._api_call(url, params={'file_id': file_id})
        return resp.json()

    def get_file(self, file_path: str) -> BytesIO:
        url = f"https://api.telegram.org/file/bot{self.token}/{file_path}"
        resp = self._api_call(url)
        return BytesIO(resp.content)

    def download_file(self, file_id: str) -> BytesIO:
        file_data = self.get_file_data(file_id)
        file_path = file_data['result']['file_path']
        file = self.get_file(file_path)
        return file


telegram_client = TelegramClient(settings.TELEGRAM_BOT_TOKEN)
