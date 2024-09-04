"""
Orchestrates webscraping and inserting data into tables
"""

from webscrape import VGScraper
from DBWrappers import ArticlesWrapper


class Orchestrator:
    def __init__(self):
        self.scrapers = VGScraper()
        self.article_table = ArticlesWrapper()
    
    def scrape_internet(self):
        
        # Get list of article data
        # For each article insert into tabell
        article_urls = self.scrapers.get_article_from_urls()
        for data in article_urls:
            try:
                self.article_table.insert_article(data)
            except Exception as e:
                print(f"""Couldnt insert data with 
                      the following url {data['article_url']}""")
        
        