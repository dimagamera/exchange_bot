import requests
import sqlite3


def into():
    conn = sqlite3.connect('database/database.db', check_same_thread=False)
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS `currencly` (`currencly` STRING, `course` REAL)")
    r  = requests.get('https://openexchangerates.org/api/latest.json?app_id=dd0cdb5c177f4d1e8537175f1b6852a6').json()
    UAH =  r['rates']['UAH']
    UAH = '%.2f' % UAH
    RUB =  r['rates']['RUB']
    RUB = '%.2f' % RUB
    CAD =  r['rates']['CAD']
    CAD = '%.2f' % CAD
    conn = sqlite3.connect('database/database.db', check_same_thread=False)
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO currency VALUES ('UAH', {UAH})")
    conn.commit()
    cursor.execute(f"INSERT INTO currency VALUES ('RUB', {RUB})")
    conn.commit()
    cursor.execute(f"INSERT INTO currency VALUES ('CAD', {CAD})")
    conn.commit()


def show():
    conn = sqlite3.connect('database/database.db', check_same_thread=False)
    cursor = conn.cursor()
    rows = cursor.execute("SELECT * FROM currency").fetchall()
    print(rows)
    return rows

def update():
    conn = sqlite3.connect('database/database.db', check_same_thread=False)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM currency")
    conn.commit()

def find(currency):
    conn = sqlite3.connect('database/database.db', check_same_thread=False)
    cursor = conn.cursor()
    curenc = cursor.execute(f"SELECT * FROM currency WHERE currency = '{currency}' ").fetchall()
    return curenc