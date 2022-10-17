from tkinter import * 
import screens.home_screen as hs

root = Tk()
root.geometry("800x600")

hs.home_screen(root)

root.title("Billing System")
icon = PhotoImage(file='icon.png')
root.iconphoto(False,icon)

root.mainloop()