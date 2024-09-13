# News Article Scraper and Embedding System

This is a very simple repo for educational purposes on RAG. 

This repository contains a script for scraping news articles, managing embeddings, and generating responses based on user queries. The system integrates web scraping with a generative AI model to handle and query news articles effectively.

Use playground.ipynb to play and interact with the libraries


## Usage

1. **Set Up Environment Variables**
   - Obtain a free API key for the Gemini model from [Google AI Studio](https://aistudio.google.com/app/apikey).
   - Create a `.env` file in the root directory of your project.
   - Add the following line to the `.env` file, replacing `YOUR_API_KEY_HERE` with your actual API key:
     ```
     apikey=YOUR_API_KEY_HERE
     ```

2. **Run the `main.py` Script**
   - This script will scrape articles, generate embeddings, and insert them into the database.
     ```bash
     python main.py
     ```

3. **Interact with the Model**
   - Open `playground.ipynb` 
   - Use the notebook to query the model about today's news and interact with the generated content.


