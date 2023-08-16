import tkinter as tk
from tkinter import *
from tkinter.ttk import *
import tkinter.ttk as ttk
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class WelcomePage(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Welcome")
        self.geometry("800x480")
        self.configure(bg = "#04043B")
        #self.attributes('-fullscreen', True)

        self.button_8_image = tk.PhotoImage(file=("button_8.png"))

        self.welcome_text = tk.Label(self, text="Welcome to the Magik Box", compound="center", font=("Arial", 50), bg= "#04043B", fg= "#ff8c00", pady=30).pack()

        self.button_8 = tk.Button(self, image=self.button_8_image, bg = "#04043B", highlightthickness= 0, borderwidth=0, command=self.go_to_home_page)
        self.button_8.place(x=277, y=244)

        self.after(300000, self.destroy_window)

    def go_to_home_page(self):
        self.withdraw() 
        self.another_window = HomePage(self)

    def destroy_window(self):
        self.destroy()


#Home Page Class, first window to pop up
class HomePage(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Home Page")
        #Set Dimensions of Window
        self.geometry("800x480")
        #Set Background of Window
        self.configure(bg = "#04043B")
        # Make Window Fullscreen
        self.attributes('-fullscreen', True)

        #Import images to use 
        self.home_image = tk.PhotoImage(file=("image_1.png"))
        self.button_1_image = tk.PhotoImage(file=("button_1.png"))
        self.button_2_image = tk.PhotoImage(file=("button_2.png"))
        self.button_3_image = tk.PhotoImage(file=("button_3.png"))

        #Create Label to hold the Logo
        tk.Label(self, image=self.home_image, borderwidth=0,compound="center",highlightthickness = 0, padx=0, pady=30).pack()
        #Dark Roast Button
        self.button_1 = tk.Button(self, image=self.button_1_image, bg= "#04043B", command=self.navigate_to_window)
        self.button_1.place(x=550, y=150)
        #Medium Roast Button
        self.button_2 = tk.Button(self, image=self.button_3_image, bg= "#04043B", command=self.navigate_to_window)
        self.button_2.place(x=550, y=250)
        #Light Roast Button
        self.button_2 = tk.Button(self, image=self.button_2_image, bg= "#04043B", command=self.navigate_to_window)
        self.button_2.place(x=550, y=350)
    #Function to Navigate to The Brew Profile Window    
    def navigate_to_window(self):
        #Hide The Home Page
        self.withdraw() 
        # Go to The Brew Profile Window
        self.another_window = BrewProfileWindow(self)

#Brew Profile Window Class
class BrewWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Another Window")
        # Set Window Size
        self.geometry("800x480")
        # Set Window Background Color
        self.configure(bg = "#04043B")
        # Make Window Fullscreen
        self.attributes('-fullscreen', True)

        #Import and Place Logo
        self.home_image = tk.PhotoImage(file=("image_1.png"))
        tk.Label(self, image=self.home_image, borderwidth=0,compound="center",highlightthickness = 0, padx=0, pady=30).pack()

        # Display Text to show that the Machine is Brewing
        self.brew_text = tk.Label(self, text="Brewing...", font=("Arial", 30), bg= "#04043B", fg= "#ff8c00")
        self.brew_text.pack()


        # Schedule the go_to_home_page function to be called after 5000 milliseconds (5 seconds)
        self.after(5000, self.go_to_home_page)

    def go_to_home_page(self):
        self.destroy()  # Close the secondary window
        self.master.master.deiconify()  # Show the home page

# Custom Brewing Window, Had to make this a seperate class due to poor navigation by Tkinter
class BrewCustWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Another Window")
        # Set Window Dimesions
        self.geometry("800x480")
        # Set Background Color of the Window
        self.configure(bg = "#04043B")
        # Make Window Fullscreen
        self.attributes('-fullscreen', True)

        # Import and Place the Logo
        self.home_image = tk.PhotoImage(file=("image_1.png"))
        tk.Label(self, image=self.home_image, borderwidth=0,compound="center",highlightthickness = 0, padx=0, pady=30).pack()

        # Display text to show that the Machine is Brewing
        self.brew_text = tk.Label(self, text="Brewing...", font=("Arial", 30), bg= "#04043B", fg = "#ff8c00")
        self.brew_text.pack()


        # Schedule the go_to_home_page function to be called after 5000 milliseconds (5 seconds)
        self.after(5000, self.go_to_home_page)

    def go_to_home_page(self):
        self.destroy()  # Close the secondary window
        self.master.master.master.deiconify() # Navigate back to Home Page, each Master navigates back one window


# Brew Profile window to select the type of Profile the User Wants to use
class BrewProfileWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title(("Brew Profile Selection"))
        # Set Window Dimensions
        self.geometry("800x480")
        # Set the Background Color of Window
        self.configure(bg = "#04043B")
        # Make Window Fullscreen
        self.attributes('-fullscreen', True)

        # Import Logo and Button Images
        self.home_image = tk.PhotoImage(file=("image_1.png"))
        self.button_1_image = tk.PhotoImage(file=("button_4.png"))
        self.button_2_image = tk.PhotoImage(file=("button_5.png"))
        self.button_3_image = tk.PhotoImage(file=("button_6.png"))

        # Place the Logo
        tk.Label(self, image=self.home_image, borderwidth=0,compound="center",highlightthickness = 0, padx=0, pady=30).pack()

        # Blooming Profile Button
        self.button_1 = tk.Button(self, image=self.button_1_image, bg= "#04043B", command=self.go_to_brew_page)
        self.button_1.place(x=550, y=150)
        # Custom Profile Button
        self.button_2 = tk.Button(self, image=self.button_2_image, bg= "#04043B", command=self.go_to_cust_page)
        self.button_2.place(x=50, y=200)
        # Default Profile Button
        self.button_3 = tk.Button(self, image=self.button_3_image, bg= "#04043B", command=self.go_to_brew_page)
        self.button_3.place(x=550, y=250)
    
    # Function to go to Brew Window
    def go_to_brew_page(self):
        # Go to Brew Window
        self.brew_window = BrewWindow(self)
        # Hide Brew Profile Window
        self.withdraw()

    # Function to go to the Custom Brew Window
    def go_to_cust_page(self):
        # Go to Custom Profile Window
        self.cust_page = CustomizeWindow(self)
        # Hide Brew Profile Window
        self.withdraw()

# Custom Profile Making Window
class CustomizeWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title(("Customize Your Profile"))
        # Set Window Dimensions
        self.geometry("800x480")
        # Set Window Background
        self.configure(bg = "#04043B")
        # Make Window Fullscreen
        self.attributes('-fullscreen', True)
        s = ttk.Style()
        s.configure('Vertical.TScale', background= '#04043B')

        # Import Logo and Buttom Image
        self.home_image = tk.PhotoImage(file=("image_1.png"))
        self.button_1_image = tk.PhotoImage(file=("button_7.png"))

        # Set Variables of Pressure and Time to be passed to the Brewing Functions
        self.time_1 = tk.IntVar()
        self.time_2 = tk.IntVar()
        self.time_3 = tk.IntVar()
        self.time_4 = tk.IntVar()
        self.time_5 = tk.IntVar()
        self.ss1 = tk.IntVar()
        self.ss2 = tk.IntVar()
        self.ss3 = tk.IntVar()
        self.ss4 = tk.IntVar()
        self.ss5 = tk.IntVar()

        def getSS1():
            return (self.ss1.get())
        def getSS2():
            return (self.ss2.get())
        def getSS3():
            return (self.ss3.get())
        def getSS4():
            return (self.ss4.get())
        def getSS5():
            return (self.ss5.get())
        
        self.s1_value = tk.Label(self, text=getSS1(), bg="#04043B", fg="#ff8c00", font="Arial 15 bold")
        self.s2_value = tk.Label(self, text=getSS2(), bg="#04043B", fg="#ff8c00", font="Arial 15 bold")
        self.s3_value = tk.Label(self, text=getSS3(), bg="#04043B", fg="#ff8c00", font="Arial 15 bold")
        self.s4_value = tk.Label(self, text=getSS4(), bg="#04043B", fg="#ff8c00", font="Arial 15 bold")
        self.s5_value = tk.Label(self, text=getSS5(), bg="#04043B", fg="#ff8c00", font="Arial 15 bold")

        self.s1_value.place(x= 20, y = 300)
        self.s2_value.place(x= 180, y = 300)
        self.s3_value.place(x = 340, y = 300)
        self.s4_value.place(x = 500, y = 300)
        self.s5_value.place(x = 660, y = 300)


        def slider_changed(event):
            self.s1_value.configure(text=getSS1())
            self.s2_value.configure(text=getSS2())
            self.s3_value.configure(text=getSS3())
            self.s4_value.configure(text=getSS4())
            self.s5_value.configure(text=getSS5())

        # Place Logo 
        tk.Label(self, image=self.home_image, borderwidth=0,compound="center",highlightthickness = 0, padx=0, pady=30).pack()

        # Create Sliders from 1-10 for user to input Pressure at 5 points of time, Place Sliders
        s1 = ttk.Scale(self, from_=0, to=10, variable= self.ss1, cursor="dot", style='Vertical.TScale', orient= "vertical", command=slider_changed)
        s1.set(5)
        s1.place(x=20, y=150)
        s2 = ttk.Scale(self, from_=0, to=10, variable= self.ss2, cursor="dot", style='Vertical.TScale', orient= "vertical", command=slider_changed)
        s2.set(5)
        s2.place(x=180, y=150)
        s3 = ttk.Scale(self, from_=0, to=10, variable= self.ss3, cursor="dot", style='Vertical.TScale', orient= "vertical", command=slider_changed)
        s3.set(5)
        s3.place(x=340, y=150)
        s4 = ttk.Scale(self, from_=0, to=10, variable = self.ss4, cursor="dot", style='Vertical.TScale', orient= "vertical", command=slider_changed)
        s4.set(5)
        s4.place(x=500, y=150)
        s5 = ttk.Scale(self, from_=0, to=10, variable = self.ss5, cursor="dot", style='Vertical.TScale', orient= "vertical", command=slider_changed)
        s5.set(5)
        s5.place(x=660, y=150)

        # Create Entry's for user to set a time for each Pressure to be hit
        t1 = tk.Entry(self, textvariable = self.time_1, width=7)
        t2 = tk.Entry(self, textvariable = self.time_2, width=7)
        t3 = tk.Entry(self, textvariable = self.time_3, width=7)
        t4 = tk.Entry(self, textvariable = self.time_4, width=7)
        t5 = tk.Entry(self, textvariable = self.time_5, width=7)



        # Place the Entry boxes
        t1.place(x= 20, y= 260)
        t2.place(x= 180, y= 260)
        t3.place(x= 340, y = 260)
        t4.place(x= 500, y= 260)
        t5.place(x = 660, y= 260)

        # Create Button to submit values and go to Brew Page
        self.button_1 = tk.Button(self, image=self.button_1_image, bg= "#04043B", command=self.go_to_brew_page)
        self.button_1.place(x=300, y=360)

        self.button_1 = tk.Button(self, image=self.button_1_image, bg= "#04043B", command=self.go_to_graph_page)
        self.button_1.place(x=500, y=360)

    
    def go_to_graph_page(self):
        # Go to Custom Profile Window
        self.graph_page = GraphWindow(self)
        # Hide Brew Profile Window
        self.withdraw()
        
    # Function to submit values and go to brew page
    def go_to_brew_page(self):
        # Go to Brew Page
        self.brew_window = BrewCustWindow(self)
        # Hide Custom Profile Window
        self.withdraw()
        # Print Statements to show that values are being set on submit
        print("Pressures:")
        print(self.ss1.get())
        print(self.ss2.get())
        print(self.ss3.get())
        print(self.ss4.get())
        print(self.ss5.get())
        print("times:")
        print(self.time_1.get())
        print(self.time_2.get())
        print(self.time_3.get())
        print(self.time_4.get())
        print(self.time_5.get())
    """ def graph(self):
       y_axis = [self.ss1.get(), self.ss2.get(), self.ss3.get(), self.ss4.get(), self.ss5.get()]
       x_axis = [self.time_1.get(), self.time_2.get(), self.time_3.get(), self.time_4.get(), self.time_5.get()]

       plt.plot(x_axis, y_axis)
       plt.title('Pressure vs. Time')
       plt.xlabel('Time')
       plt.ylabel('Pressure')
       plt.show() """
    
class GraphWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title(("Customize Your Profile"))
        # Set Window Dimensions
        self.geometry("800x480")
        # Set Window Background
        self.configure(bg = "#04043B")
        # Make Window Fullscreen
        self.attributes('-fullscreen', True)
        # Import Logo and Buttom Image
        self.button_1_image = tk.PhotoImage(file=("button_7.png"))
        self.home_image = tk.PhotoImage(file=("image_1.png"))
        tk.Label(self, image=self.home_image, borderwidth=0,compound="center",highlightthickness = 0, padx=0, pady=30).pack()

        data = {'year': [1920, 1930, 1049, 1950, 1960, 1970, 1980, 1990, 2000, 2010],
                'unemployment_rate': [9.8, 12, 8, 7.2, 6.9, 7, 6.5, 6.2, 5.5, 6.3]}
        
        dataframe = pd.DataFrame(data)
        figure = plt.Figure(figsize=(5,4), dpi=100)
        figure_plot = figure.add_subplot(1, 1, 1)
        figure_plot.set_ylabel('Unemployment Rate')
        line_graph = FigureCanvasTkAgg(figure, self)
        line_graph.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
        dataframe = data[['year', 'unemployment_rate']].groupby('year'),sum()
        dataframe.plot(kind='line', legend=True, ax=figure_plot, color='r', marker='o', fontsize=10)
        figure_plot.set_title('Year vs. Unemployment Rate')

        self.button_1 = tk.Button(self, image=self.button_1_image, bg= "#04043B", command=self.go_to_brew_page)
        self.button_1.place(x=300, y=360)

    def go_to_brew_page(self):
        # Go to Brew Page
        self.brew_window = BrewCustWindow(self)
        # Hide Custom Profile Window
        self.withdraw()


# Main Function
if __name__ == "__main__":
    # On Load the Home Page is shown
    app = WelcomePage()
    # App stops at mainloop
    app.mainloop()
