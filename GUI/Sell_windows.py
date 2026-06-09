from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *


import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from systemDAO import System
from wCart.car import Cart
from motor_cycle import Motor_cycle
from Sell.sell import Sell



class SellWindow(Toplevel):

    def __init__(self, master):
        super().__init__(master)
        self.products = []
        self.protocol("WM_DELETE_WINDOW", self.close_w)
        self.configure_screen()
        self.grid_configure()
        self.labels()
        self.frame()
        self.frame_entry()
        self.table()
        self.boxs()
        self.button()
        self.load_information()
        self.styles_interface()

    def configure_screen(self):
        self.geometry('800x500+100+100')
        self.title('sell')
        self.configure(background='#ff5c46')
        self.resizable(False,False)
    
    def grid_configure(self):
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=3)

    def styles_interface(self):
        self.style = Style()
        self.style.theme_use('clam')


        self.style.configure('Treeview', fieldbackground = "#e96730", 
                             background = '#e96730', 
                             font=('Mono space', 12))
        self.style.configure('Treeview.Heading', 
                             background = '#e96730', 
                             foreground = 'black', 
                             font=('Mono space', 12))
        self.style.map('Treeview.Heading', 
                       background = [('active', '#a44218')])
        self.style.map('Treeview', 
                       background=[('selected', "#821f0c")])

        self.style.configure('TButton', background='#ba2905',
                             font = ('Mono Space', 13))
        
        self.style.map('TButton', background=[('active', '#821f0c')],
                       foreground = [('active', 'white')],
                       )

        self.style.configure('TEntry', fieldbackground = '#ff5c46',
                             font=('Mono space', 15), foreground = 'white')

    def labels(self):
        self.label_title = Label(self, text='SELL', font=('Mono space', 20))
        self.label_title.grid(row=0, column=0, columnspan=2, sticky=N)
        self.label_title.configure(background='#ff5c46')

    def frame(self):
        self.frame_tb = Frame(self)
        self.frame_tb.grid(row=1, column=1, sticky=NSEW)

        #grid inside frame
        self.frame_tb.columnconfigure(0,weight=1)
        self.frame_tb.rowconfigure(0,weight=1)

    def frame_entry(self):
        self.container_frame = Frame(self)
        self.container_frame.grid(row=1, column=0, sticky=NSEW)

        self.container_frame.columnconfigure(0, weight=1)
        self.container_frame.rowconfigure(0, weight=1)
        self.container_frame.rowconfigure(1, weight=1)
        self.container_frame.rowconfigure(2, weight=1)
        self.container_frame.rowconfigure(3, weight=1)
        self.container_frame.rowconfigure(4, weight=1)
    
    def table(self):
        headers = ('model', 'amount', 'price')
        self.table_fm = Treeview(self.frame_tb, columns=headers, show='headings')

        self.table_fm.heading('model', text= 'Model')
        self.table_fm.heading('amount', text= 'Amount')
        self.table_fm.heading('price', text='Price')

        self.table_fm.column('model', width=90)
        self.table_fm.column('amount', width=30)
        self.table_fm.column('price', width=30)
        
        self.scroll = Scrollbar(self.frame_tb, orient=VERTICAL, command=self.table_fm.yview)
        self.table_fm.configure(yscrollcommand=self.scroll.set)
        self.scroll.grid(row=0, column=1, sticky=NS)

        self.table_fm.bind('<<TreeviewSelect>>', self.get_info_table)

        self.table_fm.grid(row=0,column=0, sticky=NSEW)

    def boxs(self):
        self.name_entry = Entry(self.container_frame)
        self.name_label = Label(self.container_frame, text='Full Name', font=('mono space', 10))
        self.name_entry.grid(row=0, column=0,sticky=S)
        self.name_label.grid(row=0, column=0)
        self.name_label.configure(background='#ff5c46')

        self.CI_entry = Entry(self.container_frame)
        self.CI_label = Label(self.container_frame, text='C.I', font=('mono space', 10))
        self.CI_entry.grid(row=1, column=0, sticky=S)
        self.CI_label.grid(row=1, column=0)
        self.CI_label.configure(background='#ff5c46')

        self.NumberPh_entry = Entry(self.container_frame)
        self.NumberPh_label = Label(self.container_frame, text='Number Phone', font=('mono space', 10))
        self.NumberPh_entry.grid(row=2, column=0, sticky=S)
        self.NumberPh_label.grid(row=2, column=0)
        self.NumberPh_label.configure(background='#ff5c46')

        self.amount_entry = Entry(self.container_frame)
        self.amount_entry.insert(END, '0')
        self.amount_label = Label(self.container_frame, text='Amount', font=('mono space', 10))
        self.amount_entry.grid(row=3, column=0, sticky=S)
        self.amount_label.grid(row=3, column=0)
        self.amount_label.configure(background='#ff5c46')

        self.add = Button(self.container_frame, text= '>', command= self.add_amount, width=3)
        self.add.grid(row=3, column= 0, sticky=SE)
        self.decri = Button(self.container_frame, text= '<', command= self.decri_amount, width=3)
        self.decri.grid(row=3, column= 0, sticky=SW)

    def button(self):
        self.sell_button = Button(self.container_frame, text = 'Sell', command= self.sell_function)
        self.sell_button.grid(row=4, column=0, sticky=SW)

        self.addCart_button = Button(self.container_frame, text='Add Cart', command=self.add_cart_button)
        self.addCart_button.grid(row=4, column=0, sticky=SE)

    def load_information(self):
        for item in self.table_fm.get_children():
            self.table_fm.delete(item)
        
        # Load new data
        list_motor = System().select()
        for motor in list_motor:
            self.table_fm.insert(parent='', index=END, values=motor)

    def get_information(self):
        self.entry_name = self.name_entry.get()
        self.entry_CI = self.CI_entry.get()
        self.entry_numberPH = self.NumberPh_entry.get()
        self.entry_amount = self.amount_entry.get()
        if self.check(self.entry_name, self.entry_CI, self.entry_numberPH, self.entry_amount) == False:
            return False
        else:
            info = (self.entry_name, self.entry_CI, self.entry_numberPH, self.entry_amount)
            return info
    
    def check(self, name, CI, numberPH, amount):
        if name and CI and numberPH and amount:
            if len(numberPH) == 11:
                if int(amount) > 0:
                    return True
                else:
                    showwarning(title='', message='The amount has be more then 0')
                    self.amount_entry.delete(0,END)
                    return False
            else:
                showwarning(title='', message='Insert a correct number')
                self.NumberPh_entry.delete(0,END)
                return False
        else:
            showwarning(title='', message='Fill in every box')
            return False

    def add_cart_button(self):
        info = self.get_information()

        if len(self.products) == 0:
            showwarning(title='', message='Try select something firts')
        elif self.products[1] == 0:
            showwarning(title='', message='There\'s not enough stock')
            self.products = []
        else:
           cart = Motor_cycle(model=self.products[0], amoung=info[3], price=self.products[2])
           Cart().add_cart(cart)
           self.products = []
           showinfo(title='', message='Added to the cart.')

    def get_info_table(self, event):
        info = self.table_fm.selection()
        if info:
            product = self.table_fm.item(info)['values']
            print(product)
            for _ in product:
                self.products.append(_)
        else:
            return False

    def clear_boxes(self):
        self.name_entry.delete(0,END)
        self.CI_entry.delete(0,END)
        self.NumberPh_entry.delete(0,END)
        self.amount_entry.delete(0,END)

    def sell_function(self):
        info = self.get_information()
        if info == False:
            pass
        else:
            Sell().create_check(name=info[0], ci=info[1], numberph=info[2])
            showinfo(title='',message='The sell was succesfull')
            self.clear_boxes()
            self.load_information()

    def close_w(self):
        self.master.deiconify()
        self.destroy()
    
    def add_amount(self):
        amount = int(self.amount_entry.get())
        amount += 1
        self.amount_entry.delete(0,END)
        self.amount_entry.insert(END, amount)


    def decri_amount(self):
        amount = int(self.amount_entry.get())
        if amount is not 0:
            amount -= 1
            self.amount_entry.delete(0,END)
            self.amount_entry.insert(END, amount)
        else:
            pass
            
if __name__ == '__main__':
    SellWindow().mainloop()

    #that was fantastic you're pretty close out, don't give up :)