import sqlite3

class FumigationDB:
    def __init__(self, db_path='fumigation_services.db'):
        self.db_path = db_path
        self.conn = sqlite3.connect(self.db_path)
        self.conn.row_factory = sqlite3.Row
        self.setup_table()

    def setup_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS appointments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_name TEXT NOT NULL,
            service_type TEXT NOT NULL,
            appointment_date TEXT NOT NULL,
            notes TEXT
        );
        '''
        self.conn.execute(query)
        self.conn.commit()

    def add_appointment(self, customer_name, service_type, appointment_date, notes):
        query = '''
        INSERT INTO appointments (customer_name, service_type, appointment_date, notes)
        VALUES (?, ?, ?, ?)
        '''
        self.conn.execute(query, (customer_name, service_type, appointment_date, notes))
        self.conn.commit()

    def get_appointments(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM appointments")
        return cursor.fetchall()

    def close(self):
        self.conn.close()
