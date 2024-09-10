"""
Wrapper around articles table
"""

import sqlite3
import pickle


class ArticlesWrapper:
    def __init__(self):
        self.db = 'news.db'
        self._create_articles_table()

    def _create_articles_table(self):
        """Create articles table if it doesnt exists"""

        query = '''
                CREATE TABLE IF NOT EXISTS articles
                (article_id INTEGER PRIMARY KEY,
                event_datetime datetime NOT NULL, 
                header TEXT UNIQUE,
                newspaper text NOT NULL, 
                url text UNIQUE,
                article text NOT NULL)
                '''
        
        with sqlite3.connect(self.db) as conn:
            cursor = conn.cursor()
            cursor.execute(query)

    def drop_articles_table(self):
        """Drop articles table if it exists"""

        with sqlite3.connect(self.db) as conn:
            cursor = conn.cursor()
            cursor.execute("""DROP TABLE IF EXISTS articles""")

    def insert_article(self, data):
        """Inserts an article into the 'articles' table.
        
        Args:
            data (Dict[str, str]): A dictionary containing the following keys:
                - 'header' (str): The article header.
                - 'newspaper' (str): The newspaper name.
                - 'article_url' (str): The URL of the article.
                - 'article' (str): The full article text.
        
        Prints:
            sqlite3.DatabaseError: If a database error occurs during the insertion.
        """

        try:

            with sqlite3.connect('news.db') as conn:
                # Create a cursor object using the context manager
                cursor = conn.cursor()
                cursor.execute("""INSERT OR IGNORE INTO articles 
                               
                            (event_datetime, header, newspaper, 
                            url, article)
                               
                            VALUES 
                               
                            (:event_datetime, :header, :newspaper,
                            :url, :article)""",
                            (data))
            print(f"Success inserting article: {data['header']}")

        except Exception as e:
            print(f"The following Error occured: {e}")

    def get_articles_rows(self, query):
        """Gets rows from articles table based on query"""
        try:
            with sqlite3.connect('news.db') as conn:
                cursor = conn.cursor()
                cursor.execute(query)
                rows = cursor.fetchall()
                return rows
        except Exception as e:
            print(f"The following error occured: {e}")


class EmbeddingWrapper:
    def __init__(self):
        self.db = 'news.db'
        self._create_table()
    
    def _create_table(self):
        """Create embeddings table with (id, embedding vector)"""
        
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

    def insert_embedding(self, header, article, embeddings):
        """Inserts embedding into table"""

        query = """
                INSERT OR IGNORE INTO embeddings 
                (header, article, embedding) VALUES (?, ?, ?)
                """
    
        with sqlite3.connect(self.db) as conn:
            cursor = conn.cursor()
            cursor.execute(query, (header, article, pickle.dumps(embeddings)))
    
    def get_embedding(self, query):
        with sqlite3.connect(self.db) as conn:
            cursor = conn.cursor()
            cursor.execute(query)
            rows = cursor.fetchall()
        
        result = []
        for row in rows:
            print(row[0], row[1])
            embed = pickle.loads(row[2])
            result.append((row, embed))
        
        return result
