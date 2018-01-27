import sqlite3

conn = sqlite3.connect("appdb.db")

def create_tables():
    cursor = conn.cursor()
    conn.text_factory = str
    cursor.execute('PRAGMA foreign_keys=ON')

    cursor.execute("""CREATE TABLE IF NOT EXISTS emotionList(
        emotion TEXT PRIMARY KEY
        );""")

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(
        user_id INTEGER PRIMARY KEY,
        username TEXT,
        password TEXT,
        contactName TEXT,
        contactNumber INTEGER,
        relationToContact TEXT
        );""")

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS userEmotion(
        row_id INTEGER PRIMARY KEY,
        user_id INTEGER,
        emotion TEXT,
        emotionDate TEXT,
        FOREIGN KEY (user_id) REFERENCES users(user_id),
        FOREIGN KEY (emotion) REFERENCES emotionList(emotion)
        );""")

    conn.commit()


def insert_into_users(username, password, contactName, contactNumber, relationToContact):
    cursor = conn.cursor()
    conn.text_factory = str
    cursor.execute('PRAGMA foreign_keys=ON')

    cursor.execute("INSERT OR REPLACE INTO users (username, password, contactName, contactNumber, relationToContact) VALUES ('{0}', '{1}', '{2}', {3}, '{4}')"
                   .format(username, password, contactName, contactNumber, relationToContact))
    conn.commit()

def insert_into_userEmotion(user_id, emotion, emotionDate):
    cursor = conn.cursor()
    conn.text_factory = str
    cursor.execute('PRAGMA foreign_keys=ON')

    cursor.execute(
        "INSERT OR REPLACE INTO users (user_id, emotion, emotionDate) VALUES ({0}, '{1}', '{2}')"
        .format(user_id, emotion, emotionDate))
    conn.commit()


