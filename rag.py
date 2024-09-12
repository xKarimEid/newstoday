"""
RAG class queries the embedding table to find the closest
articles to the user prompt
"""


from DBWrappers import EmbeddingWrapper
from sklearn.metrics.pairwise import cosine_similarity
import google.generativeai as genai
import numpy as np
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.environ["apikey"])

class RAG:
    def __init__(self):
        self.embedding_table = EmbeddingWrapper()
        

    def get_cosine_distances(self, user_embedding):
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
        user_embedding = genai.embed_content(model="models/text-embedding-004", content=prompt)
        user_embedding = user_embedding['embedding']
        return user_embedding
    
    def get_top_k(self, user_prompt, k):
        user_embedding = self.embed_prompt(user_prompt)
        cosine_distances = self.get_cosine_distances(user_embedding)
        print(cosine_distances)
        cosine_distances.sort(key=lambda k: -k[0])

        return [article for embed, article in cosine_distances[:k]]
