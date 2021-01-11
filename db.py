import sqlite3

db = sqlite3.connect('TODO.db')
cursor = db.cursor()
cursor.execute('create table TODO('
               'serial INTEGER PRIMARY KEY AUTOINCREMENT,'
               'item_description TEXT, '
               'time TEXT)')
