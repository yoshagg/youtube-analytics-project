from googleapiclient.discovery import build
import os

class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        self.info = self.channel_info_request()
        self.make_attributes()

    def __str__(self):
        return f'{self.info}'

    def __add__(self, other):
        return int(self.subscriber_count) + int(other.subscriber_count)

    def __sub__(self, other):
        return int(self.subscriber_count) - int(other.subscriber_count)

    def __lt__(self, other):
        return int(self.subscriber_count) < int(other.subscriber_count)

    def __le__(self, other):
        return int(self.subscriber_count) <= int(other.subscriber_count)

    def __gt__(self, other):
        return int(self.subscriber_count) > int(other.subscriber_count)

    def __ge__(self, other):
        return int(self.subscriber_count) >= int(other.subscriber_count)



    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(self.channel_id)

    @classmethod
    def get_service(cls):
        api_key: str = os.getenv('API_KEY')
        return build('youtube', 'v3', developerKey=api_key)

    def channel_info_request(self):
        service = self.get_service()
        return service.channels().list(id=self.channel_id, part='snippet,statistics').execute()

    def make_attributes(self):
        info = self.channel_info_request()
        self.title = info['items'][0]['snippet']['title']
        self.description = info['items'][0]['snippet']['description']
        self.url = info['items'][0]['snippet']['thumbnails']['default']['url']
        self.subscriber_count = info['items'][0]['statistics']['subscriberCount']
        self.video_count = info['items'][0]['statistics']['videoCount']
        self.views_count = info['items'][0]['statistics']['viewCount']

    def to_json(self, doc):
        with open(doc, 'a') as file:
            file.write(f"""{self.channel_id}\n""")
            file.write(f"""{self.title}\n""")
            file.write(f"""{self.description}\n""")
            file.write(f"""{self.url}\n""")
            file.write(f"""{self.subscriber_count}\n""")
            file.write(f"""{self.video_count}\n""")
            file.write(f"""{self.views_count}\n\n""")


c = Channel('UC-OVMPlMA3-YCIeg4z5z23A')
print(c)
