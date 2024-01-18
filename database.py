from typing import Optional
import sqlite3 as _sql
from PySide6.QtGui import QPainter, QColor, QPixmap
from PySide6.QtCore import Qt
import datetime as dt
import re

base = 'passwords.db'

class DatabaseDec:
    def __init__(self, func):
        """
        Decorator for all database functions. Keeps everything neat and reduces repeated code.

        :param func: The function being decorated.
        """
        self.func = func

    def __call__(self,
                 dbname: str,
                 *args):
        """
        Wrapper function.

        :param dbname: The database to be edited.
        :param args: The parameters of the database query.
        """
        con = _sql.connect(dbname)
        cur = con.cursor()
        ages = cur.execute('''SELECT Used_For, Last_Updated FROM Passwords''').fetchall()
        for age in ages:
            try:
                if abs(dt.datetime.now().timestamp() - int(age[[1]])) > 2592000:
                    print(f'Change your {age[0]} password.')
            except:
                raise ValueError(f'Date of last update for {age[0]} has not been formatted correctly.')
        if isinstance(self.func(*args), tuple):
            data = cur.execute(*(self.func(*args))).fetchall()
        else:
            data = cur.execute(self.func(*args)).fetchall()
        con.commit()
        con.close()
        return data


@DatabaseDec
def create_table():
    return """ CREATE TABLE Passwords(
            Used_For VARCHAR(255) NOT NULL,
            Ciphertext VARCHAR(255) NOT NULL, 
            Last_Updated DATE NOT NULL 
        ); """


@DatabaseDec
def insert_password(uf, ct):
    lu = int(dt.datetime.now().timestamp())
    return '''INSERT INTO Passwords (Used_For, Ciphertext, Last_Updated) VALUES (?, ?, ?) ''', (uf.lower(), ct, lu)

@DatabaseDec
def test_cases(uf, ct, lu):
    return '''INSERT INTO Passwords (Used_For, Ciphertext, Last_Updated) VALUES (?, ?, ?) ''', (uf.lower(), ct, lu)

@DatabaseDec
def delete_table():
    return '''DROP TABLE Passwords'''

@DatabaseDec
def get_ciphertext(uf: str):
    return '''SELECT Ciphertext FROM Passwords WHERE Used_For = ?''', (uf.lower(),)

@DatabaseDec
def ageing_check():
    return '''SELECT Used_For, Last_Updated FROM Passwords'''

@DatabaseDec
def update_password(uf: str, ct: str):
    lu = int(dt.datetime.now().timestamp())
    return '''UPDATE Passwords SET Ciphertext = ?, Last_Updated = ? WHERE Used_For = ?''', (ct, lu, uf)

def reset_table():
    delete_table(base)
    create_table(base)

# Additional Functions.

def change_opacity(pixmap, opacity):
    new_pixmap = QPixmap(pixmap.size())
    new_pixmap.fill(Qt.transparent)

    painter = QPainter(new_pixmap)
    painter.setOpacity(opacity)
    painter.drawPixmap(0, 0, pixmap)
    painter.end()

    return new_pixmap

