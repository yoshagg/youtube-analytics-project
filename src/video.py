from googleapiclient.discovery import build
import os
import isodate

class Video:

    def __init__(self, video_id):
        self.video_id = video_id
        self.info = self.video_request()
        self.make_attributes()

    def __str__(self):
        return f'{self.video_title}'

    @classmethod
    def get_service(cls):
        api_key: str = os.getenv('API_KEY')
        service = build('youtube', 'v3', developerKey=api_key)
        return service

    def video_request(self):
        service = Video.get_service()
        info = service.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                id=self.video_id
                                                ).execute()


    def make_attributes(self):
        try:
            self.video_title: str = self.info['items'][0]['snippet']['title']
            self.view_count: int = self.info['items'][0]['statistics']['viewCount']
            self.like_count: int = self.info['items'][0]['statistics']['likeCount']
            self.comment_count: int = self.info['items'][0]['statistics']['commentCount']
        except Exception:
            self.video_title = None
            self.view_count = None
            self.like_count = None
            self.comment_count = None


class PLVideo(Video):

    def __init__(self, video_id, pl_id):
        self.video_id = video_id
        self.pl_id = pl_id
        super.make_attributes()

    def playlist_request(self):
        service = Video.get_service()
        return service.playlistItems().list(playlistId=self.pl_id,
                                               part='contentDetails',
                                               maxResults=50,
                                               ).execute()

e = Video("broken")
e.video_request()

