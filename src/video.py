import os

from googleapiclient.discovery import build


class Video:
    api_key: str = os.getenv('YT_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, id_video):
        self.id_video = id_video
        video_response = Video.youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                     id=self.id_video).execute()
        self.video_title: str = video_response['items'][0]['snippet']['title']
        self.url = f"https://www.youtube.com/watch?v={id_video}"
        self.view_count: int = video_response['items'][0]['statistics']['viewCount']
        self.like_count: int = video_response['items'][0]['statistics']['likeCount']
        self.comment_count: int = video_response['items'][0]['statistics']['commentCount']

    def __str__(self):
        return self.video_title


class PLVideo(Video):
    def __init__(self, playlist_id, id_video):
        super().__init__(id_video)
        self.playlist_id = playlist_id

    def __str__(self):
        playlist_videos = Video.youtube.playlistItems().list(playlistId=self.playlist_id, part='contentDetails',
                                                             maxResults=50, ).execute()
        video_id = playlist_videos['items'][0]['contentDetails']['videoId']
        video_response = Video.youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                     id=video_id).execute()
        return video_response['items'][0]['snippet']['title']


