"""
Wrapper around the articles table for managing text embeddings in a SQLite database.
"""

import sqlite3
import pickle


class EmbeddingWrapper:
    """
    A class to manage article embeddings in an SQLite database. 

    This class provides methods to create and drop the embeddings table,
    insert new article embeddings, and retrieve all stored embeddings.
    """

    def __init__(self):
        self.db = 'news.db'
        self._create_table()

    def _create_table(self):
        """
        Create the embeddings table if it doesn't already exist.

        The table schema includes:
        - header: A unique text field representing the article header.
        - article: A text field for the article content.
        - embedding: A BLOB field to store the serialized embedding vector.
        """

        query = """
                CREATE TABLE IF NOT EXISTS embeddings
                    (header text UNIQUE, 
                    article text,
                    embedding BLOB)
                """

        with sqlite3.connect(self.db) as conn:
            cursor = conn.cursor()
            cursor.execute(query)

    def _drop_table(self):
        """Table is dropped"""

        query = """
                DROP TABLE IF EXISTS embeddings
                """

        with sqlite3.connect(self.db) as conn:
            cursor = conn.cursor()
            cursor.execute(query)

    def insert_row(self, data):
        """
        Insert a new article embedding into the embeddings table.

        Args:
            data (dict): A dictionary containing:
                - 'header' (str): The article header.
                - 'article' (str): The article content.
                - 'embedding' (np.ndarray): The embedding vector to be stored.
        
        The embedding is serialized using the `pickle` module.
        """

        query = """
                INSERT OR IGNORE INTO embeddings 
                (header, article, embedding) VALUES (:header, :article, :embedding)
                """

        with sqlite3.connect(self.db) as conn:
            cursor = conn.cursor()
            cursor.execute(query, (data['header'],
                                   data['article'],
                                   pickle.dumps(data['embedding'])))

    def get_articles_embeddings(self):
        """
        Retrieve all articles and their embeddings from the database.

        Returns:
            list of tuples: Each tuple contains:
                - article (str): The article content.
                - embedding (np.ndarray): The deserialized embedding vector.
        """

        query = """SELECT article, embedding FROM embeddings"""

        with sqlite3.connect(self.db) as conn:
            cursor = conn.cursor()
            cursor.execute(query)
            rows = cursor.fetchall()

        # Deserialize embedding results
        result = []
        for row in rows:
            embed = pickle.loads(row[1])
            result.append((row[0], embed))

        return result
