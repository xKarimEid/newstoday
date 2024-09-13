"""
This module defines the RAG (Retrieve and Generate) class for handling article embeddings 
and generating responses based on user prompts using a generative AI model.

Components:
- EmbeddingWrapper: A wrapper for interacting with an SQLite database containing article embeddings.
- RAG: A class that manages embedding-based retrieval of articles and generates responses
  using a generative AI model.
"""


import os
from dotenv import load_dotenv

from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import google.generativeai as genai

from table_wrappers import EmbeddingWrapper


class RAG:
    """
    A class that implements the Retrieve and Generate (RAG) framework for querying and 
    generating responses based on article embeddings.

    This class uses an embedding table to retrieve articles that are most similar to a 
    user's prompt and generates a response using a generative AI model.

    Attributes:
        embedding_table (EmbeddingWrapper): An instance of the EmbeddingWrapper 
        class for accessing stored embeddings.
        model (GenerativeModel): An instance of the generative AI model used to generate responses.
    """


    def __init__(self):
        """
        Initialize the RAG class by setting up the embedding table and generative AI model.
        
        Loads API keys from environment variables and configures the generative AI model.
        """

        self.embedding_table = EmbeddingWrapper()
        load_dotenv()
        genai.configure(api_key=os.environ["apikey"])
        self.model = genai.GenerativeModel("gemini-1.5-flash")

    def get_cosine_distances(self, user_embedding):
        """
        Compute cosine similarities between the user's embedding and all stored article embeddings.

        Args:
            user_embedding (np.ndarray): The embedding vector of the user's prompt.

        Returns:
            List[Tuple[float, str]]: A list of tuples where each tuple contains:
                - cosine_sim (float): The cosine similarity score between the 
                user's embedding and an article's embedding.
                - article (str): The content of the article corresponding to the embedding.
        """

        # Get all articles and corresponding embeddings
        rows = self.embedding_table.get_articles_embeddings()
        res = []
        for row in rows:
            article, embedding = row[0], row[1],
            cosine_sim = cosine_similarity(np.array(embedding).reshape(1, -1),
                                           np.array(user_embedding).reshape(1, -1))
            res.append((cosine_sim, article))

        return res


    def embed_prompt(self, prompt):
        """Generate an embedding for a given user prompt"""

        user_embedding = genai.embed_content(model="models/text-embedding-004", content=prompt)
        user_embedding = user_embedding['embedding']

        return user_embedding

    def get_top_k(self, user_prompt, k):
        """Get top k closest vectors to the user_prompt"""

        user_embedding = self.embed_prompt(user_prompt)
        cosine_distances = self.get_cosine_distances(user_embedding)
        cosine_distances.sort(key=lambda k: -k[0])

        return [article for embed, article in cosine_distances[:k]]

    def search_news(self, user, k=3):
        """
        Generate a response to a user's query using the top k relevant articles.

        Args:
            user (str): The user's query or prompt.
            k (int, optional): The number of top similar articles to use
            for generating the response. Defaults to 3.

        Returns:
            str: The generated response based on the user's query and the top k relevant articles.
        """

        result = self.get_top_k(user, k)

        head_prompt = f"""
              Du er en hjelpsom assistent som er flink på å gjøre gode sammendrag av nyheter. 
              Du blir stilt dette spørsmålet: {user}. 
              Du skal svare på det spørsmålet ved hjelp av denne informasjonen: {result}.
              Begynn svaret slik: Basert på informasjonen jeg har, eller ta lignende start.
              Vis informasjonen ikke svarer på spørsmålet så kan du si det nærmeste jeg fant er dette:
              """

        response = self.model.generate_content(head_prompt)

        return response.text
