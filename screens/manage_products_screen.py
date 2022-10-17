from tkinter import *
from tkinter import ttk
import colors
import screens.add_product_screen as aps
import screens.home_screen as hs
import api.products

frame = 0

def go_back(main):
    frame.forget()
    hs.home_screen(main)

def add_product_screen(main):
    frame.forget()
    aps.add_prodcut_screen(main)

def manage_products_screen(main):

    products = api.products.getAll()
    style = ttk.Style()
    style.configure('TButton', foreground=colors.SECONDARY, width=20,
                    borderwidth=1, focusthickness=3, focuscolor='none')

    global frame
    frame = Frame(main, background=colors.PRIMARY)
    frame.pack(fill=BOTH, expand=True)

    header = Frame(frame)
    header.pack(fill=X)
    back = ttk.Label(header, text="⬅", background=colors.PRIMARY,
                     foreground=colors.SECONDARY, font=(30), padding=10,)
    back.pack(side=LEFT, fill=BOTH)
    ttk.Label(header, text="Manage Products 📦 ", background=colors.PRIMARY,
              foreground=colors.SECONDARY, font=(30), padding=10).pack(side=RIGHT, fill=BOTH, expand=True)
    back.bind("<Button-1>", lambda e: go_back(main))
    
    content = Frame(frame, background=colors.PRIMARY)
    content.pack(side=RIGHT, anchor='e', fill=BOTH, expand=True)

    search = Frame(content, background=colors.PRIMARY)
    search.pack(side=TOP, fill=X, padx=10, pady=10)

    ttk.Button(search, text="Add Product", width=25,
               command=lambda: add_product_screen(main)).pack(side=LEFT, padx=(0, 10))
    searchquery = ttk.Entry(search, foreground=colors.SECONDARY)
    searchquery.insert(0, 'Search Produts')
    searchquery.pack(side=LEFT, fill=BOTH, expand=True)
    ttk.Button(search, text="Search", width=25).pack(side=RIGHT)

    bill_list = Frame(content, background=colors.PRIMARY)
    bill_list.pack(side=TOP, fill=BOTH, padx=10, pady=10)
    
    for x in products:
        ttk.Label(bill_list, text=x[1] + "\n" +str(x[2])+"x\n[ $ "+str(x[3])+" ] " ,
                        background=colors.SECONDARY, foreground="#fff", padding=10).pack(fill=BOTH,pady=2)
