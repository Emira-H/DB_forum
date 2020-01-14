from connection import Connection

class MessageModel:

    def __init__(self):
        self.db = Connection()
        self.author = None
        self.content = None
        self.publishing_date = None

    def write_message(self, author, content):
        self.db.initialize_connection()
        self.db.cursor.execute("INSERT INTO message (author, pusblishing_date, content) VALUES (%s, NOW(),%s);", self.author, self.publishing_date, self.content)
        self.db.close_connection()

    def get_message(self):
        self.db.initialize_connection()
        self.db.cursor.execute("SELECT * FROM message ;")
        messages = self.db.cursor.fetchall()
        self.db.close_connection()
        return messages
