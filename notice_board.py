import tkinter as tk
from tkinter import *
from path_relative import *
from tkinter import messagebox
from datetime import datetime

def notice_make():
    notices_file = "notices.txt"

    def add_notice():
        notice = entry.get()
        if notice:
            with open(notices_file, "r+") as file:
                content = file.read()
                file.seek(0, 0)  # Move the file pointer to the beginning
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                file.write(f"{timestamp}: {notice}\n{content}")
            entry.delete(0, tk.END)
            messagebox.showinfo("Notice Added", "Notice has been added")
            display_notices()

    def delete_notice():
        selected_indices = notice_list.curselection()
        if selected_indices:
            selected_notices = [notice_list.get(index) for index in selected_indices]
            with open(notices_file, "r+") as file:
                lines = file.readlines()
                file.seek(0)  # Move the file pointer to the beginning
                for line in lines:
                    if line.strip() not in selected_notices:
                        file.write(line)
                file.truncate()
            messagebox.showinfo("Notice Deleted", "Selected notices have been deleted")
            display_notices()

    def display_notices():
        notice_list.delete(0, tk.END)
        with open(notices_file, "r") as file:
            for line in file:
                notice_list.insert(tk.END, line.strip())

    not_page = tk.Toplevel()
    not_page.title("Manage Notices")
    not_page.geometry('600x600')
    not_page.resizable(False, False)
    image_background = PhotoImage(file=relative_to_assets("notice_make.png"))
    label = tk.Label(not_page, image=image_background)
    label.place(x=0, y=0)
    entry = tk.Entry(not_page,font=("Helvetica", 14), width=40)
    entry.place(x=75, y=200)
    add_image = PhotoImage(file=relative_to_assets("add_button.png"))
    add_button = tk.Button(not_page, image=add_image, command=add_notice, borderwidth=0, 
                           background='lightblue', highlightthickness=0,relief="flat")
    add_button.place(x=200, y=250)
    delete_image = PhotoImage(file=relative_to_assets("delete_button.png"))
    delete_button = tk.Button(not_page,image=delete_image, command=delete_notice, borderwidth=0, 
                              background='lightblue', highlightthickness=0, relief="flat")
    delete_button.place(x=310, y=500)
    refresh_image = PhotoImage(file=relative_to_assets("refresh_button.png"))
    display_button = tk.Button(not_page, image=refresh_image, command=display_notices, borderwidth=0, 
                               background='lightblue', highlightthickness=0, relief="flat")
    display_button.place(x=90, y=500)
    notice_list = tk.Listbox(not_page, width=75, selectmode=tk.MULTIPLE)
    notice_list.place(x=80, y=300)
    display_notices()

    not_page.mainloop()


def notice_view():
    notices_file = "notices.txt"

    def display_notices():
        notice_list.delete(0, tk.END)
        with open(notices_file, "r") as file:
            for line in file:
                notice_list.insert(tk.END, line.strip())

    not_page = tk.Toplevel()
    not_page.title("Notice Board")
    not_page.geometry('600x600')
    not_page.resizable(False, False)
    image_background = PhotoImage(file=relative_to_assets("notice_disp.png"))
    label = tk.Label(not_page, image=image_background)
    label.place(x=0, y=0)
    refresh_image = PhotoImage(file=relative_to_assets("refresh_button.png"))
    display_button = tk.Button(not_page, image=refresh_image, command=display_notices, borderwidth=0, 
                               background='lightblue', highlightthickness=0, relief="flat")
    display_button.place(x=200, y=500)
    notice_list = tk.Listbox(not_page, width=75, selectmode=tk.MULTIPLE)
    notice_list.place(x=80, y=200)
    display_notices()

    not_page.mainloop()


