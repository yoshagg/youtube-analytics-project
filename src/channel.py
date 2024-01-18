class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        self.title = title
        self.url = url
        self.subscribers = subscribers
        self.video_count = video_count
        self.view_count = view_count

    def __str__(self):
        return f'{self.title} - {self.url}'

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(self.channel_id)

    def get_service(self):
        api_key: str = os.getenv('API_KEY')
        return build('youtube', 'v3', developerKey=api_key)

    def to_json(self):
        with open('information.json', 'a') as file:
            file.write(f"""{self.channel.id}\n""")
            file.write(f"""{self.title}\n""")
            file.write(f"""{self.link}\n""")
            file.write(f"""{self.subscribers}\n""")
            file.write(f"""{self.video_count}\n""")
            file.write(f"""{self.views_count}\n\n""")
