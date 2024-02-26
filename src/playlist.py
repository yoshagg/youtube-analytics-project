from googleapiclient.discovery import build
import os
import datetime
import isodate

class PlayList:

    def __init__(self, playlist_id):
        self.playlist_id = playlist_id
        self.make_attributes()
        self.info = self.playlist_info_request()
        self.contentDetails = self.playlist_contentDetails_request()
        self.service = self.get_service()


    @classmethod
    def get_service(cls):
        api_key: str = os.getenv('API_KEY')
        return build('youtube', 'v3', developerKey=api_key)


    def playlist_info_request(self):
        service = self.get_service()
        return service.playlists().list(id=self.playlist_id,
                                                      part='snippet',
                                                      ).execute()

    def playlist_contentDetails_request(self):
        service = self.get_service()
        return service.playlistItems().list(playlistId=self.playlist_id,
                                               part='contentDetails',
                                               maxResults=50,
                                               ).execute()
    def make_attributes(self):
        info = self.playlist_info_request()
        self.title: str = info['items'][0]['snippet']['title']
        self.url = f'https://www.youtube.com/playlist?list={self.playlist_id}'

    def get_playlist_ids(self):
        return [video['contentDetails']['videoId'] for video in self.contentDetails['items']]

    @property
    def total_duration(self):
        duration = datetime.timedelta(0)
        playlist_videos = self.playlist_info_request()
        video_ids = self.get_playlist_ids()
        video_response = self.service.videos().list(part='contentDetails,statistics',
                                               id=','.join(video_ids)
                                               ).execute()

        for video in video_response['items']:
            iso_8601_duration = video['contentDetails']['duration']
            duration += isodate.parse_duration(iso_8601_duration)
        return duration

    def show_best_video(self):
        max_like_count = 0
        video_ids = self.get_playlist_ids()
        playlist_videos = self.playlist_info_request()

        for video_id in video_ids:
            video_response = self.service.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                   id=video_id
                                                   ).execute()
            like_count = int(video_response['items'][0]['statistics']['likeCount'])
            if like_count > max_like_count:
                max_like_count = like_count
        if like_count == max_like_count:
            return f"https://youtu.be/{video_id}"
