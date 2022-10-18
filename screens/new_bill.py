from cgitb import text
from cmath import exp
from itertools import product
from math import prod
from sre_parse import fix_flags
from tkinter import *
from tkinter import ttk
from turtle import right, width
import colors
import screens.home_screen as hs
import api.products
from tkinter import messagebox

frame = 0


def go_back(main):
    frame.forget()
    hs.home_screen(main)


def new_bill(main):

    product_types = api.product_types.getAll()

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
    ttk.Label(header, text="New Bill 💷 ", background=colors.PRIMARY,
              foreground=colors.SECONDARY, font=(30), padding=10).pack(side=RIGHT, fill=BOTH, expand=True)
    back.bind("<Button-1>", lambda e: go_back(main))

    content = Frame(frame, background=colors.PRIMARY)
    content.pack(fill=BOTH, expand=True, padx=10, pady=10)

    customer_data_frame = Frame(content, background=colors.PRIMARY)
    customer_name = StringVar()
    customer_email = StringVar()
    customer_phone = StringVar()

    ttk.Label(customer_data_frame, text="Customer Name - ", background=colors.PRIMARY,
              foreground=colors.SECONDARY, padding=10,).grid(row=0, column=0)
    ttk.Entry(customer_data_frame, textvariable=customer_name,
              width=90).grid(row=0, column=1)
    ttk.Label(customer_data_frame, text="Customer Email - ", background=colors.PRIMARY,
              foreground=colors.SECONDARY, padding=10).grid(row=1, column=0)
    ttk.Entry(customer_data_frame, textvariable=customer_email,
              width=90).grid(row=1, column=1)
    ttk.Label(customer_data_frame, text="Customer Phone - ", background=colors.PRIMARY,
              foreground=colors.SECONDARY, padding=10,).grid(row=2, column=0)
    ttk.Entry(customer_data_frame, textvariable=customer_phone,
              width=90).grid(row=2, column=1)

    ttk.Button(customer_data_frame, text="Fetch").grid(row=3, column=0)
    total_label = ttk.Label(customer_data_frame, text="Total - 0", background=colors.SECONDARY,
              foreground='#FFF', padding=5,)
    total_label.grid(row=3, column=1)
    customer_data_frame.pack(side=TOP, fill=X)

    bill_frame = Frame(content, background=colors.PRIMARY)
    bill_frame.pack(side=TOP, fill=BOTH, expand=True)

    plusbutton = ttk.Button(
        content, text="➕", command=lambda: add_new_product_to_bill())
    plusbutton.pack(side=BOTTOM, fill=X)

    def add_new_product_to_bill():
        global n
        try:
            n += 1
        except:
            n = 1
        plusbutton.forget()
        plusbutton.pack(side=BOTTOM, fill=X)
        generate_bill_list(n)

    def get_product_list():
        selected_values = [i["product"].get() for i in bill_list_values]
        result = [i for i in api.products.getAll() if i[1]
                  not in selected_values]
        return result

    def generate_bill_list(n):
        global canvas
        global scrollbar
        global bill_list_values

        # LIST OF PRODUCTS WITH SCROLLBAR
        try:
            canvas.destroy()
            scrollbar.destroy()
        except NameError:
            pass

        canvas = Canvas(bill_frame, background=colors.PRIMARY)

        product_list = Frame(canvas, background=colors.PRIMARY)
        scrollbar = Scrollbar(
            bill_frame, orient='vertical', command=canvas.yview)

        if "bill_list_values" not in globals():
            bill_list_values = list()
            
       
        bill_item_frames=list()
        for x in range(n):
            products = get_product_list()
            bill_list_values.append(
                {"product": StringVar(), "quantity": IntVar(), "amount": 0})
            if bill_list_values[x]['product'].get() != "":
                if bill_list_values[x]['quantity'].get() == 0: bill_list_values[x]['quantity'].set(1)
                bill_list_values[x]['amount'] = [i[2] for i in api.products.getAll(
                ) if i[1] == bill_list_values[x]['product'].get()][0] * bill_list_values[x]['quantity'].get()
            total = [i['amount'] for i in bill_list_values]
            total = sum(total)
            total_label.config(text="Total - "+str(total))
            values = ([i[1] for i in products])
            bill_item_frames.append(
                Frame(product_list, background=colors.PRIMARY,padx=10,pady=10))
            if x < len(api.products.getAll()):
                product = ttk.Combobox(
                    bill_item_frames[x], textvariable=bill_list_values[x]["product"],width=40)
                product['values'] = values
                product.pack(side=LEFT,fill=Y)
                product.bind('<<ComboboxSelected>>',
                             lambda _: generate_bill_list(n))
                quantity = ttk.Entry(
                    bill_item_frames[x], textvariable=bill_list_values[x]['quantity'],width=40)
                quantity.bind("<FocusOut>", lambda _: generate_bill_list(n))
                amount = ttk.Label(bill_item_frames[x], text=str(
                    bill_list_values[x]['amount']),padding=10,width=20,foreground="#fff",background=colors.SECONDARY)
                quantity.pack(side=LEFT,fill=Y)
                amount.pack(side=LEFT,fill=Y)
            bill_item_frames[x].pack(side=TOP, fill=X)

        canvas_frame = canvas.create_window(
            0, 0, anchor=NW, window=product_list)
        canvas.update_idletasks()

        canvas.configure(scrollregion=canvas.bbox('all'),
                         yscrollcommand=scrollbar.set)

        canvas.pack(fill=BOTH, expand=True, side=LEFT)
        product_list.bind("<Configure>", lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")))
        canvas.bind('<Configure>', lambda e: canvas.itemconfig(
            canvas_frame, width=e.width))
        scrollbar.pack(fill=Y, side=RIGHT, anchor=E)
