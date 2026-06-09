import os
import sys
from tkinter import PhotoImage, Tk
from tkinter.constants import N, NSEW
from tkinter.messagebox import showinfo, showwarning
from tkinter import ttk

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from GUI.Toro_interface import Windows


class LogIn(Tk):
    def __init__(self):
        super().__init__()
        self.styles_c()
        self.configure_layout()
        self.frame_log()
        self.labels()
        self.entris()
        self.buttons()

    def configure_layout(self):
        self.geometry("800x500")
        self.title("Sing In")
        self.config(bg="#ff5c46")

        self.columnconfigure(0, weight=2)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=2)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=5)
        self.rowconfigure(2, weight=2)

    def styles_c(self):
        self.style = ttk.Style()

        self.style.configure("TFrame", background="#ac4537")
        self.style.configure("TEntry", fieldbackground="#882013", foreground="white")

        self.style.configure("TLabel", background="#ac4537", font=("Mono space", 12))

        self.style.configure("TButton", background="#ac4537")
        self.style.map(
            "TButton",
            background=[("active", "#6e2319")],
            foreground=[("active", "white")],
        )

    def labels(self):

        self.img = PhotoImage(file="logo/torott.png").subsample(3)
        self.logo = ttk.Label(self.log_contanier, image=self.img)
        self.logo.grid(row=0, column=0, sticky=N)

    def frame_log(self):
        self.log_contanier = ttk.Frame(self, style="TFrame")

        self.log_contanier.grid(row=1, column=1, sticky=NSEW)
        self.log_contanier.rowconfigure(0, weight=1)
        self.log_contanier.rowconfigure(1, weight=2)
        self.log_contanier.rowconfigure(2, weight=2)
        self.log_contanier.rowconfigure(3, weight=2)
        self.log_contanier.columnconfigure(0, weight=1)

    def entris(self):
        self.entry_user = ttk.Entry(self.log_contanier)
        self.entry_user.grid(row=1, column=0)
        self.user_label = ttk.Label(self.log_contanier, text="User:", style="TLabel")
        self.user_label.grid(row=1, column=0, sticky=N)

        self.entry_password = ttk.Entry(self.log_contanier, show="*")
        self.entry_password.grid(row=2, column=0)
        self.password_label = ttk.Label(
            self.log_contanier, text="Password:", style="TLabel"
        )
        self.password_label.grid(row=2, column=0, sticky=N)

    def buttons(self):
        self.button_enter = ttk.Button(
            self.log_contanier, text="Enter", style="TButton", command=self.get_info
        )
        self.button_enter.grid(row=3, column=0)

    def get_info(self):
        user = self.entry_user.get()
        password = self.entry_password.get()

        if user and password:
            return self.valid_info(user=user, password=password)
        else:
            showwarning(title="", message="First fill in every box")

    def valid_info(self, user, password):

        if user == "admin" and password == "12345678":
            showinfo(title="", message="Information is correct")
            self.destroy()
            Windows()
        else:
            showwarning(title="", message="Information is wrong")


if __name__ == "__main__":
    LogIn().mainloop()
