class Video:

    def __init__(self, id, title, url, views, likes):
        self.id = id
        self.title = title
        self.url = url
        self.views = views
        self.likes = likes

class PLVideo:

    def __init__(self, id, title, url, views, likes, plid):
        self.id = id
        self.title = title
        self.url = url
        self.views = views
        self.likes = likes
        self.plid = plid
