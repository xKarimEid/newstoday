from urllib.request import urlopen
from bs4 import BeautifulSoup

class VGScraper:
    def __init__(self):
        self.url = 'https://www.vg.no'
        #self.urls = []
    
    def get_html(self):
        html = urlopen(self.url)
        bs = BeautifulSoup(html, 'html.parser')
        return bs
    
    def get_urls(self):
        bs = self.get_html()
        urls = []
        for item in bs.find_all('a', {'itemprop': 'url'}):
            if item['href']:
               urls.append(item['href'])
        
        return urls
    
    def get_article_from_url(self, url):
        req = urlopen(url)
        bs = BeautifulSoup(req, 'html.parser')
        paraghs = []
        for p in bs.find_all('p'):
            paraghs.append(p.get_text())
        
        return ' '.join(paraghs)


if __name__ == '__main__':
    s = VGScraper()
    urls = s.get_urls()
