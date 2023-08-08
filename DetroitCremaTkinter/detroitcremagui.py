import tkinter as tk
from tkinter import *

class HomePage(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Home Page")
        self.geometry("800x480")
        self.configure(bg = "#04043B")

        self.home_image = tk.PhotoImage(file=("image_1.png"))
        self.button_1_image = tk.PhotoImage(file=("button_1.png"))
        self.button_2_image = tk.PhotoImage(file=("button_2.png"))
        self.button_3_image = tk.PhotoImage(file=("button_3.png"))

        tk.Label(self, image=self.home_image, borderwidth=0,compound="center",highlightthickness = 0, padx=0, pady=30).pack()
        self.button_1 = tk.Button(self, image=self.button_1_image, bg= "#04043B", command=self.navigate_to_window)
        self.button_1.place(x=550, y=150)

        self.button_2 = tk.Button(self, image=self.button_3_image, bg= "#04043B", command=self.navigate_to_window)
        self.button_2.place(x=550, y=250)

        self.button_2 = tk.Button(self, image=self.button_2_image, bg= "#04043B", command=self.navigate_to_window)
        self.button_2.place(x=550, y=350)
        
    def navigate_to_window(self):
        self.withdraw()  # Hide the home page
        self.another_window = BrewProfileWindow(self)

class BrewWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Another Window")
        self.geometry("800x480")
        self.configure(bg = "#04043B")

        self.home_image = tk.PhotoImage(file=("image_1.png"))
        tk.Label(self, image=self.home_image, borderwidth=0,compound="center",highlightthickness = 0, padx=0, pady=30).pack()

        self.brew_text = tk.Label(self, text="Brewing...", font=("Arial", 30), bg= "#04043B", fg= "#ff8c00")
        self.brew_text.pack()


        # Schedule the go_to_home_page function to be called after 5000 milliseconds (5 seconds)
        self.after(5000, self.go_to_home_page)

    def go_to_home_page(self):
        self.destroy()  # Close the secondary window
        self.master.master.deiconify()  # Show the home page

class BrewCustWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Another Window")
        self.geometry("800x480")
        self.configure(bg = "#04043B")

        self.home_image = tk.PhotoImage(file=("image_1.png"))
        tk.Label(self, image=self.home_image, borderwidth=0,compound="center",highlightthickness = 0, padx=0, pady=30).pack()

        self.brew_text = tk.Label(self, text="Brewing...", font=("Arial", 30), bg= "#04043B", fg = "#ff8c00")
        self.brew_text.pack()


        # Schedule the go_to_home_page function to be called after 5000 milliseconds (5 seconds)
        self.after(5000, self.go_to_home_page)

    def go_to_home_page(self):
        self.destroy()  # Close the secondary window
        self.master.master.master.deiconify()

class BrewProfileWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title(("Brew Profile Selection"))
        self.geometry("800x480")
        self.configure(bg = "#04043B")

        self.home_image = tk.PhotoImage(file=("image_1.png"))
        self.button_1_image = tk.PhotoImage(file=("button_4.png"))
        self.button_2_image = tk.PhotoImage(file=("button_5.png"))
        self.button_3_image = tk.PhotoImage(file=("button_6.png"))

        tk.Label(self, image=self.home_image, borderwidth=0,compound="center",highlightthickness = 0, padx=0, pady=30).pack()

        self.button_1 = tk.Button(self, image=self.button_1_image, bg= "#04043B", command=self.go_to_brew_page)
        self.button_1.place(x=550, y=150)

        self.button_2 = tk.Button(self, image=self.button_2_image, bg= "#04043B", command=self.go_to_cust_page)
        self.button_2.place(x=50, y=200)

        self.button_3 = tk.Button(self, image=self.button_3_image, bg= "#04043B", command=self.go_to_brew_page)
        self.button_3.place(x=550, y=250)
    
    def go_to_brew_page(self):
        self.brew_window = BrewWindow(self)
        self.withdraw()
    def go_to_cust_page(self):
        self.cust_page = CustomizeWindow(self)
        self.withdraw()

class CustomizeWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title(("Customize Your Profile"))
        self.geometry("800x480")
        self.configure(bg = "#04043B")

        self.home_image = tk.PhotoImage(file=("image_1.png"))
        self.button_1_image = tk.PhotoImage(file=("button_7.png"))

        time_1 = tk.StringVar()
        time_2 = tk.StringVar()
        time_3 = tk.StringVar()
        time_4 = tk.StringVar()
        time_5 = tk.StringVar()
        ss1 = tk.StringVar()
        ss2 = tk.StringVar()
        ss3 = tk.StringVar()
        ss4 = tk.StringVar()
        ss5 = tk.StringVar()

        tk.Label(self, image=self.home_image, borderwidth=0,compound="center",highlightthickness = 0, padx=0, pady=30).pack()

        s1 = Scale(self, from_=0, to=10, bg= "#ff8c00", bd=1, variable=ss1, troughcolor= "#04043B")
        s1.set(5)
        s1.place(x=20, y=150)
        s2 = Scale(self, from_=0, to=10, bg= "#ff8c00", bd=1, variable= ss2, troughcolor= "#04043B")
        s2.set(5)
        s2.place(x=180, y=150)
        s3 = Scale(self, from_=0, to=10, bg= "#ff8c00", bd=1, variable= ss3, troughcolor= "#04043B")
        s3.set(5)
        s3.place(x=340, y=150)
        s4 = Scale(self, from_=0, to=10, bg= "#ff8c00", bd=1, variable = ss4, troughcolor= "#04043B")
        s4.set(5)
        s4.place(x=500, y=150)
        s5 = Scale(self, from_=0, to=10, bg= "#ff8c00", bd=1, variable = ss5, troughcolor= "#04043B")
        s5.set(5)
        s5.place(x=660, y=150)

        t1 = tk.Entry(self, textvariable = time_1, width=7)
        t2 = tk.Entry(self, textvariable = time_2, width=7)
        t3 = tk.Entry(self, textvariable = time_3, width=7)
        t4 = tk.Entry(self, textvariable = time_4, width=7)
        t5 = tk.Entry(self, textvariable = time_5, width=7)

        t1.place(x= 20, y= 260)
        t2.place(x= 180, y= 260)
        t3.place(x= 340, y = 260)
        t4.place(x= 500, y= 260)
        t5.place(x = 660, y= 260)

        Label(self, text=ss1.get()).pack()
        Label(self, text=ss2.get()).pack()
        Label(self, text=ss3.get()).pack()
        Label(self, text=ss4.get()).pack()
        Label(self, text=ss5.get()).pack()
    

        self.button_1 = tk.Button(self, image=self.button_1_image, bg= "#04043B", command=self.go_to_brew_page)
        self.button_1.place(x=300, y=360)

    def go_to_brew_page(self):
        self.brew_window = BrewCustWindow(self)
        self.withdraw()
if __name__ == "__main__":
    app = HomePage()
    app.mainloop()

