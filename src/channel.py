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
        self.channel = Channel.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(json.dumps(self.channel, indent=2, ensure_ascii=False))

    @property
    def title(self):
        return self.channel['items'][0]['snippet']['title']

    @property
    def video_count(self):
        return self.channel['items'][0]['statistics']['videoCount']

    @property
    def description(self):
        return self.channel['items'][0]['snippet']['description']

    @property
    def url(self):
        return f"https://www.youtube.com/channel/{self.channel['items'][0]['id']}"

    @property
    def subscriberCount(self):
        return self.channel['items'][0]['statistics']['subscriberCount']

    @property
    def viewCount(self):
        return self.channel['items'][0]['statistics']['viewCount']

    @classmethod
    def get_service(cls):
        return cls.youtube

    def to_json(self, name_json):
        json_string = json.dumps(self.channel, indent=2, ensure_ascii=False)
        jsonFile = open(name_json, "w")
        jsonFile.write(json_string)
        jsonFile.close()

    def __str__(self):
        return f"'{self.channel['items'][0]['snippet']['title']} (https://www.youtube.com/channel/{self.channel['items'][0]['id']})'"

    def __add__(self, other):
        return int(self.channel['items'][0]['statistics']['subscriberCount']) + int(other.channel['items'][0][
            'statistics'][
            'subscriberCount'])
    def __sub__(self, other):
        return int(other.channel['items'][0]['statistics']['subscriberCount']) - int(self.channel['items'][0][
            'statistics'][
            'subscriberCount'])

    def __gt__(self, other):
        if int(self.channel['items'][0]['statistics']['subscriberCount']) > int(other.channel['items'][0][
            'statistics'][
            'subscriberCount']):
            return True
        else:
            return False


    def __ge__(self, other):
        if int(self.channel['items'][0]['statistics']['subscriberCount']) >= int(other.channel['items'][0][
            'statistics'][
            'subscriberCount']):
            return True
        else:
            return False

    def __lt__(self, other):
        if int(self.channel['items'][0]['statistics']['subscriberCount']) < int(other.channel['items'][0][
            'statistics'][
            'subscriberCount']):
            return True
        else:
            return False

    def __le__(self, other):
        if int(self.channel['items'][0]['statistics']['subscriberCount']) <= int(other.channel['items'][0]['statistics']['subscriberCount']):
            return True
        else:
            return False

    def __eq__(self, other):
        if int(self.channel['items'][0]['statistics']['subscriberCount']) == int(other.channel['items'][0][
            'statistics'][
            'subscriberCount']):
            return True
        else:
            return False
