import sqlite3

def create():
    conn = sqlite3.connect("database/DataBase.db")
    cursor = conn.cursor()
    cursor.execute("create table if not exists user (Id integer primary key AUTOINCREMENT ,first_name text,second_name text,age integer,date text,confidence_score real,prediction text)")
    conn.commit()
    conn.close()

def fill(first,second,age,date,conf,prediction):
    conn = sqlite3.connect("database/DataBase.db")
    cursor = conn.cursor()
    cursor.execute("insert into user(first_name,second_name,age,date,confidence_score,prediction) values(?,?,?,?,?,?)",(first,second,age,date,conf,prediction))
    conn.commit()
    conn.close()

def display():
    conn = sqlite3.connect("database/DataBase.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM user")
    data = cursor.fetchall()
    conn.close()
    return data