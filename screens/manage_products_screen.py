from cgitb import text
from tkinter import *
from tkinter import ttk
import colors
import screens.add_product_screen as aps
import screens.home_screen as hs
import api.products
from tkinter import messagebox

frame = 0

def go_back(main):
    frame.forget()
    hs.home_screen(main)

def add_product_screen(main,product=None):
    frame.forget()
    aps.add_prodcut_screen(main,product)

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
    content.pack(fill=BOTH, expand=True,padx=10,pady=10)


    search = Frame(content, background=colors.PRIMARY)
    search.pack(side=TOP, fill=X, padx=10, pady=10)

    ttk.Button(search, text="Add Product", width=25,
               command=lambda: add_product_screen(main)).pack(side=LEFT, padx=(0, 10))
    searchinput = StringVar()
    searchinput.set("Search Products")
    searchquery = ttk.Entry(search, foreground=colors.SECONDARY,textvariable=searchinput)
    searchquery.pack(side=LEFT, fill=BOTH, expand=True)
    ttk.Button(search, text="Search", width=25,command=lambda:search_product(searchinput.get().lower())).pack(side=RIGHT)

    def search_product(query):
        products = api.products.getAll()
        filtered = [i for i in products if query in i[1].lower()]
        generate_products_list(filtered)

    def generate_products_list(products):
        global canvas
        global scrollbar

        ## LIST OF PRODUCTS WITH SCROLLBAR
        
        try: 
            canvas.destroy()
            scrollbar.destroy()
        except NameError:
            pass
        
        canvas = Canvas(content, background=colors.PRIMARY)

        product_list = Frame(canvas, background=colors.PRIMARY)
        scrollbar = Scrollbar(content, orient = 'vertical',command=canvas.yview)
        for x in products:
            product = ttk.Label(product_list, text=x[1] + "\n" +str(x[2])+"x\n[ $ "+str(x[3])+" ] " ,
                            background=colors.SECONDARY, foreground="#fff", padding=10)
            product.pack(fill=BOTH,pady=2)
            product.bind("<Button-3>",lambda e,x=x:set_current_product(e.x_root,e.y_root,x))
  
        canvas_frmae = canvas.create_window(0, 0,anchor=NW, window=product_list)
        canvas.update_idletasks()

        canvas.configure(scrollregion=canvas.bbox('all'), 
                        yscrollcommand=scrollbar.set)
                        
        canvas.pack(fill=BOTH, expand=True, side=LEFT)
        product_list.bind("<Configure>", lambda e:canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.bind('<Configure>', lambda e:canvas.itemconfig(canvas_frmae, width = e.width))
        scrollbar.pack(fill=Y, side=RIGHT)


    def get_current_product():
        global selected_product
        return selected_product

    def set_current_product(x,y,data):
        global selected_product
        selected_product = data
        contextmenu.tk_popup(x,y)
   
    contextmenu = Menu(main, tearoff = 0)
    contextmenu.add_command(label ="Update",command=lambda:add_product_screen(main,get_current_product()))

    generate_products_list(products)