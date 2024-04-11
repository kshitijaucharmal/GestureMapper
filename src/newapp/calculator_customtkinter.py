from tkinter import *
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.minsize(width=307,height=228)
root.title("Simple Calculator_CustomTkinter")
#root.geometry('200X350')


entry = customtkinter.CTkEntry(root,placeholder_text="Enter a number",placeholder_text_color="darkgrey",width=300,fg_color="transparent",border_width=0)
entry.grid(row =0,column =0,columnspan=5,sticky = "nsew")


#buttondef
def button_click(number):
    current = entry.get()
    entry.delete(0,END)
    entry.insert(0,str(current)+str(number))

def button_additon():
    first_number = entry.get()
    global f_num
    global math
    math = "add"
    f_num = int(first_number)
    entry.delete(0,END)
    
def button_subtraction():
    first_number = entry.get()
    global f_num
    global math
    math = "sub"
    f_num = int(first_number)
    entry.delete(0,END)

def button_multiplication():
    first_number = entry.get()
    global f_num
    global math
    math = "mul"
    f_num = int(first_number)
    entry.delete(0,END)

def button_division():
    first_number = entry.get()
    global f_num
    global math
    math = "div"
    f_num = int(first_number)
    entry.delete(0,END)

def button_isequal():
    second_number = entry.get()
    entry.delete(0,END)

    if math == "add":
        entry.insert(0,f_num+int(second_number))
    if math == "sub":
        entry.insert(0,f_num-int(second_number))
    if math == "mul":
        entry.insert(0,f_num*int(second_number))
    if math == "div":
        entry.insert(0,f_num/int(second_number))         

def button_clear():
    entry.delete(0,END)

#creating button 
button_1 = customtkinter.CTkButton(root,text = "1",command=lambda:button_click(1),width=75,height=50,hover_color="darkgrey",corner_radius=100,fg_color="grey",font=("Helvetica",16))
button_2 = customtkinter.CTkButton(root,text = "2",command=lambda:button_click(2),width=75,height=50,hover_color="darkgrey",corner_radius=100,fg_color="grey",font=("Helvetica",16))
button_3 = customtkinter.CTkButton(root,text = "3",command=lambda:button_click(3),width=75,height=50,hover_color="darkgrey",corner_radius=100,fg_color="grey",font=("Helvetica",16))
button_4 = customtkinter.CTkButton(root,text = "4",command=lambda:button_click(4),width=75,height=50,hover_color="darkgrey",corner_radius=100,fg_color="grey",font=("Helvetica",16))
button_5 = customtkinter.CTkButton(root,text = "5",command=lambda:button_click(5),width=75,height=50,hover_color="darkgrey",corner_radius=100,fg_color="grey",font=("Helvetica",16))
button_6 = customtkinter.CTkButton(root,text = "6",command=lambda:button_click(6),width=75,height=50,hover_color="darkgrey",corner_radius=100,fg_color="grey",font=("Helvetica",16))
button_7 = customtkinter.CTkButton(root,text = "7",command=lambda:button_click(7),width=75,height=50,hover_color="darkgrey",corner_radius=100,fg_color="grey",font=("Helvetica",16))
button_8 = customtkinter.CTkButton(root,text = "8",command=lambda:button_click(8),width=75,height=50,hover_color="darkgrey",corner_radius=100,fg_color="grey",font=("Helvetica",16))
button_9 = customtkinter.CTkButton(root,text = "9",command=lambda:button_click(9),width=75,height=50,hover_color="darkgrey",corner_radius=100,fg_color="grey",font=("Helvetica",16))
button_0 = customtkinter.CTkButton(root,text = "0",command=lambda:button_click(0),width=75,height=50,hover_color="darkgrey",corner_radius=100,fg_color="grey",font=("Helvetica",16))
button_add = customtkinter.CTkButton(root,text = "+",command=button_additon,width=75,height=50,hover_color="darkorange",corner_radius=100,fg_color="orange",font=("Helvetica",16))
button_sub = customtkinter.CTkButton(root,text = "-",command=button_subtraction,width=75,height=50,hover_color="darkorange",corner_radius=100,fg_color="orange",font=("Helvetica",16))
button_mul = customtkinter.CTkButton(root,text = "*",command=button_multiplication,width=75,height=50,hover_color="darkorange",corner_radius=100,fg_color="orange",font=("Helvetica",16))
button_div = customtkinter.CTkButton(root,text = "/",command=button_division,width=75,height=50,hover_color="darkorange",corner_radius=100,fg_color="orange",font=("Helvetica",16))
button_clr = customtkinter.CTkButton(root,text = "clear",command=button_clear,width=75,height=50,hover_color="darkorange",corner_radius=100,fg_color="orange",font=("Helvetica",16))
button_equal = customtkinter.CTkButton(root,text = "=",command=button_isequal,width=75,height=50,hover_color="darkorange",corner_radius=100,fg_color="orange",font=("Helvetica",16))



#display button
button_0.grid(row=4,column=0,sticky = "nsew")
button_1.grid(row=3,column=0,sticky = "nsew")
button_2.grid(row=3,column=1,sticky = "nsew")
button_3.grid(row=3,column=2,sticky = "nsew")
button_4.grid(row=2,column=0,sticky = "nsew")
button_5.grid(row=2,column=1,sticky = "nsew")
button_6.grid(row=2,column=2,sticky = "nsew")
button_7.grid(row=1,column=0,sticky = "nsew")
button_8.grid(row=1,column=1,sticky = "nsew")
button_9.grid(row=1,column=2,sticky = "nsew")
button_add.grid(row=1,column=3,sticky = "nsew")
button_sub.grid(row=2,column=3,sticky = "nsew")
button_mul.grid(row=3,column=3,sticky = "nsew")
button_div.grid(row=4,column=3,sticky = "nsew")
button_equal.grid(row=4,column=2,sticky = "nsew")
button_clr.grid(row=4,column=1,sticky = "nsew")

Grid.rowconfigure(root,0,weight = 1)
Grid.rowconfigure(root,1,weight = 1)
Grid.rowconfigure(root,2,weight = 1)
Grid.rowconfigure(root,3,weight = 1)
Grid.rowconfigure(root,4,weight = 1)

Grid.columnconfigure(root,0,weight = 1)
Grid.columnconfigure(root,1,weight = 1)
Grid.columnconfigure(root,2,weight = 1)
Grid.columnconfigure(root,3,weight = 1)


root.mainloop()