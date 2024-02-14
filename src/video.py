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
        return build('youtube', 'v3', developerKey=api_key)

    def video_request(self):
        service = Video.get_service()
        return service.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                id=self.video_id
                                                ).execute()

    def make_attributes(self):
        info = self.video_request()
        self.video_title: str = info['items'][0]['snippet']['title']
        self.view_count: int = info['items'][0]['statistics']['viewCount']
        self.like_count: int = info['items'][0]['statistics']['likeCount']
        self.comment_count: int = info['items'][0]['statistics']['commentCount']

class PLVideo(Video):

    def __init__(self, video_id, pl_id):
        self.video_id = video_id
        self.pl_id = pl_id

    def __str__(self):
        return f'{self.video_title}'

    def playlist_request(self):
        service = super.get_service()
        return service.playlistItems().list(playlistId=self.pl_id,
                                               part='contentDetails',
                                               maxResults=50,
                                               ).execute()

    def perebor(self):
        for video in self.playlist_request['items']:
            iso_8601_duration = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_8601_duration)
            print(duration)

    def make_attributes(self):
        info = self.video_request()
        self.video_title: str = info['items'][0]['snippet']['title']
        self.view_count: int = info['items'][0]['statistics']['viewCount']
        self.like_count: int = info['items'][0]['statistics']['likeCount']
        self.comment_count: int = info['items'][0]['statistics']['commentCount']
