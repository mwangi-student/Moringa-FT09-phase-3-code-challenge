from database.connection import get_db_connection
conn = get_db_connection()

class Article:
    def __init__(self, author, magazine, title):
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("Title must be between 5 and 50 characters.")
        if not isinstance(author.id, int) or not isinstance(magazine.id, int):
            raise ValueError("Author and Magazine must have valid IDs.")
        
        self._title = title
        self._author_id = author.id
        self._magazine_id = magazine.id

        # Insert into the database
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO articles (title, author_id, magazine_id) VALUES (?, ?, ?)",
            (title, self._author_id, self._magazine_id)
        )
        conn.commit()
        self._id = cur.lastrowid

    @property
    def title(self):
        return self._title
