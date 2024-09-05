"""
Orchestrates webscraping and inserting data into tables
"""

from webscrape import VGScraper
from DBWrappers import ArticlesWrapper


if __name__ == '__main__':
    vgscraper = VGScraper()
    article_table = ArticlesWrapper()

    # Get all articles
    article_data = vgscraper.get_article_urls()
    # iterate through the article urls to get the article
    for data in article_data:
        # Get the article content
        article = vgscraper.get_article_from_url(data['url'])
        # Store the article
        data['article'] = article
        # Insert article row into articles table
        article_table.insert_article(data)
