import csv 
import customtkinter
from tkinter import *

'''
def imp():
    names = [
        {'first_name':"Ritesh",'last_name':"Dhake"},
        {'first_name':"Parth",'last_name':"Chandak"},
        {'first_name':"Madhav",'last_name':"Adhav"},
        {'first_name':"Mona",'last_name':"Lisa"}
    ]

    with open('names.csv',mode='w')as csvfile:
        fieldnames = names[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerows(names)

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.minsize(width=307,height=228)
root.title("CSV_ipmort_try")

names = []

def enter_data(names):
    data1=entry.get()
    data2=entry1.get()
    names.append({'first_name':data1,'last_name':data2})
    

def create_csv(names):
    with open('data.csv',mode="a")as csvfile:
        fieldnames = names[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerows(names)

#create_csv(names)

entry = customtkinter.CTkEntry(root,placeholder_text="Enter First name",placeholder_text_color="darkgrey",width=300,border_width=0)
entry.grid(row =0,column =0,columnspan=6,sticky = "nsew")

entry1 = customtkinter.CTkEntry(root,placeholder_text="Enter Last name",placeholder_text_color="darkgrey",width=300,border_width=0)
entry1.grid(row =2,column =0,columnspan=6,sticky = "nsew")

button = customtkinter.CTkButton(root,text = "Submit",command=lambda: enter_data(names),corner_radius=50)
button.grid(row =4,column =3,sticky = "nsew")

button1 = customtkinter.CTkButton(root,text = "Save",command=lambda: create_csv(names),corner_radius=50)
button1.grid(row =6,column =3,sticky = "nsew")

root.mainloop()
'''