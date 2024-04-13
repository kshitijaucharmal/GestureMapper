#!/usr/bin/env python

from detector import Detector
from newapp.login import login_page_start

import customtkinter
import tkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")


def start_page():
    app = customtkinter.CTk()
    app.geometry("650x440")
    app.title("Start Page")

    def detector():
        # Implement your detector function here
        detector = Detector(train=False)
        detector.main_loop()
        pass

    def go_to_login_page():
        app.destroy()
        login_page_start()

    frame = customtkinter.CTkFrame(app, width=320, height=360, corner_radius=15)
    frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    l2 = customtkinter.CTkLabel(frame, text="Start Page", font=("Century Gothic", 25))
    l2.place(x=100, y=60)

    start_button = customtkinter.CTkButton(
        frame, text="Start", hover_color="darkgreen", command=detector
    )
    start_button.place(x=90, y=130)

    dashboard_button = customtkinter.CTkButton(
        frame, text="Dashboard", hover_color="darkgreen", command=go_to_login_page
    )
    dashboard_button.place(x=90, y=180)

    app.mainloop()


start_page()
