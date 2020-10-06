"""
Library Databse Management System.

==================================

Basic CRUD from sqLite with Python
"""

import tkinter as tk
import tkinter.messagebox
import libbooks_db

# ==========local===============#


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

        # Member Type
        Mty = tk.StringVar()
        # Reference Number
        Ref = tk.StringVar()
        # Title
        Tit = tk.StringVar()
        # First Name
        Fname = tk.StringVar()
        # Surname
        Sname = tk.StringVar()
        # Adress 1
        Adr1 = tk.StringVar()
        # Adress 2
        Adr2 = tk.StringVar()
        # Postal Code
        Pscd = tk.StringVar()
        # Mobile Number
        MNo = tk.StringVar()
        # Book ID
        BkID = tk.StringVar()
        # Book Title
        BkTit = tk.StringVar()
        # Author
        Auth = tk.StringVar()
        # Date Borrowed
        DBo = tk.StringVar()
        # Date Due
        Dtd = tk.StringVar()
        # Selling Price
        sPr = tk.StringVar()
        # Late Return Fine
        LrF = tk.StringVar()
        # Days over Due
        DoD = tk.StringVar()
        # Days on Loan
        DonL = tk.StringVar()

# ====================================Function Declaration======================================== #

        def i_exit():
            """
            Exit func.

            i_exit() : exits program.
            """
            i_exit = tkinter.messagebox.askyesno("Library Database Management System",
                                                 "Are you sure you want to exit?")
            if i_exit > 0:
                root.destroy()
                return

        def clear_data():
            """
            Clear func.

            clear_data() : clears all form fields.
            """
            self.txt_member_type.delete(0, tk.END)
            self.txt_ref.delete(0, tk.END)
            self.txt_bk_id.delete(0, tk.END)
            self.txt_bk_tit.delete(0, tk.END)
            self.txt_tit.delete(0, tk.END)
            self.txt_auth.delete(0, tk.END)
            self.txt_fname.delete(0, tk.END)
            self.txt_dt_brw.delete(0, tk.END)
            self.txt_sname.delete(0, tk.END)
            self.txt_dt_due.delete(0, tk.END)
            self.txt_address_1.delete(0, tk.END)
            self.txt_address_2.delete(0, tk.END)
            self.txt_days_on_loan.delete(0, tk.END)
            self.txt_late_rtn_fn.delete(0, tk.END)
            self.txt_pstl_cd.delete(0, tk.END)
            self.txt_dt_ovrdue.delete(0, tk.END)
            self.txt_mbl_no.delete(0, tk.END)
            self.txt_sel_pr.delete(0, tk.END)

        def add_data():
            """
            Add data to database.

            Database: libbooks_db
            """
            if len(Mty.get()) != 0:
                libbooks_db.add_data_record(
                    Mty.get(), Ref.get(), Tit.get(), Fname.get(), Sname.get(),
                    Adr1.get(), Adr2.get(), Pscd.get(), MNo.get(), BkID.get(),
                    BkTit.get(), Auth.get(), DBo.get(), Dtd.get(), sPr.get(),
                    LrF.get(), DoD.get(), DonL.get())

                booklist.delete(0, tk.END)
                booklist.insert(tk.END,
                                Mty.get(), Ref.get(), Tit.get(), Fname.get(), Sname.get(),
                                Adr1.get(), Adr2.get(), Pscd.get(), MNo.get(), BkID.get(),
                                BkTit.get(), Auth.get(), DBo.get(), Dtd.get(), sPr.get(),
                                LrF.get(), DoD.get(), DonL.get())

        def display_data():
            """
            Display data from database.

            Database: libbooks_db
            """
            booklist.delete(0, tk.END)
            for row in libbooks_db.view_data():
                booklist.insert(tk.END, row)

        def selected_book(e):
            global book
            search_book = booklist.curselection()[0]
            book = booklist.get(search_book)

            self.txt_member_type.delete(0, tk.END)
            self.txt_member_type.insert(tk.END, book[1])
            self.txt_ref.delete(0, tk.END)
            self.txt_ref.insert(tk.END, book[2])
            self.txt_bk_id.delete(0, tk.END)
            self.txt_bk_id.insert(tk.END, book[3])
            self.txt_bk_tit.delete(0, tk.END)
            self.txt_bk_tit.insert(tk.END, book[4])
            self.txt_tit.delete(0, tk.END)
            self.txt_tit.insert(tk.END, book[5])
            self.txt_auth.delete(0, tk.END)
            self.txt_auth.insert(tk.END, book[6])
            self.txt_fname.delete(0, tk.END)
            self.txt_fname.insert(tk.END, book[7])
            self.txt_dt_brw.delete(0, tk.END)
            self.txt_dt_brw.insert(tk.END, book[8])
            self.txt_sname.delete(0, tk.END)
            self.txt_sname.insert(tk.END, book[9])
            self.txt_dt_due.delete(0, tk.END)
            self.txt_dt_due.insert(tk.END, book[10])
            self.txt_address_1.delete(0, tk.END)
            self.txt_address_1.insert(tk.END, book[11])
            self.txt_address_2.delete(0, tk.END)
            self.txt_address_2.insert(tk.END, book[12])
            self.txt_days_on_loan.delete(0, tk.END)
            self.txt_days_on_loan.insert(tk.END, book[13])
            self.txt_late_rtn_fn.delete(0, tk.END)
            self.txt_late_rtn_fn.insert(tk.END, book[14])
            self.txt_pstl_cd.delete(0, tk.END)
            self.txt_pstl_cd.insert(tk.END, book[15])
            self.txt_dt_ovrdue.delete(0, tk.END)
            self.txt_dt_ovrdue.insert(tk.END, book[16])
            self.txt_mbl_no.delete(0, tk.END)
            self.txt_mbl_no.insert(tk.END, book[17])
            self.txt_sel_pr.delete(0, tk.END)
            self.txt_sel_pr.insert(tk.END, book[18])

        def delete_record():
            if len(Mty.get()) != 0:
                libbooks_db.delete_record(book[0])
                clear_data()
                display_data()

        def search_data():
            usr_data = libbooks_db.search_data(Mty.get(), Ref.get(), Tit.get(),
                                               Fname.get(), Sname.get(),
                                               Adr1.get(), Adr2.get(),
                                               Pscd.get(), MNo.get(),
                                               BkID.get(), BkTit.get(),
                                               Auth.get(), DBo.get(),
                                               Dtd.get(), sPr.get(),
                                               LrF.get(), DoD.get(), DonL.get())
            booklist.delete(0, tk.END)
            for record in usr_data:
                booklist.insert(tk.END, record)

        def update_data():
            if len(Mty.get()) != 0:
                libbooks_db.update_data(Mty.get(), Ref.get(), Tit.get(),
                                        Fname.get(), Sname.get(),
                                        Adr1.get(), Adr2.get(),
                                        Pscd.get(), MNo.get(),
                                        BkID.get(), BkTit.get(),
                                        Auth.get(), DBo.get(),
                                        Dtd.get(), sPr.get(),
                                        LrF.get(), DoD.get(), DonL.get())

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
        self.lbl_auth = tk.Label(data_frame_left, font=('arial', 12, 'bold'),
                                 text='Author:', padx=2, pady=2, bg='cadet blue')
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
        self.lbl_address_1 = tk.Label(data_frame_left, font=('arial', 12, 'bold'),
                                      text='Address 1:', padx=2, pady=2, bg='cadet blue')
        self.lbl_address_1.grid(row=5, column=0, sticky=tk.W)

        self.txt_address_1 = tk.Entry(data_frame_left, font=('arial', 12, 'bold'),
                                      textvariable=Adr1, width=25)
        self.txt_address_1.grid(row=5, column=1)

# Address 2
        self.lbl_address_2 = tk.Label(data_frame_left, font=(
            'arial', 12, 'bold'), text='Address 2:', padx=2, pady=2, bg='cadet blue')
        self.lbl_address_2.grid(row=5, column=2, sticky=tk.W)

        self.txt_address_2 = tk.Entry(data_frame_left, font=(
            'arial', 12, 'bold'), textvariable=Adr2, width=25)
        self.txt_address_2.grid(row=5, column=3)

# Days on Loan
        self.lbl_days_on_loan = tk.Label(data_frame_left, font=('arial', 12, 'bold'),
                                         text='Days on Loan:', padx=2, pady=2, bg='cadet blue')
        self.lbl_days_on_loan.grid(row=6, column=0, sticky=tk.W)

        self.txt_days_on_loan = tk.Entry(data_frame_left, font=('arial', 12, 'bold'),
                                         textvariable=DonL, width=25)
        self.txt_days_on_loan.grid(row=6, column=1)

# Late Return Fine
        self.lbl_late_rtn_fn = tk.Label(data_frame_left, font=('arial', 12, 'bold'),
                                        text='Late Return Fine:', padx=2, pady=2, bg='cadet blue')
        self.lbl_late_rtn_fn.grid(row=6, column=2, sticky=tk.W)

        self.txt_late_rtn_fn = tk.Entry(data_frame_left, font=('arial', 12, 'bold'),
                                        textvariable=LrF, width=25)
        self.txt_late_rtn_fn.grid(row=6, column=3)

# Postal Code
        self.lbl_pstl_cd = tk.Label(data_frame_left, font=('arial', 12, 'bold'),
                                    text='Postal Code:', padx=2,
                                    pady=2, bg='cadet blue')
        self.lbl_pstl_cd.grid(row=7, column=0, sticky=tk.W)

        self.txt_pstl_cd = tk.Entry(data_frame_left, font=('arial', 12, 'bold'),
                                    textvariable=Pscd, width=25)
        self.txt_pstl_cd.grid(row=7, column=1)

# Date Overdue
        self.lbl_dt_ovrdue = tk.Label(data_frame_left, font=('arial', 12, 'bold'),
                                      text='Date Overdue:', padx=2, pady=2, bg='cadet blue')
        self.lbl_dt_ovrdue.grid(row=7, column=2, sticky=tk.W)

        self.txt_dt_ovrdue = tk.Entry(data_frame_left, font=('arial', 12, 'bold'),
                                      textvariable=DoD, width=25)
        self.txt_dt_ovrdue.grid(row=7, column=3)

# Mobile Number
        self.lbl_mbl_no = tk.Label(data_frame_left, font=('arial', 12, 'bold'),
                                   text='Mobile Number:', padx=2, pady=2, bg='cadet blue')
        self.lbl_mbl_no.grid(row=8, column=0, sticky=tk.W)

        self.txt_mbl_no = tk.Entry(data_frame_left, font=('arial', 12, 'bold'),
                                   textvariable=MNo, width=25)
        self.txt_mbl_no.grid(row=8, column=1)

# Selling Price
        self.lbl_sel_pr = tk.Label(data_frame_left, font=('arial', 12, 'bold'),
                                   text='Selling Price:', padx=2, pady=2, bg='cadet blue')
        self.lbl_sel_pr.grid(row=8, column=2, sticky=tk.W)

        self.txt_sel_pr = tk.Entry(data_frame_left, font=('arial', 12, 'bold'),
                                   textvariable=sPr, width=25)
        self.txt_sel_pr.grid(row=8, column=3)

# ===================================Listbox and Scrollbar======================================== #

        scrollbar = tk.Scrollbar(data_frame_right)
        scrollbar.grid(row=0, column=1, sticky='ns')

        booklist = tk.Listbox(data_frame_right, width=45, height=12,
                              font=('arial', 12, 'bold'), yscrollcommand=scrollbar.set)
        booklist.bind('<<ListboxSelect>>', selected_book)
        booklist.grid(row=0, column=0, padx=8)
        scrollbar.config(command=booklist.yview)


# ======================================Buttons Widget============================================ #

        self.btn_add_data = tk.Button(button_frame, text='Add Data', font=('arial', 14, 'bold'),
                                      height=2, width=13, bd=4, command=add_data)
        self.btn_add_data.grid(row=0, column=0)

        self.btn_disp_data = tk.Button(button_frame, text='Display Data',
                                       font=('arial', 14, 'bold'), height=2, width=13, bd=4,
                                       command=display_data)
        self.btn_disp_data.grid(row=0, column=1)

        self.btn_clr_data = tk.Button(button_frame, text='Clear Data', font=('arial', 14, 'bold'),
                                      height=2, width=13, bd=4, command=clear_data)
        self.btn_clr_data.grid(row=0, column=2)

        self.btn_del_data = tk.Button(button_frame, text='Delete Data', font=('arial', 14, 'bold'),
                                      height=2, width=13, bd=4, command=delete_record)
        self.btn_del_data.grid(row=0, column=3)

        self.btn_upd_data = tk.Button(button_frame, text='Update Data', font=('arial', 14, 'bold'),
                                      height=2, width=13, bd=4, command=update_data)
        self.btn_upd_data.grid(row=0, column=4)

        self.btn_srch_data = tk.Button(button_frame, text='Search Data', font=('arial', 14, 'bold'),
                                       height=2, width=13, bd=4, command=search_data)
        self.btn_srch_data.grid(row=0, column=5)

        self.btn_exit = tk.Button(button_frame, text='Exit', font=('arial', 14, 'bold'),
                                  height=2, width=13, bd=4, command=i_exit)
        self.btn_exit.grid(row=0, column=6)

# ======================================Initialization============================================ #


if __name__ == '__main__':
    root = tk.Tk()
    application = Library(root)
    root.mainloop()
