from tkinter import *
import tkinter
import customtkinter
import pandas as pd
from newapp.shortcuts import run_shortcut, get_word, remove_symbol, bad_chars

customtkinter.set_default_color_theme("green")
customtkinter.set_appearance_mode("dark")

global my_x, my_x2, my_y3
my_x = -600
my_x2 = 1000
my_y3 = 750


def main_app():
    app = customtkinter.CTk()
    app.geometry("1280x720")
    app.title("GMU")
    app.resizable(False, False)

    root = customtkinter.CTkFrame(app, width=700, height=700, corner_radius=30)
    # root.place(rely = 0.5,anchor= tkinter.W)

    root_op = customtkinter.CTkFrame(app, width=550, height=700, corner_radius=30)
    # root_op.place(relx = 1,rely = 0.5,anchor= tkinter.E)

    # creating button
    button_1 = customtkinter.CTkButton(
        root,
        text="1",
        command=lambda: button_click(1, button_1),
        width=150,
        height=150,
        hover_color="darkgreen",
        corner_radius=45,
        font=("Helvetica", 20),
        hover=True,
    )
    button_2 = customtkinter.CTkButton(
        root,
        text="2",
        command=lambda: button_click(2, button_2),
        width=150,
        height=150,
        hover_color="darkgreen",
        corner_radius=45,
        font=("Helvetica", 20),
        hover=True,
    )
    button_3 = customtkinter.CTkButton(
        root,
        text="3",
        command=lambda: button_click(3, button_3),
        width=150,
        height=150,
        hover_color="darkgreen",
        corner_radius=45,
        font=("Helvetica", 20),
        hover=True,
    )
    button_4 = customtkinter.CTkButton(
        root,
        text="4",
        command=lambda: button_click(4, button_4),
        width=150,
        height=150,
        hover_color="darkgreen",
        corner_radius=45,
        font=("Helvetica", 20),
        hover=True,
    )
    button_5 = customtkinter.CTkButton(
        root,
        text="5",
        command=lambda: button_click(5, button_5),
        width=150,
        height=150,
        hover_color="darkgreen",
        corner_radius=45,
        font=("Helvetica", 20),
        hover=True,
    )
    button_6 = customtkinter.CTkButton(
        root,
        text="6",
        command=lambda: button_click(6, button_6),
        width=150,
        height=150,
        hover_color="darkgreen",
        corner_radius=45,
        font=("Helvetica", 20),
        hover=True,
    )
    button_7 = customtkinter.CTkButton(
        root,
        text="7",
        command=lambda: button_click(7, button_7),
        width=150,
        height=150,
        hover_color="darkgreen",
        corner_radius=45,
        font=("Helvetica", 20),
        hover=True,
    )
    button_8 = customtkinter.CTkButton(
        root,
        text="8",
        command=lambda: button_click(8, button_8),
        width=150,
        height=150,
        hover_color="darkgreen",
        corner_radius=45,
        font=("Helvetica", 20),
        hover=True,
    )
    button_9 = customtkinter.CTkButton(
        root,
        text="9",
        command=lambda: button_click(9, button_9),
        width=150,
        height=150,
        hover_color="darkgreen",
        corner_radius=45,
        font=("Helvetica", 20),
        hover=True,
    )

    action_frame = customtkinter.CTkFrame(
        root_op, width=350, height=420, corner_radius=30
    )

    # Displaying buttons
    button_1.place(x=50, y=80)
    button_2.place(x=250, y=80)
    button_3.place(x=450, y=80)
    button_4.place(x=50, y=280)
    button_5.place(x=250, y=280)
    button_6.place(x=450, y=280)
    button_7.place(x=50, y=480)
    button_8.place(x=250, y=480)
    button_9.place(x=450, y=480)

    label = customtkinter.CTkLabel(
        root_op, text="Choose Gesture ", font=("Helvetica", 30)
    )
    label.place(relx=0.5, rely=0.15, anchor=tkinter.N)

    # showing option menu
    def show_option_menu(number):
        if number == 1:
            label.configure(text="Gesture: Peace")
        elif number == 2:
            label.configure(text="Gesture: Thumbs Up Left")
        elif number == 3:
            label.configure(text="Gesture: Thumbs Up Right")
        elif number == 4:
            label.configure(text="Gesture: Plam Left")
        elif number == 5:
            label.configure(text="Gesture: Plam Right")
        elif number == 6:
            label.configure(text="Gesture: Thumbs Down Left")
        elif number == 7:
            label.configure(text="Gesture: Thumbs Down Right")
        elif number == 8:
            label.configure(text="Gesture: Fist Left")
        elif number == 9:
            label.configure(text="Gesture: Fist Right")

    def frame_right_up():
        global my_y3
        my_y3 -= 6
        if my_y3 >= 200:
            action_frame.place(x=100, y=my_y3)
            app.after(6, frame_right_up)

    def button_click(number, button):
        show_option_menu(number)
        show_action_frame_load_action(number)
        frame_right_up()

    # Actionframe
    def show_action_frame_load_action(number):

        df = pd.read_csv("data.csv")
        # action_frame.place(relx = 0.5 ,rely = 0.6 , anchor = tkinter.CENTER)

        label = customtkinter.CTkLabel(
            action_frame, text="Action: ", font=("Helvetica", 30)
        )
        label.place(relx=0.25, rely=0.15, anchor=tkinter.N)

        label1 = customtkinter.CTkLabel(
            action_frame, text="Path: ", font=("Helvetica", 30)
        )
        label1.place(relx=0.25, rely=0.29, anchor=tkinter.N)

        entry = customtkinter.CTkEntry(
            action_frame, width=135, height=28, bg_color="transparent", state="disabled"
        )
        entry.place(relx=0.45, rely=0.15)

        entry_p = customtkinter.CTkEntry(
            action_frame, width=135, height=28, bg_color="transparent", state="disabled"
        )
        entry_p.place(relx=0.45, rely=0.295)

        # label2 = customtkinter.CTkLabel(action_frame ,text="Gesture: ",font=("Helvetica",30))
        # label2.place(relx = 0.25 ,rely = 0.45, anchor = tkinter.N)

        # option = customtkinter.CTkOptionMenu(action_frame,width=135,height = 28,values=["Peace","Thumbsup_Right","Thumbsup_Left","Plam_Right","Plam_Left","Thumbdown_Right","Thumbsdown_Left","Fist_left","Fist_Right"],fg_color="grey")
        # option.place(relx = 0.45,rely = 0.455)

        button_demo = customtkinter.CTkButton(
            action_frame, text="DEMO RUN", command=lambda: demo_run(number)
        )

        def choose_action(number):
            button_choose_action = customtkinter.CTkButton(
                root_op,
                text="Load Action",
                command=lambda: action_selected(1, number),
                width=50,
            )
            button_choose_action.place(relx=0.35, rely=0.23)

            button_choose_path = customtkinter.CTkButton(
                root_op,
                text="Load Path",
                command=lambda: action_selected(2, number),
                width=50,
            )
            button_choose_path.place(relx=0.51, rely=0.23)

        def action_selected(value, number):
            # df = pd.read_csv("data.csv")
            button_demo.place(relx=0.3, rely=0.55)
            if value == 1:
                temp = df.loc[number - 1, "action"]
                entry.configure(state="normal")
                button_act = customtkinter.CTkButton(
                    action_frame,
                    text="Save Action " + str(number),
                    command=lambda: enter_data(number),
                    font=("Helvetica", 18),
                )
                button_act.place(relx=0.3, rely=0.45)
                entry_p.delete(0, END)
                entry.delete(0, END)
                entry.insert(0, temp)
                entry_p.configure(state="disabled")
                # opt = df.loc[number-1,"gesture"]
                # option.set(opt)

                def enter_data(number):
                    data1 = entry.get()
                    data2 = ""
                    # names[number-1].update({'action':data1,'path':data2,'gesture':number})
                    df.loc[number - 1, "action"] = data1
                    df.loc[number - 1, "path"] = data2
                    # df.loc[number-1,"gesture"] = option.get()
                    df.to_csv("data.csv", index=False)

            elif value == 2:
                temp = df.loc[number - 1, "path"]
                entry_p.configure(state="normal")
                button_act = customtkinter.CTkButton(
                    action_frame,
                    text="Save Path " + str(number),
                    command=lambda: enter_data(number),
                    font=("Helvetica", 18),
                )
                button_act.place(relx=0.3, rely=0.45)
                entry_p.delete(0, END)
                entry.delete(0, END)
                entry_p.insert(0, temp)
                entry.configure(state="disabled")
                # opt = df.loc[number-1,"gesture"]
                # option.set(opt)

                def enter_data(number):
                    data1 = ""
                    data2 = entry_p.get()
                    # names[number-1].update({'action':data1,'path':data2,'gesture':number})
                    df.loc[number - 1, "action"] = data1
                    df.loc[number - 1, "path"] = data2
                    # df.loc[number-1,"gesture"] = option.get()
                    df.to_csv("data.csv", index=False)

        choose_action(number)

        def demo_run(number):
            s = df.loc[number - 1, "action"]
            new = remove_symbol(s, bad_chars)
            new_s = get_word(new)
            if len(new_s) == 2:
                run_shortcut(new_s[0], new_s[1], "")
            elif len(new_s) == 3:
                run_shortcut(new_s[0], new_s[1], new_s[2])

    def mode_change():
        value = button_mode_change.cget("text")
        global my_x, my_x2
        my_x = -600
        my_x2 = 1000
        left_in()
        right_in()
        if value == "Light":
            customtkinter.set_appearance_mode("dark")
            button_mode_change.configure(
                text="Dark", fg_color="grey", hover_color="darkgrey"
            )
        elif value == "Dark":
            customtkinter.set_appearance_mode("light")
            button_mode_change.configure(
                text="Light", fg_color="grey", hover_color="darkgrey"
            )

    button_mode_change = customtkinter.CTkSwitch(
        root_op, text="Dark", fg_color="grey", command=mode_change
    )
    button_mode_change.place(x=400, y=40)

    def logout():
        app.destroy()

    button_logout = customtkinter.CTkButton(
        root_op,
        text="Logout",
        width=50,
        fg_color="grey",
        hover_color="red",
        command=logout,
    )
    button_logout.place(relx=0.1, rely=0.05)

    def left_in():
        global my_x
        my_x += 8
        if my_x <= 10:
            root.place(x=my_x, y=6)
            app.after(8, left_in)

    def right_in():
        global my_x2
        my_x2 -= 6
        if my_x2 >= 715:
            root_op.place(x=my_x2, y=6)
            app.after(10, right_in)

    left_in()
    right_in()
    app.mainloop()


# main_app()
