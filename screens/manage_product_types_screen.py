from cgitb import text
from tkinter import *
from tkinter import ttk
import colors
import screens.add_product_screen as aps
import screens.home_screen as hs
import api.product_types
from tkinter import messagebox

frame = 0

def go_back(main):
    frame.forget()
    hs.home_screen(main)

def add_product_screen(main,product=None):
    frame.forget()
    aps.add_prodcut_screen(main,product)

def manage_product_types_screen(main):

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
    ttk.Label(header, text="Manage Product Types 📑 ", background=colors.PRIMARY,
              foreground=colors.SECONDARY, font=(30), padding=10).pack(side=RIGHT, fill=BOTH, expand=True)
    back.bind("<Button-1>", lambda e: go_back(main))
    
    content = Frame(frame, background=colors.PRIMARY)
    content.pack(fill=BOTH, expand=True,padx=10,pady=10)


    addproducttype = Frame(content, background=colors.PRIMARY)
    
    product_type = StringVar()
    ttk.Entry(addproducttype,textvariable=product_type).pack(side=LEFT,padx=(0,10),fill=X,expand=True)
    
    add_update_button = ttk.Button(addproducttype, text="Add Product Type", width=25,
               command=lambda:add_product_type())
    add_update_button.pack(side=RIGHT, padx=10)

    addproducttype.pack(side=TOP,fill=X)

    def generate_product_types_list(product_types):
        global canvas
        global scrollbar

        ## LIST OF product_types WITH SCROLLBAR
        
        try: 
            canvas.destroy()
            scrollbar.destroy()
        except NameError:
            pass
        
        canvas = Canvas(content, background=colors.PRIMARY)

        product_list = Frame(canvas, background=colors.PRIMARY)
        scrollbar = Scrollbar(content, orient = 'vertical',command=canvas.yview)
        for x in product_types:
            product = ttk.Label(product_list, text=x[1] ,
                            background=colors.SECONDARY, foreground="#fff", padding=10)
            product.pack(fill=BOTH,pady=2)
            product.bind("<Button-3>",lambda e,x=x:set_current_product_type(e.x_root,e.y_root,x))
  
        canvas_frmae = canvas.create_window(0, 0,anchor=NW, window=product_list)
        canvas.update_idletasks()

        canvas.configure(scrollregion=canvas.bbox('all'), 
                        yscrollcommand=scrollbar.set)
                        
        canvas.pack(fill=BOTH, expand=True, side=LEFT)
        product_list.bind("<Configure>", lambda e:canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.bind('<Configure>', lambda e:canvas.itemconfig(canvas_frmae, width = e.width))
        scrollbar.pack(fill=Y, side=RIGHT)


    def update_screen():
        selected_product_type = get_current_product_type()
        product_type.set(selected_product_type[1])
        add_update_button.config(text="Update Product Type")
        add_update_button.config(command=lambda:update_product_type(selected_product_type[0]))

    def update_product_type(id):
        api.product_types.update((id,product_type.get()))
        product_type.set('')
        add_update_button.config(text="Add Product Type")
        add_update_button.config(command=lambda:add_product_type())
        product_types = api.product_types.getAll()
        generate_product_types_list(product_types)

    def add_product_type():
        data = product_type.get()
        if data == "":
            messagebox.showerror("Error","Product Type Cannot Be Empty!")
            return 
        
        api.product_types.add(data)
        product_type.set('')
        product_types = api.product_types.getAll()
        generate_product_types_list(product_types)

    def get_current_product_type():
        global selected_product_type
        return selected_product_type

    def set_current_product_type(x,y,data):
        global selected_product_type
        selected_product_type = data
        contextmenu.tk_popup(x,y)
    

    contextmenu = Menu(main, tearoff = 0)
    contextmenu.add_command(label ="Update",command=lambda:update_screen())

    generate_product_types_list(product_types)