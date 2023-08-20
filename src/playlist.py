from src.video import PLVideo
import json
import datetime
import os

from googleapiclient.discovery import build

# class PlayList:
#     api_key: str = os.getenv('YT_API_KEY')
#     youtube = build('youtube', 'v3', developerKey=api_key)
#
#     def __init__(self, playlist_id):
#         playlist_videos = PLVideo.youtube.playlistItems().list(playlistId=playlist_id, part='contentDetails',
#                                                              maxResults=50, ).execute()
#         self.playlist_id = playlist_id
#         self.title = playlist_videos
#         self.url = f"https://www.youtube.com/playlist?list={self.playlist_id}"

playlist_id = 'PLv_zOGKKxVpj-n2qLkEM2Hj96LO6uqgQw'
api_key: str = os.getenv('YT_API_KEY')
youtube = build('youtube', 'v3', developerKey=api_key)
playlist_videos = youtube.playlistItems().list(playlistId=playlist_id, part='snippet',
                                                             maxResults=50, ).execute()

print(json.dumps(playlist_videos, indent=2, ensure_ascii=False))