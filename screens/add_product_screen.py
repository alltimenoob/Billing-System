from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import colors
import screens.manage_products_screen as mps
import api.product_types
import api.products

frame = 0


def go_back(main):
    frame.forget()
    mps.manage_products_screen(main)


def add_prodcut_screen(main):

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
    ttk.Label(header, text="Add Products 📦 ", background=colors.PRIMARY,
              foreground=colors.SECONDARY, font=(30), padding=10).pack(side=RIGHT, fill=BOTH, expand=True)
    back.bind("<Button-1>", lambda e: go_back(main))

    content = Frame(frame, background=colors.PRIMARY)
    content.pack(fill=BOTH, expand=True)

    selected_product_type = StringVar()
    container = Frame(content, background=colors.PRIMARY)
    container.pack(fill=X, padx=10, pady=10)
    ttk.Label(container, text="Product Type",
              background=colors.SECONDARY, foreground="#fff", width=25).pack(side=LEFT)
    product_types_combobox = ttk.Combobox(
        container, textvariable=selected_product_type)
    product_types_combobox['values'] = tuple([i[1] for i in product_types])
    product_types_combobox.pack(side=RIGHT, fill=X, expand=True)

    selected_product_name = StringVar()
    container = Frame(content, background=colors.PRIMARY)
    container.pack(fill=X, padx=10, pady=10)
    ttk.Label(container, text="Product Name",
              background=colors.SECONDARY, foreground="#fff", width=25).pack(side=LEFT)
    ttk.Entry(container, textvariable=selected_product_name).pack(
        side=RIGHT, fill=X, expand=True)

    seleceted_quantity = StringVar()
    container = Frame(content, background=colors.PRIMARY)
    container.pack(fill=X, padx=10, pady=10)
    ttk.Label(container, text="Quantity",
              background=colors.SECONDARY, foreground="#fff", width=25).pack(side=LEFT)
    ttk.Entry(container, textvariable=seleceted_quantity).pack(
        side=RIGHT, fill=X, expand=True)

    selected_price = StringVar()
    container = Frame(content, background=colors.PRIMARY)
    container.pack(fill=X, padx=10, pady=10)
    ttk.Label(container, text="Price",
              background=colors.SECONDARY, foreground="#fff", width=25).pack(side=LEFT)
    ttk.Entry(container, textvariable=selected_price).pack(
        side=RIGHT, fill=X, expand=True)

    def add_product(data):
        selected_price.set('')
        seleceted_quantity.set('')
        selected_product_name.set('')
        if api.products.add(data)>0 :
            messagebox.showinfo("Info","Inserted Successfully")
        else:
            messagebox.showerror("Error","Something Went Wrong!")

    container = Frame(content, background=colors.PRIMARY)
    container.pack(fill=X, padx=10, pady=10)
    ttk.Button(container, text="Submit", width=25,
               command=lambda: add_product(
                   {
                       'products_name': selected_product_name.get(),
                       'quantity': seleceted_quantity.get(),
                       'price': selected_price.get(),
                       'products_types_id': [a[0] for a in product_types if selected_product_type.get() in a]
                   })
               ).pack(fill=BOTH)
