import os
import json

from googleapiclient.discovery import build

class Channel:
    api_key: str = os.getenv('YT_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id


    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        channel = Channel.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        print(json.dumps(channel, indent=2, ensure_ascii=False))



