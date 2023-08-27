import os
import requests

from googleapiclient.discovery import build

class PLNotFound(Exception):
    pass

class Video:
    api_key: str = os.getenv('YT_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, id_video):
        self.id_video = id_video
        response = requests.get(f'https://www.youtube.com/watch?v={self.id_video}')
        if response.status_code != 200:
            raise PLNotFound

        try:
            self.video_response = Video.youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                     id=self.id_video).execute()
            self.title: str = self.video_response['items'][0]['snippet']['title']
            self.view_count: int = self.video_response['items'][0]['statistics']['viewCount']
            self.like_count: int = self.video_response['items'][0]['statistics']['likeCount']
            self.comment_count: int = self.video_response['items'][0]['statistics']['commentCount']
        except IndexError:
            self.title = None
            self.view_count = None
            self.like_count = None
            self.comment_count = None
            self.url = f'https://www.youtube.com/watch?v={self.id_video}'


    def __str__(self):
        return self.title

class PLVideo(Video):
    def __init__(self, id_video, playlist_id):
        super().__init__(id_video)
        self.playlist_id = playlist_id

    def __str__(self):
        playlist_videos = Video.youtube.playlistItems().list(playlistId=self.playlist_id, part='snippet',
                                                             maxResults=50, ).execute()
        return playlist_videos['items'][0]['snippet']['title']


def send_request(site_name):
    response = requests.get(site_name)
    if response.status_code != 200:
        return None


