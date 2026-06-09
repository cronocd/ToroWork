from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *
import smtplib
from email.message import EmailMessage

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from motor_cycle import Motor_cycle
from systemDAO import System
from .Sell_windows import SellWindow
from funtionc_close.close import CloseStore

class Windows(Tk):

    def __init__(self):
        super().__init__()
        self.model = None
        self.show_screen()
        self.styles_interface()
        self.configure_screen()
        self.labels()
        self.frame_buttons()
        self.frame_entries()
        self.frame_table()
        self.table_frame()
        self.buttons()
        self.boxs()
        self.clear_boxs()

    def show_screen(self):
        self.geometry('950x500+100+100')
        self.title('Toro')
        self.configure(background='#ff5c46')
        self.resizable(False,False)

    def configure_screen(self):
        self.columnconfigure(0,weight=1)
        self.columnconfigure(1,weight=2)

        self.rowconfigure(0,weight=1)
        self.rowconfigure(1,weight=2)
        self.rowconfigure(2,weight=1)

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
                             font=('Mono space', 13), foreground = 'white')
        
        self.style.configure('TFrame', background='#ff5c46')

    def labels(self):

        self.label_title = Label(self, text='Inventory Toro', font=('Mono Space', 20))
        self.label_title.configure(background='#ff5c46')
        self.label_title.grid(row=0, column=0, columnspan=2, sticky=N)

    def frame_table(self):
        self.frame_tb = Frame(self)
        
        #GRID------------------------------------
        self.frame_tb.grid(row=1, column=1, sticky=NSEW)
        self.frame_tb.columnconfigure(0,weight=1)
        self.frame_tb.rowconfigure(0,weight=1)
        #-----------------------------------------

    def frame_entries(self):
        self.entries_container = Frame(self)
        self.entries_container.grid(row=1, column=0, sticky=NSEW)

        self.entries_container.columnconfigure(0, weight=1)
    
        self.entries_container.rowconfigure(0, weight=1)
        self.entries_container.rowconfigure(1, weight=1)
        self.entries_container.rowconfigure(2, weight=1)
    
    def frame_buttons(self):
        self.buttons_container = Frame(self)
        self.buttons_container.grid(row=2, column=0, columnspan=2, sticky=NSEW)

        self.buttons_container.columnconfigure(0, weight=1)
        self.buttons_container.columnconfigure(1, weight=1)
        self.buttons_container.columnconfigure(2, weight=1)
        self.buttons_container.columnconfigure(3,weight=1)
        self.buttons_container.columnconfigure(4,weight=1)

        self.buttons_container.rowconfigure(0, weight=1)

    def table_frame(self):

        headers = ('Model', 'Amoung', 'Price')
        self.table_fm = Treeview(self.frame_tb, columns=headers, show='headings')

        #HEADERS---------------------------------------
        self.table_fm.heading('Model', text='Model')
        self.table_fm.heading('Amoung', text='Amoung')
        self.table_fm.heading('Price', text='Price')

        self.table_fm.column('Model', width=100)
        self.table_fm.column('Amoung', width=100)
        self.table_fm.column('Price', width=100)
        #-----------------------------------------------

        self.load_table_data()

        self.table_fm.bind('<<TreeviewSelect>>', self.record_table)
        
        #It doesn't work
        self.scrollbar = Scrollbar(self.frame_tb, orient=VERTICAL, command=self.table_fm.yview)
        self.table_fm.configure(yscroll=self.scrollbar.set)
        self.scrollbar.grid(row=0, column=1, sticky=NS)

        self.table_fm.tag_configure(tagname='low-stock', foreground='Blue')

        self.table_fm.grid(row=0,column=0, sticky=NSEW)
        
    def buttons(self):

        self.button_s = Button(self.buttons_container, text='Save', command=self.add_new_motor)
        self.button_s.grid(row=0, column=0)

        self.button_d = Button(self.buttons_container, text='Delete', command=self.delete_motor_cycle)
        self.button_d.grid(row=0, column=1)

        self.button_clear = Button(self.buttons_container, text='Clear', command=self.clear_boxs)
        self.button_clear.grid(row=0, column=2)

        self.button_sell = Button(self.buttons_container, text='Sell', command=self.view_sell)
        self.button_sell.grid(row=0, column=3)

        self.button_c = Button(self.buttons_container, text='Close', command= self.close_button)
        self.button_c.grid(row=0, column=4)

    def boxs(self):
        self.model_entry= Entry(self.entries_container)
        self.label_model = Label(self.entries_container, text= 'Model', font=('Mono space', 12))

        self.model_entry.grid(row=0, column=0)
        self.label_model.grid(row=0, column=0, sticky=N)
        self.label_model.configure(background='#ff5c46')

        self.amoung_entry= Entry(self.entries_container)
        self.label_amoung = Label(self.entries_container, text= 'Amoung', font=('Mono space', 12))

        self.amoung_entry.grid(row=1, column=0)
        self.label_amoung.grid(row=1, column=0, sticky=N)
        self.label_amoung.configure(background='#ff5c46')

        self.price_entry= Entry(self.entries_container)
        self.label_price = Label(self.entries_container, text= 'Price', font=('Mono space', 12))

        self.price_entry.grid(row=2, column=0)
        self.label_price.grid(row=2, column=0, sticky=N)
        self.label_price.configure(background='#ff5c46')

    def clear_boxs(self):
        self.model_entry.delete(0, END)
        self.amoung_entry.delete(0,END)
        self.price_entry.delete(0,END)
        self.model = None

    def record_entry(self):
        model = self.model_entry.get()
        amoung = self.amoung_entry.get()
        price = self.price_entry.get()
        if model and amoung and price:
            if '-' in model:
                motor = Motor_cycle(model=model, amoung=int(amoung), price=float(price))
                return motor
            else:
                showwarning(title='', message='Check model')
        else:
                showwarning(title='Warning', message='Fill in every box')
                return None

    def add_new_motor(self):
        motor = self.record_entry()
        
        if self.model is not None:
            print(f'Im happing model {self.model}')
            System().update(motor=motor)
            self.load_table_data()
            showinfo(title='', message=f'{self.model}, was updated')
            self.clear_boxs()
        elif motor is not None:
            print('im happening motor----')
            System().insert(motor)
            self.load_table_data()
            showinfo(title='', message='Motor cycle was added.')
            self.clear_boxs()

        else:
             print('i am happing')

    def load_table_data(self):
        low_stock = []
        # Clear existing data
        for item in self.table_fm.get_children():
            self.table_fm.delete(item)
        
        # Load new data
        list_motor = System().select()
        for motor in list_motor:
            if motor.amoung < 20:
                self.table_fm.insert(parent='', index=END, values=motor, tags='low-stock')
                low_stock.append([motor.model, motor.amoung])
            else:
                self.table_fm.insert(parent='', index=END, values=motor)

        if low_stock is not None:
            self.send_email(low_stock)
        else:
            print('working')

    def record_table(self,event):
        info_select = self.table_fm.selection()
        if info_select:
            motor = self.table_fm.item(info_select)['values']
            
            self.clear_boxs()
            self.model = motor[0]
            self.model_entry.insert(END,motor[0])
            self.amoung_entry.insert(END,motor[1])
            self.price_entry.insert(END,motor[2])

    def delete_motor_cycle(self):
        if self.model is not None:
            motor = Motor_cycle(model=self.model)
            System().delete(motor=motor)
            self.load_table_data()
            showinfo(title='', message='Motor cycle was deleted.')
            self.clear_boxs()
            self.model = None
        else:
            showerror(title='', message='Select something first')

    def view_sell(self):
                self.withdraw()
                SellWindow(self)
        
    def close_button(self):
        CloseStore().close_store()
        self.clear_boxs()
        showinfo(title='', message='Finish every operation')
        self.destroy()

    def send_email(self, products):
        EMAIL_ADDRES = 'kolormi333@gmail.com'
        EMAIL_PASSWORD = 'dgus imaj xrvo fqsi'

        msg = EmailMessage()
        msg['subject'] = 'Hello mr.Francisco, I\'m Toro Storo'
        msg['From'] = EMAIL_ADDRES
        msg['To'] = EMAIL_ADDRES

        body = 'The following product is running low: \n\n'
        for name,stock in products:
            body += f'{name}:{stock} unit left\n'

        msg.set_content(body)


        try:
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(EMAIL_ADDRES, EMAIL_PASSWORD)
                smtp.send_message(msg)
        except Exception as e:
            print(f'Error ocurrered while we were sending an email: {e}')

if __name__ == '__main__':
    Windows().mainloop()