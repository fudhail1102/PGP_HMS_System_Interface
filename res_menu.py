import tkinter as tk
from tkinter import *
from path_relative import *
from notice_board import notice_view
from maintenance_module import *
from login import *
from HashTableConstruction import HashTable
from Portal import *
import PGP_main

def home_page():
    res_page.destroy()
    PGP_main.home()


def residentpage(username,password):
    global res_page
    def notice():
        notice_view()
    
    def maintenance():
        resident_main_window(username,password)

    def complaint():
        complaint_window_tenant(username,password)

    res_page = tk.Tk()
    res_page.geometry("1200x613")
    res_page.title('Resident Menu')
    res_page.resizable(False,False)
    image_background = PhotoImage(file=relative_to_assets("resident_page.png"))
    label = tk.Label(res_page, image=image_background)
    label.place(x=0, y=0)

    button_notice_img = PhotoImage(file=relative_to_assets("res_notice.png"))
    button_notice = Button(res_page, image=button_notice_img, borderwidth=0,  command=notice, highlightthickness=0, relief="flat")
    button_notice.place(x=78.0, y=227.0, width=250, height=75)

    button_complaint_img = PhotoImage(file=relative_to_assets("res_complaint.png"))
    button_complaint= Button(res_page, image=button_complaint_img, command = complaint, borderwidth=0, highlightthickness=0, relief="flat")
    button_complaint.place(x=78.0, y=332.0, width=250, height=75)

    button_maint_img = PhotoImage(file=relative_to_assets("res_maintenance.png"))
    button_maint = Button(res_page, image=button_maint_img, borderwidth=0, command = maintenance, highlightthickness=0, relief="flat")
    button_maint.place(x=78.0, y=437.0, width=250, height=75)

    button_home_img = PhotoImage(file=relative_to_assets("logout_button.png"))
    button_home = Button(res_page, image=button_home_img, borderwidth=0, highlightthickness=0, 
                            command=home_page, relief="flat")
    button_home.place(x=900, y=10)

    House=HashTable[(username,password)]
    x = 600
    y = 150
    for key, value in House.get_all_details().items():
        label = tk.Label(res_page,foreground="#507B3B", text=f"{key}: {value}", font=("Ariel", 20), width=25, height=1,anchor="w")
        label.place(x=x, y=y)
        y+= 50

    res_page.mainloop()
