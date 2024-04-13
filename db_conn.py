from pathlib import Path
import sqlite3
import sys
import sqlite3
from pathlib import Path
class DB:
    @staticmethod
    def loadSqlScript(filepath: str) -> str:
        content = ""
        try:
            file =  open(filepath, 'r', encoding='UTF-8')
            content = file.read()
        except FileNotFoundError:
            print(f"Failed to read '{filepath}' file.")
            sys.exit(-1)
        return content
    @staticmethod
    def initializeDB() -> None:
        DB_FILEPATH1 = Path('./match_history.sql')
        script = DB.loadSqlScript(DB_FILEPATH1)
        DB_FILEPATH2 = Path('./news.db')
        DB_CONN = sqlite3.connect(DB_FILEPATH2)
        cursor = DB_CONN.cursor()
        cursor.executescript(script)
        DB_CONN.commit()
        cursor.close()
if __name__ == "__main__":
    DB.initializeDB()
    

