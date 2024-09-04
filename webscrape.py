from urllib.request import urlopen
from bs4 import BeautifulSoup
from datetime import datetime

class VGScraper:
    def __init__(self):
        self.url = 'https://www.vg.no'
        #self.urls = []
    
    def _get_html(self):
        """Get the html content of the main page"""

        html = urlopen(self.url)
        bs = BeautifulSoup(html, 'html.parser')
        return bs
    
    def get_article_urls(self):
        """Get all article urls from the main page"""
    
        bs = self._get_html()
        article_data = []
        for item in bs.find_all('a', {'itemprop': 'url'}):
            data = {}
            if item['href']:
               # Store the article url
               data['url'] = item['href']
               # Store what newspaper this is
               data['newspaper'] = 'vg'
               # Store the article header
               data['header'] = item.h2.text.replace('\n', '')
               # Add datetime
               dt = datetime.now()
               dt = dt.strftime('%Y-%m-%d %H:%M:%S')
               data['event_datetime'] = dt
               # Append for later insertion
               article_data.append(data)

        return article_data
    
    def get_article_from_url(self, article_url):
        """Get the article text from the article url"""
    
        req = urlopen(article_url)
        bs = BeautifulSoup(req, 'html.parser')
        paraghs = []
        for p in bs.find_all('p'):
            paraghs.append(p.get_text())
        
        return ' '.join(paraghs)


if __name__ == '__main__':
    s = VGScraper()
