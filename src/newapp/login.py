from tkinter import *
import customtkinter
import tkinter
import pandas as pd

# from PIL import Image, ImageTk
from newapp.main import main_app
from newapp.forgot_my_password import forgot_my_password

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")


def login_page_start():
    app = customtkinter.CTk()
    app.geometry("650x440")
    app.title("Login Page")

    df = pd.read_csv("passwords.csv")

    # l1 =customtkinter.CTkImage(dark_image=Image.open("/Users/riteshdhake/Coding /Tkinter/IMG_0183.PNG"))
    """
    def new_open():
        app.destroy()
        w = customtkinter.CTk()
        w.geometry("1280x720")
        w.title("GMU")
        l1 = customtkinter.CTkLabel(w,text="Welcome",font=("Century Gothic",20))
        l1.place(x=60,y=0)
        w.mainloop()
    """

    def button_submit():
        new_label = customtkinter.CTkLabel(frame, text="", text_color="red")
        user = entry.get()
        passwrd = password.get()
        check(user, passwrd, new_label)

    def check(user, passwrd, new_label):
        accs = 0
        row_count = len(df)
        for i in range(3):
            usr = df.loc[i, "username"]
            pwd = df.loc[i, "password"]
            if user == usr and passwrd == pwd:
                accs = 1
                break
            else:
                accs = -1
        if accs == 1:
            password.delete(0, END)
            entry.delete(0, END)
            app.destroy()
            main_app()
        elif accs == -1:
            new_label.configure(text="Enter valid username and password")
            password.delete(0, END)
            entry.delete(0, END)
            new_label.place(x=90, y=300)
            button_forgot_password.place(x=90, y=270)

    def forgot_password():
        app.destroy()
        forgot_my_password()

    frame = customtkinter.CTkFrame(app, width=320, height=360, corner_radius=15)
    frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    l2 = customtkinter.CTkLabel(frame, text="Login In", font=("Century Gothic", 25))
    l2.place(x=125, y=60)

    entry = customtkinter.CTkEntry(frame, width=220, placeholder_text="Username")
    entry.place(x=50, y=130)

    password = customtkinter.CTkEntry(
        frame, width=220, placeholder_text="Password", show="*"
    )
    password.place(x=50, y=180)

    button = customtkinter.CTkButton(
        frame, text="Login", hover_color="darkgreen", command=button_submit
    )
    button.place(x=90, y=220)

    button_forgot_password = customtkinter.CTkButton(
        frame,
        text="Forgot Password",
        text_color="green",
        command=forgot_password,
        fg_color="transparent",
        hover=False,
    )

    app.mainloop()


# login_page_start()
