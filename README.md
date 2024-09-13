This is a very simple repo for educational purposes on how to use RAG. 

# News Article Scraper and Embedding System

This repository contains a collection of scripts for scraping news articles, managing embeddings, and generating responses based on user queries. The system integrates web scraping with a generative AI model to handle and query news articles effectively.



## `main.py`
This script orchestrates the process of web scraping, embedding article content, and storing it in the database. It uses `VGScraper` to fetch article data and `EmbeddingWrapper` to store embeddings.

## Usage
1. Ensure you have a `.env` file with your API key for a gemini model.
2. Run the main.py script to scrape articles, generate embeddings, and insert them into the database.

```bash
python main.py
