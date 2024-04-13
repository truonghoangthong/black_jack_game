import sqlite3
from pathlib import Path
import csv

class NoteDAO:
    @staticmethod
    def addNote(win: int, lose: int, tie: int) -> None:
        try :
            DB_FILEPATH = Path('./news.db')
            DB_CONN = sqlite3.connect(DB_FILEPATH)
            cur = DB_CONN.cursor()
            cur.execute("INSERT INTO history VALUES (NULL, ?, ?, ?)",(win, lose, tie))
            DB_CONN.commit()
        except Exception :
            print("Error while inserting note.")
    
    def write_csv():
        DB_FILEPATH = Path('./news.db')
        DB_CONN = sqlite3.connect(DB_FILEPATH)
        cur = DB_CONN.cursor()
        cur.execute('SELECT * FROM history')
        rows = cur.fetchall()
        columns = [column[0] for column in cur.description]
        with open('match_history.csv', 'w', newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(columns)
            csv_writer.writerows(rows)
        DB_CONN.close()