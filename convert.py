from .crawling import crawling


class Convert:
    def __int__(self, url):
        self.html = crawling(url)
