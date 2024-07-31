import tkinter as tk
import csv
from datetime import datetime
from tkinter import messagebox
from path_relative import *
from login import *


# Function to read apartment details from the CSV file
def read_apartment_details(filename):
    apartment_details = {}
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            block = row['Block']
            flat_no = row['FlatNo']
            bhk = int(row['BHK'])
            square_foot = float(row['SquareFoot'])
            customer_name = row['CustomerName']
            username = row['Username']
            password = row['Password']
            phone_number = row['PhoneNumber']
            email_id = row['EmailID']
            status = row['Status']
            
            apartment_details[username] = {
                'block': block,
                'flat_no': flat_no,
                'bhk': bhk,
                'square_foot': square_foot,
                'customer_name': customer_name,
                'password': password,
                'phone_number': phone_number,
                'email_id': email_id,
                'status': status
            }
    return apartment_details


# Function to create the admin main window
def admin_main_window(username,password):
    global admin_main_frame, total_charge_entry

    admin_main_frame = tk.Toplevel()
    admin_main_frame.title("Maintenance Charges")
    admin_main_frame.geometry("500x300")
    admin_main_frame.resizable(False,False)
    admin_main_frame.configure(bg="#507B3B")


    try:
        with open("monthly_charges.csv", "r+") as file:
            reader = csv.reader(file)
            rows = list(reader)
        if not rows:
            writer = csv.writer(file)
            writer.writerows(["Month","Year","Charges"])
        else:
            prev_charge_label = tk.Label(admin_main_frame, text="Previous Month Charges: ",bg="#507B3B")
            prev_charge_label.place(x=100,y=120)
            prev_charge_value = tk.Label(admin_main_frame, text= str(rows[-1][-1]),bg="#507B3B")
            prev_charge_value.place(x=250,y=120)
    except FileNotFoundError:
        pass
    
    # Function to write data to CSV file
    def write_to_csv():
        now = datetime.now()
        month = now.strftime("%B")  # Full month name
        year = now.year
        charges = total_charge_entry.get()
        data = [[month, year, charges]]
        filename = "monthly_charges.csv"

        with open(filename, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(data)
        thanks_label = tk.Label(admin_main_frame,text="Thank You!\nThe charges have been noted.",bg="#507B3B")
        thanks_label.place(x=100,y=200)
        submit_charges_button.config(state="disabled")
        admin_main_frame.after(5000,admin_main_frame.destroy)

    total_charge_label = tk.Label(admin_main_frame, text='Total Monthly Charge:',bg="#507B3B")
    total_charge_label.place(x=100,y=150)
    total_charge_entry = tk.Entry(admin_main_frame,bg="#507B3B")
    total_charge_entry.place(x=250, y=150)

    submit_charges_button = tk.Button(admin_main_frame, text="Submit Charges",bg="#507B3B",command = write_to_csv)
    submit_charges_button.place(x=150, y=200)


# Function to create the resident main window
def resident_main_window(username,password):
    global resident_main_frame,charges_button

    resident_main_frame = tk.Toplevel()
    resident_main_frame.title("Monthly Charges")
    resident_main_frame.geometry("500x300")
    resident_main_frame.resizable(False,False)
    resident_main_frame.configure(bg="#507B3B")

    resident = apartment_details[username]["customer_name"]
    welcome_label = tk.Label(resident_main_frame,text="Welcome Mr./Mrs."+resident,bg="#507B3B")
    welcome_label.place(x=100,y=100)

    # Function to display charges for a specific flat
    def display_flat_charges(flat_areas):
        for flat, area in flat_areas.items():
            if flat == username:
                charge = area[1]
        charge = round(charge,2)
        charge_label = tk.Label(resident_main_frame, text="Your Monthly Charges are: "+str(charge),bg="#507B3B")
        charge_label.place(x=100,y=200)
        resident_main_frame.after(5000,resident_main_frame.destroy)

    def calculate_monthly_charges():
        global flat_areas
        now = datetime.now()
        month = now.strftime("%B")

        try:
            with open("monthly_charges.csv", "r+") as file:
                reader = csv.reader(file)
                rows = list(reader)

            if not rows or rows[-1][0] != month:
                message_label = tk.Label(resident_main_frame, text="Current Month Charges not available yet!\nCome back later.",bg="#507B3B")
                message_label.place(x=100,y=200)
                charges_button.config(state='disabled')

                resident_main_frame.after(5000,resident_main_frame.destroy)
            else:
                flat_areas = {}
            for flat in apartment_details:
                if apartment_details[flat]['status'] == 'Occupied':
                    flat_area = apartment_details[flat]['square_foot']
                    flat_areas[flat] = flat_area
            
            total_charge = int(rows[-1][-1])
            total_area = sum(flat_areas.values())
            
            for flat, area in flat_areas.items():
                if flat == username:
                    charge = (total_charge * area) / total_area
                    flat_areas[flat]=[area,charge]
                    display_flat_charges(flat_areas)


        except FileNotFoundError:
            message_label = tk.Label(resident_main_frame, text="Current Month Charges not available yet!\nCome back later.",bg="#507B3B")
            message_label.place(x=100,y=200)
            charges_button.config(state='disabled')

            resident_main_frame.after(5000,resident_main_frame.destroy)

    charges_button = tk.Button(resident_main_frame, text="View Maintenance Charges",command = calculate_monthly_charges,bg="#507B3B")
    charges_button.place(x=100,y=150)



apartment_details = read_apartment_details('apartmentdetails.csv')