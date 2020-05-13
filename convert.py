from crawling import crawling
from bs4 import BeautifulSoup
import re


class Convert:
    def __init__(self, url):
        self.html = crawling(url)
        self.soup = BeautifulSoup(self.html, 'html.parser')
        self.hangul = self.soup.select('body')
        self.__no_hangul__ = re.compile("""[^ ㄱ-ㅣ가-힣]+""")
        self.hangul = self.__no_hangul__.sub('', str(self.hangul))
        self.content_list = list(n.strip() for n in self.hangul.split('  ') if n != '')


p = Convert('https://news.naver.com/')
for ele in p.content_list:
    print(ele)
q = Convert('https://bodhi-sattva.tistory.com/89')
for ele in q.content_list:
    print(ele)
