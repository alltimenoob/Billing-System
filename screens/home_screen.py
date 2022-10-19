from tkinter import *
from tkinter import ttk
import colors
import screens.manage_products_screen as mps
import screens.manage_product_types_screen as mpts
import screens.new_bill as nb
import api.bills
import api.customers

frame = 0


def navigate(main,screen):
    frame.forget()
    if screen == 0 : nb.new_bill(main)
    elif screen == 1 : mps.manage_products_screen(main)
    else : mpts.manage_product_types_screen(main)


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
    ttk.Button(sidebar, text="New Bill", width=25,style='TButton',
               command=lambda: navigate(main,0)).pack(anchor='n', padx=10, pady=10)
    ttk.Button(sidebar, text="Manage Products", width=25, style='TButton',
               command=lambda: navigate(main,1)).pack(anchor='n', padx=10, pady=10)
    ttk.Button(sidebar, text="Manage Product Types", width=25,
               command=lambda: navigate(main,2),style='TButton').pack(anchor='n', padx=10, pady=10)
    ttk.Button(sidebar, text="Quit", width=25, style='TButton',
               command=main.destroy).pack(anchor='n', side=RIGHT, padx=10, pady=10)

    content = Frame(frame, background=colors.PRIMARY)
    content.pack(side=RIGHT, anchor='e', fill=BOTH, expand=True)

    search = Frame(content, background=colors.PRIMARY)
    search.pack(side=TOP, fill=X, padx=10, pady=10)

    query = StringVar()
    searchquery = ttk.Entry(search, foreground=colors.SECONDARY,textvariable=query)
    searchquery.insert(0, 'Search Bills')
    searchquery.pack(side=LEFT, fill=BOTH, expand=True)
    ttk.Button(search, text="Search", width=25,command=lambda:filter_bills(query.get())).pack(side=RIGHT)

    def filter_bills(query):
        bills = api.bills.getAll()

        newbill = list()
        for i in bills:
            if query in i[2]:
                newbill.append(i)

        generate_bills(newbill)
        return

    bills = api.bills.getAll()

    
   
    def generate_bills(bills):
        global canvas
        global scrollbar
        if 'canvas' in globals():
            canvas.destroy()
            scrollbar.destroy()
        
        canvas = Canvas(content, background=colors.PRIMARY)
    
        bill_list = Frame(canvas, background=colors.PRIMARY)
        scrollbar = Scrollbar(content, orient = 'vertical',command=canvas.yview)
        

        for i in bills:
            customer = api.customers.getEmailById(i[3])
            ttk.Label(bill_list, text="ID : "+str(i[0])+"\nAmount : "+str(i[1])+"\nDate : "+str(i[2])+"\nCustomer : "+customer[0],
                            background=colors.SECONDARY, foreground="#fff", padding=10,width=100).pack(fill=BOTH,padx=10,pady=10)
        canvas_frmae = canvas.create_window(0, 0,anchor=NW, window=bill_list)
        canvas.update_idletasks()

        canvas.configure(scrollregion=canvas.bbox('all'), 
                            yscrollcommand=scrollbar.set)
                            
        canvas.pack(fill=BOTH, expand=True, side=LEFT)
        bill_list.bind("<Configure>", lambda e:canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.bind('<Configure>', lambda e:lambda e:canvas.itemconfig(canvas_frmae, width = e.width))
        scrollbar.pack(fill=Y, side=RIGHT)

    generate_bills(bills)