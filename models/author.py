from database.connection import get_db_connection
conn = get_db_connection()

class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string.")
        
        self._name = name
        
        # Insert into the database and retrieve the ID
        cur = conn.cursor()
        cur.execute("INSERT INTO authors (name) VALUES (?)", (name,))
        conn.commit()
        self._id = cur.lastrowid

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name
    
    def articles(self):
        cur = conn.cursor()
        cur.execute("SELECT * FROM articles WHERE author_id = ?", (self._id,))
        return cur.fetchall()

    def magazines(self):
        cur = conn.cursor()
        cur.execute("""
            SELECT DISTINCT magazines.* FROM magazines
            JOIN articles ON magazines.id = articles.magazine_id
            WHERE articles.author_id = ?
        """, (self._id,))
        return cur.fetchall()

