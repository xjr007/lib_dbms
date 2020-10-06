"""
Initialize Database.

====================

Database: libbooks_db
"""

import sqlite3


def connect_data():
    conn = sqlite3.connect('libbooks.db')
    curs = conn.cursor()
    curs.execute('CREATE TABLE IF NOT EXISTS libbooks (id INTEGER PRIMARY KEY, \
    Mty text, Ref text, Tit text, Fname text, Sname text, Adr1, Adr2 text, Pscd \
    text, MNo text, BkID text, BkTit text, Auth text, DBo text, Dtd text, sPr text,\
    LrF text, DoD text, DonL text)')
    conn.commit()
    conn.close()


def add_data_record(*args):
    """
    Add data to database(BACKEND).

    Database: libbooks.db
    """
    conn = sqlite3.connect('libbooks.db')
    curs = conn.cursor()
    curs.execute('INSERT INTO libbooks VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, \
    ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                 (args[0],
                  args[1],
                  args[2],
                  args[3],
                  args[4],
                  args[5],
                  args[6],
                  args[7],
                  args[8],
                  args[9],
                  args[10],
                  args[11],
                  args[12],
                  args[13],
                  args[14],
                  args[15],
                  args[16],
                  args[17]))
    conn.commit()
    conn.close()


def view_data():
    """
    Fetch data from database(BACKEND).

    Database: libbooks.db
    """
    conn = sqlite3.connect('libbooks.db')
    curs = conn.cursor()
    curs.execute('SELECT * FROM libbooks')
    data = curs.fetchall()
    conn.close()
    return data


def delete_record(id_):
    """
    Delete data from database(BACKEND).

    Database: libbooks.db
    """
    conn = sqlite3.connect('libbooks.db')
    curs = conn.cursor()
    curs.execute('DELETE FROM libbooks WHERE id=?', (id_,))
    conn.commit()
    conn.close()


def search_data(Mty='', Ref='', Tit='', Fname='', Sname='', Adr1='', Adr2='',
                Pscd='', MNo='', BkID='', BkTit='', Auth='', DBo='', Dtd='',
                sPr='', LrF='', DoD='', DonL=''):
    """
    Find data in database(BACKEND).

    Database: libbooks.db
    """
    conn = sqlite3.connect('libbooks.db')
    curs = conn.cursor()
    curs.execute('SELECT * FROM libbooks WHERE \
                Mty=?, Ref=?, Tit=?, Fname=?,\
                Sname=?, Adr1=?, Adr2=?, Pscd=?,\
                MNo=?, BkID=?, BkTit=?, Auth=?, \
                DBo=?, Dtd=?, sPr=?, LrF=?, DoD=\
                ?, DonL=?',
                 (Mty, Ref, Tit, Fname,
                  Sname, Adr1, Adr2, Pscd,
                  MNo, BkID, BkTit, Auth, DBo, Dtd,
                  sPr, LrF, DoD, DonL))
    data = curs.fetchall()
    conn.close()
    return data


def update_data(id_, Mty='', Ref='', Tit='', Fname='', Sname='', Adr1='', Adr2='',
                Pscd='', MNo='', BkID='', BkTit='', Auth='', DBo='', Dtd='',
                sPr='', LrF='', DoD='', DonL=''):
    """
    Update data in database(BACKEND).

    Database: libbooks.db
    """
    conn = sqlite3.connect('libbooks.db')
    curs = conn.cursor()
    curs.execute('UPDATE libbooks SET \
                Mty=?, Ref=?, Tit=?, Fname=?,\
                Sname=?, Adr1=?, Adr2=?, Pscd=?,\
                MNo=?, BkID=?, BkTit=?, Auth=?, \
                DBo=?, Dtd=?, sPr=?, LrF=?, DoD=\
                ?, DonL=? WHERE id=?',
                 (Mty, Ref, Tit, Fname,
                  Sname, Adr1, Adr2, Pscd,
                  MNo, BkID, BkTit, Auth, DBo, Dtd,
                  sPr, LrF, DoD, DonL, id_))
    conn.commit()
    conn.close()


connect_data()
