from tkinter import *
from tkinter import ttk
import colors
import screens.manage_products_screen as mps
import screens.manage_product_types_screen as mpts

frame = 0


def manage_products_screen(main):
    frame.forget()
    mps.manage_products_screen(main)

def manage_product_types_screen(main):
    frame.forget()
    mpts.manage_product_types_screen(main)

def home_screen(main):

    style = ttk.Style()
    style.configure('TButton', foreground=colors.SECONDARY, width=20,
                    borderwidth=1, focusthickness=3, focuscolor='none')

    global frame

    if frame != 0:
        frame.pack(fill=BOTH, expand=True)
        return

    frame = Frame(main, background=colors.PRIMARY)
    frame.pack(fill=BOTH, expand=True)

    header = ttk.Label(frame, text="Billing System 💷 ", background=colors.PRIMARY,
                       foreground=colors.SECONDARY, font=(30), padding=10)
    header.pack(fill=BOTH)

    sidebar = Frame(frame, background=colors.PRIMARY)
    sidebar.pack(side=LEFT, anchor='w', fill=Y)
    ttk.Button(sidebar, text="New Bill", width=25,
               style='TButton').pack(anchor='n', padx=10, pady=10)
    ttk.Button(sidebar, text="Manage Products", width=25, style='TButton',
               command=lambda: manage_products_screen(main)).pack(anchor='n', padx=10, pady=10)
    ttk.Button(sidebar, text="Manage Product Types", width=25,
               command=lambda: manage_product_types_screen(main),style='TButton').pack(anchor='n', padx=10, pady=10)
    ttk.Button(sidebar, text="Quit", width=25, style='TButton',
               command=main.destroy).pack(anchor='n', side=RIGHT, padx=10, pady=10)

    content = Frame(frame, background=colors.PRIMARY)
    content.pack(side=RIGHT, anchor='e', fill=BOTH, expand=True)

    search = Frame(content, background=colors.PRIMARY)
    search.pack(side=TOP, fill=X, padx=10, pady=10)

    searchquery = ttk.Entry(search, foreground=colors.SECONDARY)
    searchquery.insert(0, 'Search Bills')
    searchquery.pack(side=LEFT, fill=BOTH, expand=True)
    ttk.Button(search, text="Search", width=25).pack(side=RIGHT)

    bill_list = Frame(content, background=colors.PRIMARY)
    bill_list.pack(side=TOP, fill=BOTH, padx=10, pady=10)
    header = ttk.Label(bill_list, text="Bill #1",
                       background=colors.SECONDARY, foreground="#fff", padding=10)
    header.pack(fill=BOTH)
