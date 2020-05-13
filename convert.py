from crawling import crawling
from bs4 import BeautifulSoup
import re


class Convert:
    def __init__(self, url):
        self.html = crawling(url)
        self.soup = BeautifulSoup(self.html, 'html.parser')
        self.hangul = self.soup.select('body context')
        if self.hangul is []:
            self.__no_hangul__ = re.compile("""[^ ㄱ-ㅣ가-힣|'"]+""")
            self.hangul = self.__no_hangul__.sub('', str(self.soup))
        self.wow = self.soup.get_text


p = Convert('http://www.itworld.co.kr/news/150073')
print(p.hangul)
print(p.wow)
q = Convert('https://bodhi-sattva.tistory.com/89')
print(q.hangul)
