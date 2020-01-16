from .connection import Connection

class MessageModel:
    '''class to execute SQL statements'''
    def __init__(self):
        self.db = Connection()
    # The class requires an instance of Connection to execute SQL statements


    def write_message(self, author, content):
        '''Methode that requires 2 arguments (author and content) and a to update the table message by
        adding a row with the corresponding informations '''
        # first, we call the method to connect to the DB and use the cursor in this one
        # we execute the SQL request to add a row with the informations in the table message
        # In order to commit all changes to the PostgreSQL database permanently, we call the commit() method .
        # At the end, we close both connection and cursor by calling the method close_connection from class Connection
        self.db.initialize_connection()
        self.db.cursor.execute("INSERT INTO message (author, publishing_date, content) VALUES (%s, NOW(),%s);",(author, content))
        self.db.connection.commit()
        self.db.close_connection()

    def get_message(self):
        ''' Methode to '''
        self.db.initialize_connection()
        self.db.cursor.execute("SELECT * FROM message ;")
        messages = self.db.cursor.fetchall()
        self.db.close_connection()
        return messages
