import sqlite3
import threading

class DatabaseManager:
    def __init__(self, db_path='my_database.db'):
        self.db_path = db_path
        self.conn = sqlite3.connect(self.db_path, check_same_thread=False)
        self.thread_local = threading.local()

    def get_cursor(self):
        """Ensure each thread has its own cursor."""
        if not hasattr(self.thread_local, 'cursor'):
            # Create a new cursor for this thread if it doesn't already have one
            self.thread_local.cursor = self.conn.cursor()
        return self.thread_local.cursor

    def create_table(self):
        """Create a USERS table if it doesn't already exist."""
        cursor = self.get_cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS USERS (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                email TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL
            );
        ''')
        self.conn.commit()

    def insert_user(self, username, email, password):
        """Insert a new user into the USERS table."""
        cursor = self.get_cursor()
        try:
            cursor.execute("INSERT INTO USERS (username, email, password) VALUES (?, ?, ?)", (username, email, password))
            self.conn.commit()
            return "User registered successfully."
        except sqlite3.IntegrityError as e:
            return f"Error registering user: {e}"

    def validate_user(self, username, password):
        """Validate a user's credentials."""
        cursor = self.get_cursor()
        cursor.execute("SELECT password FROM USERS WHERE username = ?", (username,))
        result = cursor.fetchone()
        if result and result[0] == password:
            return True
        return False

    def close(self):
        """Close the cursor and connection when done."""
        if hasattr(self.thread_local, 'cursor'):
            self.thread_local.cursor.close()
            del self.thread_local.cursor
        self.conn.close()
