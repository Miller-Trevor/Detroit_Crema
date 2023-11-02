import tkinter as tk
from tkinter.ttk import *
from tkinter.font import Font
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import Setups as s
import Functions as f
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)
import CustomPlotMaker as m
from csv import DictWriter
#from matplotlib.backends.bd_tkagg import BackendFigureCanvasTkAgg

class WelcomePage(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Welcome")
        self.geometry("800x480")
        self.configure(bg = "#04043B")
        #self.attributes('-fullscreen', True)
        #self.heat_up_thread = s.threading.Thread(target = f.Heat_Up())
        #self.heat_up_thread.start()
        self.button_8_image = tk.PhotoImage(file=("button_8.png"))
        
        self.welcome_text = tk.Label(self, text="Welcome to the Magik Box", compound="center", font=("Arial", 50), bg= "#04043B", fg= "#ff8c00", pady=30).pack()
        
        self.button_8 = tk.Button(self, image=self.button_8_image, bg = "#04043B", highlightthickness= 0, borderwidth=0, command = lambda: [s.heat_up_flag == True, self.go_to_home_page()])
        self.button_8.place(x=277, y=244)
        
        # self.after(300000, self.destroy_window)

    def go_to_home_page(self):
        self.withdraw() 
        self.another_window = BrewProfileWindow(self)
    
    # def destroy_window(self):
    #     self.destroy()

#Home Page Class, first window to pop up
class DefaultTemps(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Home Page")
        #Set Dimensions of Window
        self.geometry("800x480")
        #Set Background of Window
        self.configure(bg = "#04043B")
        # Make Window Fullscreen
        #self.attributes('-fullscreen', True)
        
        #Import images to use 
        self.home_image = tk.PhotoImage(file=("image_1.png"))
        self.button_1_image = tk.PhotoImage(file=("button_1.png"))
        self.button_2_image = tk.PhotoImage(file=("button_2.png"))
        self.button_3_image = tk.PhotoImage(file=("button_3.png"))
        self.weight = tk.IntVar()
        
        #Create Label to hold the Logo
        tk.Label(self, image=self.home_image, borderwidth=0,compound="center",highlightthickness = 0, padx=0, pady=30).pack()
        #Dark Roast Button
        self.button_1 = tk.Button(self, image=self.button_1_image, bg= "#04043B", command = lambda: [self.set_dark_temp(), self.navigate_to_window(), self.get_weight_targ_val(), self.get_data()])
        self.button_1.place(x=150, y=380)
        #Medium Roast Button
        self.button_3 = tk.Button(self, image=self.button_3_image, bg= "#04043B", command = lambda: [self.set_med_temp(), self.navigate_to_window(), self.get_weight_targ_val(), self.get_data()])
        self.button_3.place(x=350, y=380)
        #Light Roast Button
        self.button_2 = tk.Button(self, image=self.button_2_image, bg= "#04043B", command = lambda: [self.set_light_temp(), self.navigate_to_window(), self.get_weight_targ_val(), self.get_data()])
        self.button_2.place(x=550, y=380)
        
        self.back_button = tk.Button(self, text="Back", command=self.go_back)
        self.back_button.place(x=20, y=20)
        
        self.weight_label = tk.Label(self, text="Enter Dry Weight (g)", font=("Arial", 15), bg= "#04043B", fg= "#ff8c00")
        self.weight_label.place(x = 300, y= 200)

        self.weight_entry = tk.Spinbox(self, textvariable= self.weight, width=5, from_=0, to=20, font=Font(size=28, weight='bold'))
        self.weight_entry.place(x= 350, y = 240)
        
        
        
    #Function to Navigate to The Brew Profile Window    
    def navigate_to_window(self):
        #Hide The Home Page
        self.withdraw() 
        # Go to The Brew Profile Window
        self.another_window = BrewWindow(self)
    def set_dark_temp(self):
        s.targ_temp = 90
    def set_med_temp(self):
        s.targ_temp = 93
    def set_light_temp(self):
        s.targ_temp = 96
    def get_weight_targ_val(self):
        s.targ_weight = self.weight.get() * 2
    def go_back(self):
        self.master.deiconify()
        self.withdraw()
    def get_data(self):
        field_names = ['Weight', 'Temp', 'Preinfuse Pressure', 'Preinfuse Time', 'Brew Time', 'Pressure Array', 'Time Array']
        data = {'Weight': s.targ_weight, 'Temp': s.targ_temp, 'Preinfuse Pressure': s.preinfuse_bar, 'Preinfuse Time': s.preinfuse_time, 'Brew Time': s.brew_time, 'Pressure Array': s.targ_pressure_arr, 'Time Array': s.targ_time_arr}
        with open('data1.csv', 'a') as f_object:
            dictwriter_object = DictWriter(f_object, fieldnames=field_names)
            dictwriter_object.writerow(data)
            f_object.close
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
        #self.attributes('-fullscreen', True)
        
        #Import and Place Logo
        self.home_image = tk.PhotoImage(file=("image_1.png"))
        tk.Label(self, image=self.home_image, borderwidth=0,compound="center",highlightthickness = 0, padx=0, pady=30).pack()
        
        # Display Text to show that the Machine is Brewing
        self.brew_text = tk.Label(self, text="Brewing...", font=("Arial", 30), bg= "#04043B", fg= "#ff8c00")
        self.brew_text.pack()
        
        
        # Schedule the go_to_home_page function to be called after 5000 milliseconds (5 seconds)
        self.after(5000, self.go_to_graph)
    
    def go_to_graph(self):  
        self.graph_show_page = ShowGraph(self)
        self.withdraw()
    
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
        #self.attributes('-fullscreen', True)
        
        # Import and Place the Logo
        self.home_image = tk.PhotoImage(file=("image_1.png"))
        tk.Label(self, image=self.home_image, borderwidth=0,compound="center",highlightthickness = 0, padx=0, pady=30).pack()
        
        # Display text to show that the Machine is Brewing
        self.brew_text = tk.Label(self, text="Brewing...", font=("Arial", 30), bg= "#04043B", fg = "#ff8c00")
        self.brew_text.pack()
        
        
        # Schedule the go_to_home_page function to be called after 5000 milliseconds (5 seconds)
        self.after(5000, self.go_to_graph)
    
    def go_to_graph(self):  
        self.graph_show_page = ShowGraph(self)
        self.withdraw()
        

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
        #self.attributes('-fullscreen', True)
        #print('Targ temp is {}'.format(s.targ_temp))
        #print('Targ Weight {} Preinfuse time {}'.format(s.targ_weight, s.preinfuse_time))
        # Import Logo and Button Images
        self.home_image = tk.PhotoImage(file=("image_1.png"))
        self.button_1_image = tk.PhotoImage(file=("button_4.png"))
        self.button_2_image = tk.PhotoImage(file=("button_5.png"))
        self.button_3_image = tk.PhotoImage(file=("button_6.png"))
        self.button_9_image = tk.PhotoImage(file=("button_9.png"))
        self.button_10_image = tk.PhotoImage(file=("button_10.png"))
        self.button_11_image = tk.PhotoImage(file=("button_11.png"))
        self.profile = tk.StringVar()
        
        # Place the Logo
        tk.Label(self, image=self.home_image, borderwidth=0,compound="center",highlightthickness = 0, padx=0, pady=30).pack()
        
        # Blooming Profile Button
        self.button_1 = tk.Button(self, image=self.button_1_image, bg= "#04043B", command= lambda: [self.profile == 'Blooming', self.go_to_default_temps(), self.set_blooming_plot()])
        self.button_1.place(x=550, y=150)
        # Custom Profile Button
        self.button_2 = tk.Button(self, image=self.button_2_image, bg= "#04043B", command=self.go_to_text_boxes)
        self.button_2.place(x=30, y=150)
        # Default Profile Button
        self.button_3 = tk.Button(self, image=self.button_3_image, bg= "#04043B", command= lambda: [self.profile == 'Default', self.go_to_default_temps(), self.set_default_plot()])
        self.button_3.place(x=290, y=150)
        # 4th Button
        self.button_4 = tk.Button(self, image=self.button_11_image, bg= "#04043B", command= lambda: [self.profile == 'Blooming Allonge', self.go_to_default_temps(), self.set_bloomingallonge_plot()])
        self.button_4.place(x=150, y=250)
        # 5th Button
        self.button_5 = tk.Button(self, image=self.button_10_image, bg= "#04043B", command= lambda: [self.profile == 'Allonge', self.go_to_default_temps(), self.set_allonge_plot()])
        self.button_5.place(x=420, y=250)
        
        self.purge_button = tk.Button(self, image=self.button_9_image, bg= "#04043B")
        self.purge_button.place(x = 280, y = 380)


    # Function to go to Brew Window
    def go_to_default_temps(self):
        # Go to Brew Window
        self.default_temps = DefaultTemps(self)
        # Hide Brew Profile Window
        self.withdraw()
    def set_default_plot(self):
        s.targ_time_arr, s.targ_pressure_arr = [0,8,13.5,19,24.5,30], [1,1,9,9,9,9] 
        s.preinfuse_time = 8
        s.preinfuse_bar = 1
        s.brew_time = 30
    def set_blooming_plot(self):
        s.targ_time_arr, s.targ_pressure_arr = [0,8,13.5,19,24.5,35], [3,3,9,9,0,0]
        s.preinfuse_time = 8
        s.preinfuse_bar = 3
        s.brew_time = 35
    def set_bloomingallonge_plot(self):
        s.targ_time_arr, s.targ_pressure_arr = [0,10,20,30,40,50], [1,1,2,2,2,1]
        s.preinfuse_time = 10
        s.preinfuse_bar = 1
        s.brew_time = 50
    def set_allonge_plot(self):
        s.targ_time_arr, s.targ_pressure_arr = [0,8,13.5,19,24.5,30], [1,1,1,1,1,1,1]
        s.preinfuse_time = 8
        s.preinfuse_bar = 1
        s.brew_time = 30
            

        #self.delta_t_brew = int((s.brew_time - s.preinfuse_time)/5)
        # s.targ_time_arr, s.targ_pressure_arr = m.get_point_data()
    # Function to go to the Custom Brew Window
    def go_to_text_boxes(self):
        # Go to Custom Profile Window
        self.text_boxes = TextBoxes(self)
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
        #self.attributes('-fullscreen', True)
        #s = ttk.Style()
        #s.configure('Vertical.TScale', background= '#04043B')
        
        # Import Logo and Buttom Image
        self.home_image = tk.PhotoImage(file=("image_1.png"))
        self.button_7_image = tk.PhotoImage(file=("button_7.png"))
        self.button_1_image = tk.PhotoImage(file=("button_1.png"))
        self.button_2_image = tk.PhotoImage(file=("button_2.png"))
        self.button_3_image = tk.PhotoImage(file=("button_3.png"))
        
        
        
            
        # Place Logo 
        # tk.Label(self, image=self.home_image, borderwidth=0,compound="center",highlightthickness = 0, padx=0, pady=30).pack()
        self.canvas = FigureCanvasTkAgg(m.make_plot(s.brew_time, s.preinfuse_time, s.preinfuse_bar),
                            master = self)  
        print("plot made")
        self.canvas.draw()
        print("drawing")
        # placing the canvas on the Tkinter window
        self.canvas.get_tk_widget().pack()
        print("canvas packed")

        # creating the Matplotlib toolbar
        self.toolbar = NavigationToolbar2Tk(self.canvas,
                                self, pack_toolbar = False)
        print("toolbar made")
        self.toolbar.update()
        print("updated")

        # placing the toolbar on the Tkinter window
        # self.canvas.get_tk_widget().pack()
        #print('canvas packed')
        
        # Create Button to submit values and go to Brew Page
        # self.button_1 = tk.Button(self, image=self.button_1_image, bg= "#04043B", command=self.go_to_brew_page)
        # self.button_1.place(x=30, y=30)
        
        self.button_1 = tk.Button(self, image=self.button_1_image, bg= "#04043B", command = lambda: [self.set_dark_temp(), self.go_to_brew_page(), self.get_data()])
        self.button_1.place(x=150, y=380)
        #Medium Roast Button
        self.button_2 = tk.Button(self, image=self.button_3_image, bg= "#04043B", command = lambda: [self.set_med_temp(), self.go_to_brew_page(), self.get_data()])
        self.button_2.place(x=350, y=380)
        #Light Roast Button
        self.button_2 = tk.Button(self, image=self.button_2_image, bg= "#04043B", command = lambda: [self.set_light_temp(), self.go_to_brew_page(), self.get_data()])
        self.button_2.place(x=550, y=380)

        self.back_button = tk.Button(self, text="Back", command= self.go_back)
        self.back_button.place(x=20, y=20)
        
        
        #self.button_1 = tk.Button(self, image=self.button_1_image, bg= "#04043B", command=self.reload_window)
        #self.button_1.place(x=550, y= 30)
    

    def go_to_graph_page(self):
        self.set_plot_arrs()
        #print('time: {} pressure: {}'.format(s.targ_time_arr, s.targ_pressure_arr))
        s.profile.create_plot(s.targ_time_arr, s.targ_pressure_arr)
        # Go to Custom Profile Window
        #self.graph_page = GraphWindow(self)
        # Hide Brew Profile Window
        self.withdraw()
        
    def set_plot_arrs(self):
        #self.delta_t_brew = int((s.brew_time - s.preinfuse_time)/5)
        s.targ_time_arr, s.targ_pressure_arr = m.get_point_data()
        s.profile.create_plot(s.targ_time_arr, s.targ_pressure_arr)
    # Function to submit values and go to brew page
    def go_to_brew_page(self):
        self.set_plot_arrs()
        # Go to Brew Page
        self.brew_window = BrewCustWindow(self)
        # Hide Custom Profile Window
        self.withdraw()
    def set_dark_temp(self):
        s.targ_temp = 90
    def set_med_temp(self):
        s.targ_temp = 93
    def set_light_temp(self):
        s.targ_temp = 96
    def go_back(self):
        m.listLabelPoints.clear()
        self.set_plot_arrs()
        self.master.deiconify()
        self.withdraw()
    def get_data(self):
        field_names = ['Weight', 'Temp', 'Preinfuse Pressure', 'Preinfuse Time', 'Brew Time', 'Pressure Array', 'Time Array']
        data = {'Weight': s.targ_weight, 'Temp': s.targ_temp, 'Preinfuse Pressure': s.preinfuse_bar, 'Preinfuse Time': s.preinfuse_time, 'Brew Time': s.brew_time, 'Pressure Array': s.targ_pressure_arr, 'Time Array': s.targ_time_arr}
        with open('data1.csv', 'a') as f_object:
            dictwriter_object = DictWriter(f_object, fieldnames=field_names)
            dictwriter_object.writerow(data)
            f_object.close
        #df.to_csv('C:/Users/tmiller4/Desktop/DetroitCremaGUI/DetroitCremaGUI/data/data1.csv')
class TextBoxes(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title(("Customize Your Profile"))
        # Set Window Dimensions
        self.geometry("800x480")
        # Set Window Background
        self.configure(bg = "#04043B")
        # Make Window Fullscreen
        #self.attributes('-fullscreen', True)
        
        self.preinfuse_time = tk.IntVar()  
        self.preinfuse_bar = tk.IntVar()  
        self.brew_time = tk.IntVar()                                                                                                                                            
        self.weight = tk.IntVar()
        self.home_image = tk.PhotoImage(file=("image_1.png"))
        
        tk.Label(self, image=self.home_image, borderwidth=0,compound="center",highlightthickness = 0, padx=0, pady=30).pack()
        
        self.preinfuse_label = tk.Label(self, text="Set Preinfuse Time (sec)", font=("Arial", 15), bg= "#04043B", fg= "#ff8c00")
        self.preinfuse_label.place(x= 50, y = 150)

        self.preinfuse_entry = tk.Spinbox(self, textvariable = self.preinfuse_time, width=5, from_=0, to=30, font=Font(size=28, weight='bold'))
        self.preinfuse_entry.place(x = 100, y = 190)

        self.preinfuse_bar_label = tk.Label(self, text="Set Preinfuse Pressure (Bar)", font=("Arial", 15), bg= "#04043B", fg= "#ff8c00")
        self.preinfuse_bar_label.place(x = 300, y= 150)

        self.preinfuse_bar_entry = tk.Spinbox(self, textvariable= self.preinfuse_bar, width=5, from_=0, to=20, font=Font(size=28, weight='bold'))
        self.preinfuse_bar_entry.place(x= 350, y = 190)
        
        self.brew_time_label = tk.Label(self, text="Set Total Brew Time (sec)", font=("Arial", 15), bg= "#04043B", fg= "#ff8c00")
        self.brew_time_label.place(x = 50, y= 300)

        self.brew_time_entry = tk.Spinbox(self, textvariable= self.brew_time, width=5, from_=0, to=60, font=Font(size=28, weight='bold'))
        self.brew_time_entry.place(x= 100, y = 340)
        
        self.weight_label = tk.Label(self, text="Enter Dry Weight (g)", font=("Arial", 15), bg= "#04043B", fg= "#ff8c00")
        self.weight_label.place(x = 300, y= 300)

        self.weight_entry = tk.Spinbox(self, textvariable= self.weight, width=5, from_=0, to=20, font=Font(size=28, weight='bold'))
        self.weight_entry.place(x= 350, y = 340)
        
        self.cust_button = tk.Button(self, text="Next", command= lambda: [self.get_pre_val(), self.get_weight_targ_val(), self.get_pre_bar(), self.get_brew_time(), self.go_to_cust_page()])
        self.cust_button.place(x = 550, y=425)
        
        self.back_button = tk.Button(self, text="Back", command=self.go_back)
        self.back_button.place(x=20, y=20)
        
        
    def go_to_cust_page(self):
        self.cust_page = CustomizeWindow(self)
        self.withdraw()
    def get_pre_val(self):
        s.preinfuse_time = self.preinfuse_time.get()
    def get_weight_targ_val(self):
        s.targ_weight = self.weight.get() * 2
    def get_pre_bar(self):
        s.preinfuse_bar = self.preinfuse_bar.get()
    def get_brew_time(self):
        s.brew_time = self.brew_time.get()
    def go_back(self):
        self.master.deiconify()
        self.withdraw()

class ShowGraph(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title(("Customize Your Profile"))
        # Set Window Dimensions
        self.geometry("800x480")
        # Set Window Background
        self.configure(bg = "#04043B")
        # Make Window Fullscreen
        #self.attributes('-fullscreen', True)
        self.home_image = tk.PhotoImage(file=("image_1.png"))
        # self.currentBrewImage = tk.PhotoImage(file=("BrewGraph.png"))
        tk.Label(self, image=self.home_image, borderwidth=0,compound="center",highlightthickness = 0, padx=0, pady=30).pack()
        
        self.return_button = tk.Button(self, text="Home Page", command=self.go_to_home_page)
        self.return_button.place(x=20, y=20)
        # tk.Label(self, image=self.currentBrewImage, borderwidth=0,compound="center",highlightthickness = 0, padx=0, pady=30).pack()
    def go_to_home_page(self):
        self.home_page = BrewProfileWindow(self)
        self.withdraw()
        
# Main Function
if __name__ == "__main__":
    # On Load the Home Page is shown
    app = WelcomePage()
    # App stops at mainloop
    app.mainloop()
