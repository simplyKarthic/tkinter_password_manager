import sqlite3


def connect():
    connection = sqlite3.connect("passwords.db")
    cursor = connection.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS passwords (id INTEGER PRIMARY KEY, website VARCHAR, email VARCHAR, username VARCHAR, passed PASSWORD)")
    connection.commit()
    connection.close()


def insert(website, email, username, passed):
    connection = sqlite3.connect("passwords.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO passwords VALUES(NULL,?,?,?,?)",
                   (website, email, username, passed))
    connection.commit()
    connection.close()


def view():
    connection = sqlite3.connect("passwords.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM passwords")
    rows = cursor.fetchall()
    connection.close()
    return rows


def search(website="", email="", username="", passed=""):
    connection = sqlite3.connect("passwords.db")
    cursor = connection.cursor()
    cursor.execute(
        "SELECT * FROM passwords WHERE website= ? OR email =? OR username= ? OR passed= ?", (website, email, username, passed))
    rows = cursor.fetchall()
    connection.close()
    return rows


def delete(id):
    connection = sqlite3.connect("passwords.db")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM passwords WHERE id=?", (id,))
    connection.commit()
    connection.close()


def update(id, website, email, username, passed):
    connection = sqlite3.connect("passwords.db")
    cursor = connection.cursor()
    cursor.execute("UPDATE passwords SET website= ?, email =?, username= ?, passed= ? WHERE id = ?",
                   (website, email, username, passed, id))
    connection.commit()
    connection.close()


connect()
