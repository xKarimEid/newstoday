"""
Wrapper around news.db
"""

import sqlite3


class SQLiteNews:
    def __init__(self):
        self.db = 'news.db'
        self._create_tables()

    def _create_tables(self):
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

    def insert_article(self, header, newspaper, url, article):
        with sqlite3.connect('news.db') as conn:
            # Create a cursor object using the context manager
            cursor = conn.cursor()
            cursor.execute("""INSERT OR IGNORE INTO articles 
                           (header, newspaper, url, article)
                           VALUES 
                           (?, ?, ?, ?)""",
                          (header, newspaper, url, article))

    def get_rows(self, query):
        with sqlite3.connect('news.db') as conn:
            cursor = conn.cursor()
            cursor.execute(query)
            rows = cursor.fetchall()
            return rows
