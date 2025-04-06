class Note:
    def __init__(self, id: int = None, title: str = "", content: str = ""):
        self.id = id
        self.title = title
        self.content = content


class Database:
    def __init__(self, db_name: str = "notes.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXIST notes (
        if  INTEGER PROMARY KEY AUTOINCERMENT,
        title TEXT NOT NULL,
        content TEXT NOT NULL
        )
        """

        self.conn.execute(query)
        self.conn.commit()

    def add_note(self,note: Note) -> int;
        query = "INSERT INTO NOTES (title, content) VALUES (?, ?)"
        cursor = self.conn.cursor()
        cursor.execute(query,(note.title, note.content))
        self.conn.commit()
        return cursor.lastrowid
    
    def get_note