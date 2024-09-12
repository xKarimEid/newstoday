"""
Orchestrates webscraping and inserting data into tables
"""

"""
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

"""

from dotenv import load_dotenv
import google.generativeai as genai
import os
from DBWrappers import EmbeddingWrapper
from webscrape import VGScraper


if __name__ == "__main__":

    # Scrapes and inserts into table
    # Load env variables from .env file
    load_dotenv()
    # Conifgure the model
    genai.configure(api_key=os.environ["apikey"])
    model = genai.GenerativeModel("gemini-1.5-flash")

    # Connect to embedding table
    emb_table = EmbeddingWrapper()
    # Scrape articles
    scraper = VGScraper()
    data = scraper.get_article_urls()

    # Iterate through article urls to extract articles
    # And embed them then insert into table
    for i in range(len(data)):
        url = data[i]['url']
        article = scraper.get_article_from_url(url)
        # If article exists
        if len(article) > 0:
            data[i]['article'] = article 
            # Create article embeddings
            embedding = genai.embed_content(model="models/text-embedding-004", content=data[i]['article'][:9500])
            data[i]['embedding'] = embedding['embedding']
            emb_table.insert_row(data[i])
            print(f"finished inserting: {data[i]['header']}")
