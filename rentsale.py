import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import csv
from path_relative import *
import Rent_sale_view

def button1_click():
    Rent_sale_view.OutsiderView(1)
def button2_click():
    Rent_sale_view.OutsiderView(2)
def button3_click():
    Rent_sale_view.OutsiderView(3)
def button4_click():
    Rent_sale_view.OutsiderView(4)
def button5_click():
    window.destroy()
    from PGP_main import home
    home()

def rentsale():
    global window
    # Create the main window
    window = tk.Tk()
    window.title("Find your apartment")
    # Set the window size
    window.geometry("1500x700")
    window.resizable(False, False)

    # Open and resize the image
    image = Image.open(relative_to_assets("pvgreen.jpg"))
    resized_image = image.resize((1500, 700)) 

    # Convert the resized image to Tkinter PhotoImage format
    background_image = ImageTk.PhotoImage(resized_image)

    # Create a Label widget for the background image
    background_label = tk.Label(window, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    background_label.image = background_image

    content_label = tk.Label(window, text="Welcome to provident Green Park", font=("Arial", 16), fg="black",width=40,height=2)
    content_label.place(x=550,y=10)

    # Define the style for the buttons
    button_style = {
        "background": "white",
        "foreground": "green",
        "font": ("Arial", 12),
        "relief": tk.SOLID,
        "width":40,
        "height":2
    }

    button1 = tk.Button(window, text="View flats for rent in 1 BHK", command= button1_click, **button_style)
    button1.place(x=600,y=100)

    button2 = tk.Button(window, text="View flats for rent in 2 BHK", command=button2_click, **button_style)
    button2.place(x=600,y=200)

    button3= tk.Button(window, text="View flats for rent in 3 BHK", command=button3_click, **button_style)
    button3.place(x=600,y=300)

    button4= tk.Button(window, text="View flats for sale", command=button4_click, **button_style)
    button4.place(x=600,y=400)

    back_button= tk.Button(window, text="HOME", command=button5_click, **button_style)
    back_button.place(x=600,y=600)
    
    window.mainloop()