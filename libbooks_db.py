"""
Initialize Database.

====================

Database: libbooks_db
"""

import sqlite3


def connect_data():
    conn = sqlite3.connect('libbooks.db')
    curs = conn.cursor()
    curs.execute('CREATE TABLE IF NOT EXISTS libbooks (id INTEGER PRIMARY KEY, Mty text, Tit text, Fname text, Sname text, Adr1, Adr2 text, Pscd text, MNo text, BkID text, BkTit text, Auth text, DBo text, Dtd text, sPr text, LrF text, DoD text, DonL text)')
    conn.commit()
    conn.close()


def add_data_record(Mty, Tit, Fname, Sname, Adr1, Adr2, Pscd, MNo, BkID, BkTit, Auth, DBo, Dtd, sPr, LrF, DoD, DonL):
    conn = sqlite3.connect('libbooks.db')
    curs = conn.cursor()
    curs.execute('INSERT INTO libbooks VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                 (Mty, Tit, Fname, Sname, Adr1, Adr2, Pscd, MNo, BkID, BkTit, Auth, DBo, Dtd, sPr, LrF, DoD, DonL))
    conn.commit()
    conn.close()


connect_data()
