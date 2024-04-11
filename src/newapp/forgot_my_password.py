from tkinter import *
import customtkinter
import tkinter
import pandas as pd

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")
def forgot_my_password():
    app= customtkinter.CTk()
    app.geometry("650x440")
    app.title("Forgot Password")
    df = pd.read_csv("passwords.csv")

    row_count = len(df)

    def change_password():
        username = entry.get()
        password = new_password.get()
        access = 0
        temp = -1
        for i in range(row_count):
            if username == df.loc[i,"username"]:
                access = 1
                temp = i 
        if access == 1:
            l4.configure(text = "")
            l3.configure(text="Success")
            l3.place(x=100 ,y=250 )
            
            df.loc[temp,"password"] = password
            df.to_csv("passwords.csv", index=False)
            
            entry.configure(state = "disabled")
            new_password.configure(state = "disabled")
            button.configure(state = "disabled",fg_color = "grey")
            button_exit.place(x = 50,y= 280)

        else:
            l3.configure(text = "")
            l4.configure(text = "Wrong Username")
            l4.place(x=100 ,y=280 )

    def return_to_login_page():
        app.destroy()


    frame = customtkinter.CTkFrame(app,width=320,height=360,corner_radius=15)
    frame.place(relx =0.5 ,rely=0.5,anchor = tkinter.CENTER)

    l2 = customtkinter.CTkLabel(frame,text="Forgot Password",font=("Century Gothic",25))
    l2.place(x=100 ,y=60 )

    l4 = customtkinter.CTkLabel(frame,text="",font=("Century Gothic",15))
    l3 = customtkinter.CTkLabel(frame,text="",font=("Century Gothic",15))

    entry = customtkinter.CTkEntry(frame,width=220,placeholder_text="Username",state="normal")
    entry.place(x=50,y=130)

    new_password = customtkinter.CTkEntry(frame,width=220,placeholder_text="Set New Password",state = "normal",show="*")
    new_password.place(x=50,y=180)

    button = customtkinter.CTkButton(frame,text="Confirm",hover_color="darkgreen",command = change_password,state="normal")
    button.place(x=90,y=220)

    button_exit = customtkinter.CTkButton(frame,text="Done",hover_color="darkgreen",state="normal",command = return_to_login_page)

    app.mainloop()

#forgot_my_password()