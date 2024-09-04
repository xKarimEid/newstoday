"""
Wrapper around articles table
"""

import sqlite3


class ArticlesWrapper:
    def __init__(self):
        self.db = 'news.db'
        self._create_articles_table()

    def _create_articles_table(self):
        """Create articles table if it doesnt exists"""

        with sqlite3.connect(self.db) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS articles
                (article_id INTEGER PRIMARY KEY, 
                header TEXT UNIQUE,
                newspaper text, 
                url text UNIQUE,
                article text NOT NULL)
                ''')

    def drop_articles_table(self):
        """Drop articles table if it exists"""

        with sqlite3.connect(self.db) as conn:
            cursor = conn.cursor()
            cursor.execute("""DROP TABLE IF EXISTS articles""")

    def insert_article(self, header, newspaper, url, article):
        """Inserts article into articles table"""

        try:

            with sqlite3.connect('news.db') as conn:
                # Create a cursor object using the context manager
                cursor = conn.cursor()
                cursor.execute("""INSERT OR IGNORE INTO articles 
                            (header, newspaper, url, article)
                            VALUES 
                            (?, ?, ?, ?)""",
                            (header, newspaper, url, article))
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