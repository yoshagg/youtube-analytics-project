from googleapiclient.discovery import build
import os
import datetime

class PlayList:

    def __init__(self, playlist_id):
        self.playlist_id = playlist_id
        self.make_attributes()
        self.info = self.playlist_info_request()
        self.contentDetails = self.playlist_contentDetails_request()


    @classmethod
    def get_service(cls):
        api_key: str = os.getenv('API_KEY')
        return build('youtube', 'v3', developerKey=api_key)


    def playlist_info_request(self):
        service = self.get_service()
        return service.playlistItems().list(playlistId=self.playlist_id,
                                               part='snippet'
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
        self.url: str = info['items'][0]['snippet']['thumbnails']['default']['url']

    def get_playlist_ids(self):
        return [video['contentDetails']['videoId'] for video in self.contentDetails['items']]

    def total_duration(self):
        service = self.get_service()
        ids = self.get_playlist_ids()
        return service.videos().list(part='contentDetails,statistics',
                                       id=','.join(ids)
                                       ).execute()

    # def show_best_video(self):
    #     return self.info['items'][0]['snippet']['thumbnails']['statistics'][max('likecount')]
