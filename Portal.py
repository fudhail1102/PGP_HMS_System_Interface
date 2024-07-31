from complaint import priority_queue_node ,linked_priority_queue
import tkinter as tk
from tkinter import messagebox
import csv
from path_relative import *

try:  
    with open('complaint_record.txt','r') as f:
        complaints=f.readlines()
    complaint_queue=linked_priority_queue()
    if len(complaints)>0:
        for i in complaints:
            item=i[:-3].split('   ')
            pr=i[-2].encode('unicode_escape').decode('utf-8')
            complaint_queue.queue(item,int(pr[0]))
except:
    complaint_queue=linked_priority_queue()

def checkinput(main,issue,description):
    if len(str(issue))==0:               
        tk.messagebox.showwarning("Invalid input", "Issue field can't be empty. Please try again.")
        main.mainloop()
    elif len(str(description))==0:
        tk.messagebox.showwarning("Invalid input", "Please describe your issue")
        main.mainloop()

def queue(username,main,issue, description):
    checkinput(main, issue, description)
    global complaint_record
    if issue and description:
        if issue in ('Water','Electricity','Parking','Labour'):
            priority=3
        elif issue in ('Parcel','Neighbours','Amenity','App'):
            priority=2
        else:
            priority=1
        f=open('complaint_record.txt','w+')
        rows=[]
        fields=[]
        with open('apartmentdetails.csv', 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            fields = next(csvreader)
            for row in csvreader:
                rows.append(row)
        res=''
        a=username
        for x in rows:
            if a in x:
                info=[x[0],x[1],x[4],x[7],x[8]]
        data_list=[i for i in info]
        data_list.extend([issue,description])
        complaint_queue.queue(data_list,priority)
        temp=complaint_queue._front
        while temp:
            x=''
            for i in range(len(temp._item)):
                x+=str(temp._item[i])+'   '
            x+=str(temp._priority)
            f.write(x)
            f.write('\n')
            temp=temp._next
        f.close()
        tk.messagebox.showinfo("Process completed","Complaint added successfully")
        main.destroy()

def complaint_window_tenant(username,password):
    main=tk.Tk()
    complaint=tk.StringVar(main)
    issue=tk.StringVar(main)
    main.geometry("600x400")
    main.title("Complaint board")
    L1 = tk.Label(main, text="Please choose the type of complaint :", font=('calibre',10, 'bold'))
    L1.grid(row = 0, column = 0, pady = 2)
    R1 = tk.Radiobutton(main, text="Water-related", variable=complaint, value="Water",font=('calibre',10, 'normal'))  
    R2 = tk.Radiobutton(main, text="Electricity-related", variable=complaint, value='Electricity',font=('calibre',10, 'normal'))
    R3 = tk.Radiobutton(main, text="Parcel-related", variable=complaint, value='Parcel',font=('calibre',10, 'normal'))
    R4 = tk.Radiobutton(main, text="Neighbours", variable=complaint, value="Neighbours",font=('calibre',10, 'normal'))  
    R5 = tk.Radiobutton(main, text="Parking-related", variable=complaint, value='Parking',font=('calibre',10, 'normal'))
    R6 = tk.Radiobutton(main, text="Improper Labour work", variable=complaint, value='Labour',font=('calibre',10, 'normal'))
    R7 = tk.Radiobutton(main, text="App-related", variable=complaint, value='App',font=('calibre',10, 'normal'))
    R8 = tk.Radiobutton(main, text="Amenity-related", variable=complaint, value="Amenity",font=('calibre',10, 'normal'))
    R9 = tk.Radiobutton(main, text="Other", variable=complaint, value='Other',font=('calibre',10, 'normal'))
    R1.grid(row = 1, column = 0, sticky = 'W', padx = 2, pady = 2)
    R2.grid(row = 1, column = 1, sticky = 'W', padx = 2, pady = 2)
    R3.grid(row = 1, column = 2, sticky = 'W', padx = 2, pady = 2)
    R4.grid(row = 2, column = 0, sticky = 'W', padx = 2, pady = 2)
    R5.grid(row = 2, column = 1, sticky = 'W', padx = 2, pady = 2)
    R6.grid(row = 2, column = 2, sticky = 'W', padx = 2, pady = 2)
    R7.grid(row = 3, column = 0, sticky = 'W', padx = 2, pady = 2)
    R8.grid(row = 3, column = 1, sticky = 'W', padx = 2, pady = 2)
    R9.grid(row = 3, column = 2, sticky = 'W', padx = 2, pady = 2)
    L2 = tk.Label(main, text="Please describe your issue :",font=('calibre',10, 'bold')).grid(row = 4, column=0, sticky='W', pady=2)
    info_entry= tk.Entry(main, font=('calibre',8, 'normal'), textvariable=issue).place(x=10, y=150, width=500, height=100)
    B1=tk.Button(main, text="Submit", bd= 5, command = lambda:(queue(username,main,complaint.get(),issue.get()))).place(x=250, y=275)
    B2=tk.Button(main, text='Go Back', bd=5, command=main.destroy).place(x=250, y=350)
    main.mainloop()
    
def complaint_window_admin():

    def delete():
        selected_indices = complaint_list.curselection()
        if selected_indices:
            selected_notices = [complaint_list.get(index) for index in selected_indices]
            with open('complaint_record.txt', "r+") as file:
                lines = file.readlines()
                file.seek(0)  # Move the file pointer to the beginning
                for line in lines:
                    if line not in selected_notices:
                        file.write(line)
                file.truncate()
            messagebox.showinfo("Complaint Deleted", "Selected complaints have been deleted")
            display()
    
    def display():
        complaint_list.delete(0, tk.END)
        with open('complaint_record.txt', "r") as file:
            for line in file:
                complaint_list.insert(tk.END, line)
    
    main=tk.Toplevel()
    main.geometry("1200x600")
    main.title("Complaint board")
    main.resizable(False, False)
    image_background = tk.PhotoImage(file=relative_to_assets("complaints_manage.png"))
    label = tk.Label(main, image=image_background)
    label.place(x=0, y=0)
    delete_image = tk.PhotoImage(file=relative_to_assets("delete_button.png"))
    delete_button = tk.Button(main,image=delete_image, command=delete, borderwidth=0, 
                              background='lightblue', highlightthickness=0, relief="flat")
    delete_button.place(x=750, y=500)
    refresh_image = tk.PhotoImage(file=relative_to_assets("refresh_button.png"))
    display_button = tk.Button(main, image=refresh_image, command=display, borderwidth=0, 
                               background='lightblue', highlightthickness=0, relief="flat")
    display_button.place(x=200, y=500)
    complaint_label=tk.Label(main, text='Block\tFlat no\tTenant\tPh no.\tEmail\tIssue type\tDescription\tPriority no         ',font=('calibre',10))
    complaint_label.place(x=250,y=280)
    complaint_list = tk.Listbox(main, width=100, selectmode=tk.MULTIPLE)
    complaint_list.place(x=250, y=300)
    display()
    main.mainloop()

##complaint_window_admin()
##complaint_window_tenant('A1101','aB3dG7fI9')

