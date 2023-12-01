#imports
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


#first page with start button on it and "Welcome to Detroit Crema" uses tk.tk because it is the base class, every other class is based off of this one
class WelcomePage(tk.Tk):
    #main function, need to define as self so that all variables defined in here can be used in here
    def __init__(self):
        #Nothing in init parentheses because it is the base class
        super().__init__()
        #title at top of window
        self.title("Welcome")
        #how big the window is, x by y
        self.geometry("800x480")
        #Background color of entire window
        self.configure(bg = "#04043B")
        #uncomment fullscreen when on the Pi, makes it fullscreen
        #self.attributes('-fullscreen', True)
        #self.heat_up_thread = s.threading.Thread(target = f.Heat_Up())
        #self.heat_up_thread.start()
        
        #import the power button image
        self.button_8_image = tk.PhotoImage(file=("button_8.png"))
        #create the Welcome to the Magik Box text
        self.welcome_text = tk.Label(self, text="Welcome to the Magik Box", compound="center", font=("Arial", 50), bg= "#04043B", fg= "#ff8c00", pady=30).pack()
        #create a button for the power button and use the power button image
        self.button_8 = tk.Button(self, image=self.button_8_image, bg = "#04043B", highlightthickness= 0, borderwidth=0, command = lambda: [s.heat_up_flag == True, self.go_to_home_page()])
        #places the button on x and y coordinate
        self.button_8.place(x=277, y=244)
        
        # self.after(300000, self.destroy_window)
    #goes the the home page after power button is pressed
    def go_to_home_page(self):
        #withdraws current window
        self.withdraw() 
        #self.another_window takes you to whatever window you specify after the = sign
        self.another_window = BrewProfileWindow(self)
    
    # def destroy_window(self):
    #     self.destroy()

#page that shows after a default profile (not custom) is chosen
class DefaultTemps(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Default Temps")
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
        #creates an int variable
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
        
        #Back Button
        self.back_button = tk.Button(self, text="Back", command=self.go_back)
        self.back_button.place(x=20, y=20)
        
        ##Text label for Enter Dry Weight
        self.weight_label = tk.Label(self, text="Enter Dry Weight (g)", font=("Arial", 15), bg= "#04043B", fg= "#ff8c00")
        self.weight_label.place(x = 300, y= 200)

        #entry for weight, spinbox allows for there to be an up and down arrow on entry for touchscreen accessability
        self.weight_entry = tk.Spinbox(self, textvariable= self.weight, width=5, from_=0, to=20, font=Font(size=28, weight='bold'))
        self.weight_entry.place(x= 350, y = 240)
        
        
        
    #Function to Navigate to The Brew Profile Window    
    def navigate_to_window(self):
        #Hide The Home Page
        self.withdraw() 
        # Go to The Brew Profile Window
        self.another_window = BrewWindow(self)
    #Sets target temp to 90
    def set_dark_temp(self):
        s.targ_temp = 90
    #sets traget temp to 93
    def set_med_temp(self):
        s.targ_temp = 93
    #sets target temp to 96
    def set_light_temp(self):
        s.targ_temp = 96
    #gets inputed weight and multipys it by 2 to get target weight
    def get_weight_targ_val(self):
        s.targ_weight = self.weight.get() * 2
    #Go back function used for go back button
    def go_back(self):
        #goes back one window, using multiple deiconify's will bring you back a window everytime one is added
        self.master.deiconify()
        #Withdraws current screen
        self.withdraw()
    #gets data and sends to csv
    def get_data(self):
        #create the field names for the csv file, this will make sure there are enough rows to collect all of the data and separate them correctly
        field_names = ['Weight', 'Temp', 'Preinfuse Pressure', 'Preinfuse Time', 'Brew Time', 'Pressure Array', 'Time Array']
        #collects data when brew is started, this is a dictionary
        data = {'Weight': s.targ_weight, 'Temp': s.targ_temp, 'Preinfuse Pressure': s.preinfuse_bar, 'Preinfuse Time': s.preinfuse_time, 'Brew Time': s.brew_time, 'Pressure Array': s.targ_pressure_arr, 'Time Array': s.targ_time_arr}
        #opens the csv file and writes the data dictionary to it
        with open('data1.csv', 'a') as f_object:
            dictwriter_object = DictWriter(f_object, fieldnames=field_names)
            dictwriter_object.writerow(data)
            f_object.close

#Brewing window, this should stay on screen for the entirety of the brew
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
        
        
        # Schedule the go_to_graph function to be called after 5000 milliseconds (5 seconds)
        self.after(5000, self.go_to_graph)
    
    
    def go_to_graph(self): 
        #redirects to the ShowGraph page 
        self.graph_show_page = ShowGraph(self)
        #withdraws current page
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
        # Blooming Allonge Button
        self.button_4 = tk.Button(self, image=self.button_11_image, bg= "#04043B", command= lambda: [self.profile == 'Blooming Allonge', self.go_to_default_temps(), self.set_bloomingallonge_plot()])
        self.button_4.place(x=150, y=250)
        # Allonge Button
        self.button_5 = tk.Button(self, image=self.button_10_image, bg= "#04043B", command= lambda: [self.profile == 'Allonge', self.go_to_default_temps(), self.set_allonge_plot()])
        self.button_5.place(x=420, y=250)
        
        #Purge Button
        self.purge_button = tk.Button(self, image=self.button_9_image, bg= "#04043B")
        self.purge_button.place(x = 280, y = 380)


    # Function to go to Brew Window
    def go_to_default_temps(self):
        # Go to Brew Window
        self.default_temps = DefaultTemps(self)
        # Hide Brew Profile Window
        self.withdraw()
    #sets target values for default 
    def set_default_plot(self):
        #time and pressure array
        s.targ_time_arr, s.targ_pressure_arr = [0,8,13.5,19,24.5,30], [1,1,9,9,9,9]
        #Preinfuse time 
        s.preinfuse_time = 8
        #Preinfuse pressure
        s.preinfuse_bar = 1
        #total brew time, includes preinfuse time
        s.brew_time = 30
    #sets target values for blooming
    def set_blooming_plot(self):
        #time and pressure array
        s.targ_time_arr, s.targ_pressure_arr = [0,8,13.5,19,24.5,35], [3,3,9,9,0,0]
        #preinfuse time
        s.preinfuse_time = 8
        #preinfuse pressure
        s.preinfuse_bar = 3
        #total brew time, includes preinfuse time
        s.brew_time = 35
    #sets target values for blooming allonge
    def set_bloomingallonge_plot(self):
        #time and pressure array
        s.targ_time_arr, s.targ_pressure_arr = [0,10,20,30,40,50], [1,1,2,2,2,1]
        #preinfuse time
        s.preinfuse_time = 10
        #prefinfuse pressure
        s.preinfuse_bar = 1
        #total brew time, includes preinfuse time
        s.brew_time = 50
    #sets target values for allonge 
    def set_allonge_plot(self):
        #time and pressure array
        s.targ_time_arr, s.targ_pressure_arr = [0,8,13.5,19,24.5,30], [1,1,1,1,1,1,1]
        #preinfuse time
        s.preinfuse_time = 8
        #preinfuse pressure
        s.preinfuse_bar = 1
        #total brew time, includes preinfuse time
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
        #creates the canvas and intitializes it with given values
        self.canvas = FigureCanvasTkAgg(m.make_plot(s.brew_time, s.preinfuse_time, s.preinfuse_bar),
                            master = self)  
        print("plot made")
        #draws canvas on window
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
        
        #Dark Roast Button
        self.button_1 = tk.Button(self, image=self.button_1_image, bg= "#04043B", command = lambda: [self.set_dark_temp(), self.go_to_brew_page(), self.get_data()])
        self.button_1.place(x=150, y=380)
        #Medium Roast Button
        self.button_2 = tk.Button(self, image=self.button_3_image, bg= "#04043B", command = lambda: [self.set_med_temp(), self.go_to_brew_page(), self.get_data()])
        self.button_2.place(x=350, y=380)
        #Light Roast Button
        self.button_2 = tk.Button(self, image=self.button_2_image, bg= "#04043B", command = lambda: [self.set_light_temp(), self.go_to_brew_page(), self.get_data()])
        self.button_2.place(x=550, y=380)

        #Back button
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
    #sets target temp to 90
    def set_dark_temp(self):
        s.targ_temp = 90
    #sets target temp to 93
    def set_med_temp(self):
        s.targ_temp = 93
    #sets target temp to 96
    def set_light_temp(self):
        s.targ_temp = 96
    #goes bakc one page
    def go_back(self):
        #clears the point array, makes sure that graph is reset after going back and changing numbers
        m.listLabelPoints.clear()
        #sends plot arrays to backend code to brew
        self.set_plot_arrs()
        #go back one window
        self.master.deiconify()
        #withdraw current window
        self.withdraw()
    #sends data to csv file
    def get_data(self):
        #initializes field names aka row names
        field_names = ['Weight', 'Temp', 'Preinfuse Pressure', 'Preinfuse Time', 'Brew Time', 'Pressure Array', 'Time Array']
        #create dictionary of the data values
        data = {'Weight': s.targ_weight, 'Temp': s.targ_temp, 'Preinfuse Pressure': s.preinfuse_bar, 'Preinfuse Time': s.preinfuse_time, 'Brew Time': s.brew_time, 'Pressure Array': s.targ_pressure_arr, 'Time Array': s.targ_time_arr}
        #open csv file and write to it 
        with open('data1.csv', 'a') as f_object:
            dictwriter_object = DictWriter(f_object, fieldnames=field_names)
            dictwriter_object.writerow(data)
            f_object.close
        #df.to_csv('C:/Users/tmiller4/Desktop/DetroitCremaGUI/DetroitCremaGUI/data/data1.csv')
#screen right before custom graph, has 4 textboxes (please change the name of this class lol)
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
        
        #initialize all of the Int values
        self.preinfuse_time = tk.IntVar()  
        self.preinfuse_bar = tk.IntVar()  
        self.brew_time = tk.IntVar()                                                                                                                                            
        self.weight = tk.IntVar()
        #import logo
        self.home_image = tk.PhotoImage(file=("image_1.png"))
        
        #place logo
        tk.Label(self, image=self.home_image, borderwidth=0,compound="center",highlightthickness = 0, padx=0, pady=30).pack()
        
        #preinfuse time text
        self.preinfuse_label = tk.Label(self, text="Set Preinfuse Time (sec)", font=("Arial", 15), bg= "#04043B", fg= "#ff8c00")
        self.preinfuse_label.place(x= 50, y = 150)
        #preinfuse time entry
        self.preinfuse_entry = tk.Spinbox(self, textvariable = self.preinfuse_time, width=5, from_=0, to=30, font=Font(size=28, weight='bold'))
        self.preinfuse_entry.place(x = 100, y = 190)
        #preinfuse pressure text
        self.preinfuse_bar_label = tk.Label(self, text="Set Preinfuse Pressure (Bar)", font=("Arial", 15), bg= "#04043B", fg= "#ff8c00")
        self.preinfuse_bar_label.place(x = 300, y= 150)
        #preinfuse pressure entry
        self.preinfuse_bar_entry = tk.Spinbox(self, textvariable= self.preinfuse_bar, width=5, from_=0, to=20, font=Font(size=28, weight='bold'))
        self.preinfuse_bar_entry.place(x= 350, y = 190)
        #brew time text
        self.brew_time_label = tk.Label(self, text="Set Total Brew Time (sec)", font=("Arial", 15), bg= "#04043B", fg= "#ff8c00")
        self.brew_time_label.place(x = 50, y= 300)
        #brew time entry
        self.brew_time_entry = tk.Spinbox(self, textvariable= self.brew_time, width=5, from_=0, to=60, font=Font(size=28, weight='bold'))
        self.brew_time_entry.place(x= 100, y = 340)
        #weight text
        self.weight_label = tk.Label(self, text="Enter Dry Weight (g)", font=("Arial", 15), bg= "#04043B", fg= "#ff8c00")
        self.weight_label.place(x = 300, y= 300)
        #weight entry
        self.weight_entry = tk.Spinbox(self, textvariable= self.weight, width=5, from_=0, to=20, font=Font(size=28, weight='bold'))
        self.weight_entry.place(x= 350, y = 340)
        #button to take you to custom graph
        self.cust_button = tk.Button(self, text="Next", command= lambda: [self.get_pre_val(), self.get_weight_targ_val(), self.get_pre_bar(), self.get_brew_time(), self.go_to_cust_page()])
        self.cust_button.place(x = 550, y=425)
        #takes you back one window
        self.back_button = tk.Button(self, text="Back", command=self.go_back)
        self.back_button.place(x=20, y=20)
        
    #goes to custom graph page  
    def go_to_cust_page(self):
        self.cust_page = CustomizeWindow(self)
        self.withdraw()
    #sets preinfuse time to the value in the preinfuse text box on next button click
    def get_pre_val(self):
        s.preinfuse_time = self.preinfuse_time.get()
    #sets weight to the value in the weight text box on the next button click
    def get_weight_targ_val(self):
        s.targ_weight = self.weight.get() * 2
    #sets preinfuse pressure to the value in the preinfuse pressure text box on next button click
    def get_pre_bar(self):
        s.preinfuse_bar = self.preinfuse_bar.get()
    #sets brew time to the value in the brew time text box on the next button click
    def get_brew_time(self):
        s.brew_time = self.brew_time.get()
    #goes back one window
    def go_back(self):
        self.master.deiconify()
        self.withdraw()
#Last window after the brew, in future should show the graph made by mechanical code
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
        
        #returns user to home page
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
