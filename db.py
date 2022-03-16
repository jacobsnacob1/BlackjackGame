from objects import Session
import sqlite3
from contextlib import closing

conn = None


def connect():
    global conn
    if not conn:
        global DB_FILE
        DB_FILE = "session_db.sqlite"
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row


def close():
    if conn:
        conn.close()


def make_session(row):
    return Session(row["sessionID"], row["startTime"], row["startMoney"], row["stopTime"], row["stopMoney"])


def create_session():
    c = conn.cursor()
    with closing(conn.cursor()) as c:
        c.execute('''CREATE TABLE IF NOT EXISTS Session 
                    (sessionID INTEGER PRIMARY KEY, 
                    startTime TEXT, 
                    startMoney REAL, 
                    stopTime TEXT, 
                    stopMoney REAL)''')
        conn.commit()

    getL = get_last_session()
    if not getL:
        query = '''INSERT INTO Session (sessionID, startTime, startMoney, stopTime, stopMoney)
                            VALUES (0, 'x', 199, 'y', 199);'''
        with closing(conn.cursor()) as c:
            c.execute(query)
        conn.commit()
    else:
        pass


def get_last_session():
    query = '''SELECT * FROM Session ORDER BY sessionID DESC;'''
    with closing(conn.cursor()) as c:
        c.execute(query)
        results = c.fetchone()
        session = make_session(results)
        return session


def add_session(s):
    query = '''INSERT INTO Session (sessionID, startTime, startMoney, stopTime, stopMoney) 
                    VALUES (?, ?, ?, ?, ?)'''
    with closing(conn.cursor()) as c:
        c.execute(query, (s.sessionID, s.startTime, s.startMoney, s.stopTime, s.stopMoney))
        conn.commit()
    return

def start():
    connect()
    create_session()
    global money
    money = get_last_session()
    return money.stopMoney


