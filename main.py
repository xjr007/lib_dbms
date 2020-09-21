"""
Library Databse Management System.

=================================

Basic CRUD from sqLite with Python
"""

import tkinter as tk


class Library:
    """
    Super class.

    ===========
    class - Library
    """

    def __init__(self, master):
        """
        Create constructor.

        ==================

        Initialize main window
        """
        self.master = master
        master.title("Library Database Management System")
        master.geometry("1350x750+0+0")

        Mty = tk.StringVar()
        Ref = tk.StringVar()
        Tit = tk.StringVar()
        Fname = tk.StringVar()
        Sname = tk.StringVar()
        Adr1 = tk.StringVar()
        Adr2 = tk.StringVar()
        pcd = tk.StringVar()
        MNo = tk.StringVar()
        BkID = tk.StringVar()
        BkTit = tk.StringVar()
        Auth = tk.StringVar()
        DBo = tk.StringVar()
        Dtd = tk.StringVar()
        sPr = tk.StringVar()
        LrF = tk.StringVar()
        DoD = tk.StringVar()
        DonL = tk.StringVar()

# ==========================================Frames================================================ #

# Main Frame
        main_frame = tk.Frame(master)
        main_frame.grid()

# Title Frame
        tit_frame = tk.Frame(main_frame, bd=2, padx=40, pady=8, bg="cadet blue", relief=tk.RIDGE)

        tit_frame.pack(side=tk.TOP)

        self.lbl_tit = tk.Label(tit_frame, font=('arial', 46, 'bold'),
                                text='Library Database Management System')
        self.lbl_tit.grid(sticky=tk.W)

# Button Frame
        button_frame = tk.Frame(main_frame, bd=2, width=1350, height=100, padx=20, pady=20,
                                bg="cadet blue", relief=tk.RIDGE)
        button_frame.pack(side=tk.BOTTOM)

        frame_detail = tk.Frame(main_frame, bd=0, width=1350, height=50, padx=20, relief=tk.RIDGE)
        frame_detail.pack(side=tk.BOTTOM)

# Data Frame
        data_frame = tk.Frame(main_frame, bd=1, width=1350, height=400, padx=20, pady=20,
                              relief=tk.RIDGE)
        data_frame.pack(side=tk.BOTTOM)
# Children of the 'Data' Frame:
# - data_frame_right
        data_frame_left = tk.LabelFrame(data_frame, bd=1, width=800, height=300, padx=20,
                                        font=('arial', 12, 'bold'), text="Library Membership Info:",
                                        bg='cadet blue', relief=tk.RIDGE)
        data_frame_left.pack(side=tk.LEFT)

# - data_frame_right
        data_frame_right = tk.LabelFrame(data_frame, bd=1, width=450, height=300, padx=20, pady=3,
                                         font=('arial', 12, 'bold'), text="Book Details:",
                                         bg='cadet blue', relief=tk.RIDGE)
        data_frame_right.pack(side=tk.RIGHT)

# ======================================Label and Entry=========================================== #

# Member Type
        self.lbl_member_type = tk.Label(data_frame_left, font=('arial', 12, 'bold'),
                                        text='Member Type', padx=2, pady=2, bg='cadet blue')
        self.lbl_member_type.grid(row=0, column=0, sticky=tk.W)

        self.txt_member_type = tk.Entry(data_frame_left, font=('arial', 12, 'bold'),
                                        textvariable=Mty, width=25)
        self.txt_member_type.grid(row=0, column=1)

# Reference
        self.lbl_ref = tk.Label(data_frame_left, font=('arial', 12, 'bold'),
                                text='Reference Number:', padx=2, pady=2, bg='cadet blue')
        self.lbl_ref.grid(row=0, column=2, sticky=tk.W)

        self.txt_ref = tk.Entry(data_frame_left, font=('arial', 12, 'bold'), textvariable=Ref,
                                width=25)
        self.txt_ref.grid(row=0, column=3)

# Book ID
        self.lbl_bk_id = tk.Label(data_frame_left, font=('arial', 12, 'bold'),
                                  text='Book ID:', padx=2, pady=2, bg='cadet blue')
        self.lbl_bk_id.grid(row=1, column=0, sticky=tk.W)

        self.txt_bk_id = tk.Entry(data_frame_left, font=('arial', 12, 'bold'), textvariable=BkID,
                                  width=25)
        self.txt_bk_id.grid(row=1, column=1)

# Book title
        self.lbl_bk_tit = tk.Label(data_frame_left, font=('arial', 12, 'bold'), text='Book Title:',
                                   padx=2, pady=2, bg='cadet blue')
        self.lbl_bk_tit.grid(row=1, column=2, sticky=tk.W)

        self.txt_bk_tit = tk.Entry(data_frame_left, font=('arial', 12, 'bold'), textvariable=BkTit,
                                   width=25)
        self.txt_bk_tit.grid(row=1, column=3)

# Title
        self.lbl_tit = tk.Label(data_frame_left, font=('arial', 12, 'bold'), text='Title:', padx=2,
                                pady=2, bg='cadet blue')
        self.lbl_tit.grid(row=2, column=0, sticky=tk.W)

        self.txt_tit = tk.Entry(data_frame_left, font=('arial', 12, 'bold'), textvariable=Tit,
                                width=25)
        self.txt_tit.grid(row=2, column=1)

# Author
        self.lbl_auth = tk.Label(data_frame_left, font=('arial', 12, 'bold'), text='Author:', padx=2
                                 , pady=2, bg='cadet blue')
        self.lbl_auth.grid(row=2, column=2, sticky=tk.W)

        self.txt_auth = tk.Entry(data_frame_left, font=('arial', 12, 'bold'), textvariable=Auth,
                                 width=25)
        self.txt_auth.grid(row=2, column=3)

# First Name
        self.lbl_fname = tk.Label(data_frame_left, font=('arial', 12, 'bold'), text='Name:', padx=2,
                                  pady=2, bg='cadet blue')
        self.lbl_fname.grid(row=3, column=0, sticky=tk.W)

        self.txt_fname = tk.Entry(data_frame_left, font=('arial', 12, 'bold'), textvariable=Fname,
                                  width=25)
        self.txt_fname.grid(row=3, column=1)

# Date Borrowed
        self.lbl_dt_brw = tk.Label(data_frame_left, font=('arial', 12, 'bold'),
                                   text='Date Borrowed:', padx=2, pady=2, bg='cadet blue')
        self.lbl_dt_brw.grid(row=3, column=2, sticky=tk.W)

        self.txt_dt_brw = tk.Entry(data_frame_left, font=('arial', 12, 'bold'), textvariable=DBo,
                                   width=25)
        self.txt_dt_brw.grid(row=3, column=3)

# Surname
        self.lbl_sname = tk.Label(data_frame_left, font=('arial', 12, 'bold'), text='Surname:',
                                  padx=2, pady=2, bg='cadet blue')
        self.lbl_sname.grid(row=4, column=0, sticky=tk.W)

        self.txt_sname = tk.Entry(data_frame_left, font=('arial', 12, 'bold'), textvariable=Sname,
                                  width=25)
        self.txt_sname.grid(row=4, column=1)

# Due Date
        self.lbl_dt_due = tk.Label(data_frame_left, font=('arial', 12, 'bold'), text='Due Date:',
                                   padx=2, pady=2, bg='cadet blue')
        self.lbl_dt_due.grid(row=4, column=2, sticky=tk.W)

        self.txt_dt_due = tk.Entry(data_frame_left, font=('arial', 12, 'bold'), textvariable=Dtd,
                                   width=25)
        self.txt_dt_due.grid(row=4, column=3)

# Address 1
        self.lbl_address_1 = tk.Label(data_frame_left, font=('arial', 12, 'bold'), text='Address 1:'
                                      , padx=2, pady=2, bg='cadet blue')
        self.lbl_address_1.grid(row=5, column=0, sticky=tk.W)

        self.txt_adress_1 = tk.Entry(data_frame_left, font=('arial', 12, 'bold'), textvariable=Adr1,
                                     width=25)
        self.txt_adress_1.grid(row=5, column=1)

# Address 2
        self.lbl_adress_2 = tk.Label(data_frame_left, font=('arial', 12, 'bold'), text='Address 2:',
                                     padx=2, pady=2, bg='cadet blue')
        self.lbl_adress_2.grid(row=5, column=2, sticky=tk.W)

        self.txt_address_2 = tk.Entry(data_frame_left, font=('arial', 12, 'bold'), textvariable=Adr2
                                      , width=25)
        self.txt_address_2.grid(row=5, column=3)

# Days on Loan
        self.lbl_days_on_loan = tk.Label(data_frame_left, font=('arial', 12, 'bold'),
                                         text='Days on Loan:', padx=2, pady=2, bg='cadet blue')
        self.lbl_days_on_loan.grid(row=6, column=0, sticky=tk.W)

        self.txt_days_on_loan = tk.Entry(data_frame_left, font=('arial', 12, 'bold'),
                                         textvariable=DonL, width=25)
        self.txt_days_on_loan.grid(row=6, column=1)
# ======================================Initialization============================================ #


if __name__ == '__main__':
    root = tk.Tk()
    application = Library(root)
    root.mainloop()
