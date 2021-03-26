# Author: Nahum Maciel
# Email: nahumamaciel@gmail.com
# Date: 2021-03-21
# File: main.py

""""
|DESCRIPTION|

Execution entry point to NanaHub application. 

|GOAL|

1. Prompt for parent id
2. Prompt for child clock in 
3. Present child clock in details
4. Prompt clock in operation confirmation
"""

import tkinter as tk
import psycopg2 as psy
from datetime import datetime, date
import time
import sys
import os

database_credentials = ""
conn = psy.connect(database_credentials)
cur = conn.cursor()

# class Controller_Login():
#     def __init__(self, user_id):
#         self.user_id = user_id
        
#         cur.execute(f"SELECT name FROM guardians WHERE id = {user_id};")
#         user_name = cur.fetchone()

#         cur.execute(f"SELECT household FROM guardians WHERE id = {user_id};")
#         user_household = cur.fetchone()

#         if user_name == None:
#             lbl_login_feedback.configure(text=f"ID de Usuario invalido", fg="#881010", font="Roboto\ slab 10 bold",)
#             lbl_user_id.config(text="-  -  -  -", fg="#881010")
#         else:
#             user_first_name = user_name[0].split(' ')[0].title()
#             lbl_login_feedback.configure(text=f"Hola {user_first_name}", fg="#16a2ad", font="Roboto\ slab 10 bold",)
#             lbl_user_id.config(text="-  -  -  -", fg="#16a2ad")

class Widget_View_Header():
    def live_clock(self):
        current_time = time.strftime("%I:%M:%S %p")
        self.lbl_header_time.configure(text=current_time)
        self.lbl_header_time.after(100, self.live_clock)
    
    def live_calender(self):
        current_date = time.strftime("%A %B %d, %Y")
        self.lbl_header_date.configure(text=current_date)
        self.lbl_header_date.after(60000, self.live_calender)

    def __init__(self, master, view_title):

        print("Attaching Header Widget")

        self.master = master
        self.view_title = view_title

        self.lbl_header = tk.Label(
            master=self.master,
            text=self.view_title,
            font="Roboto 18 bold",
            fg="#2E7DDE",
            bg="#DACBB5"
        )
        self.lbl_header.grid(
            row=0,
            column=0,
            padx=15,
            pady=15,
            sticky="w"
        )

        self.lbl_header_date = tk.Label(
            master=self.master,
            font="Roboto\ slab 10 bold",
            fg="#2e7dde",
            bg="white",
            width=22
        )
        self.lbl_header_date.grid(
            row=0,
            column=2,
            padx=0,
            pady=5,
            sticky="w",
        )

        self.lbl_header_time = tk.Label(
            master=self.master,
            font="Roboto\ slab 10",
            fg="#2e7dde",
            bg="white",
            width=10
        )
        self.lbl_header_time.grid(
            row=0,
            column=1,
            padx=0,
            pady=5,
            sticky="e"
        )

        self.live_calender()
        self.live_clock()

class Widget_Login_Pad(object):
    class Number_Button(object):
        def update_id_display(self, input):
            self.lbl_id_display = tk.Label(
                master=self.display_master,
                text="-  -  -  -",
                font="Roboto 20",
                bg="white",
                fg="#2E7DDE",  
                width=25
            )
            self.lbl_id_display.grid(
                row=0,
                column=0,
                columnspan=4,
                pady=15,
                sticky="nesw"
        )

        def print_id(self, user_id):
            print(user_id)

        def id_display_controller(self):
            index = 0
            current_input = list(self.lbl_id_display["text"])

            for char in current_input:
                if char == "-":
                    current_input[index] = str(self.btn_value)
                    print(current_input)
                    print(index)

                    if index + 2 > len(current_input):
                        self.lbl_id_display.configure(text=''.join(current_input))
                        self.lbl_id_display.after(500, self.print_id(current_input))
                    else:
                        self.lbl_id_display.configure(text=''.join(current_input))
                        return

                else:
                    index += 1

        def __init__(self, master, btn_value, btn_row, btn_column, display_master):
            self.master = master
            self.btn_value = btn_value
            self.btn_row = btn_row
            self.btn_column = btn_column
            self.display_master = display_master

            self.update_id_display("-  -  -  -")

            btn_number = tk.Button(
                master=self.master,
                text=f"{self.btn_value}",
                command=self.id_display_controller,
                relief=tk.FLAT,
                font="Roboto 16 bold",
                fg="#2E7DDE", #ffffff
                bg="#2E7DDE", #2E7DDE
                width=4
            )
            btn_number.grid(
                row=btn_row, 
                column=btn_column,
                padx=5,
                pady=5
            )

    def __init__(self, master):
        self.master = master

        frm_login_pad = tk.Frame(
            master=self.master,
            relief=tk.FLAT,
            borderwidth=1,
            bg="white"
        )
        frm_login_pad.grid(
            row=1,
            column=0,
            columnspan=3,
            pady=10
        )

        self.lbl_login_feedback = tk.Label(
            master=frm_login_pad,
            text="Ingrese su ID de Usuario para entrar",
            font="Roboto\ slab 10",
            fg="#2e7dde",
            bg="white"
        )
        self.lbl_login_feedback.grid(
            row=1,
            column=0,
            columnspan=4,
            pady=5,
            sticky="nesw"
        )

        frm_number_pad = tk.Frame(
            master=frm_login_pad,
            relief=tk.FLAT,
            bg="white"
        )
        frm_number_pad.grid(
            row=2,
            column=0,
            columnspan=4,
            padx=5,
            pady=5
        )

        button_counter = 1
        for btn_row in range(3):
            for btn_column in range(3):
                self.Number_Button(frm_number_pad, button_counter, btn_row, btn_column, frm_login_pad)
                button_counter += 1
        
        self.Number_Button(frm_number_pad, 0, 3, 1, frm_login_pad)

class View_Clock_In_Form():
    def __init__(self):
        
        print("Making form")

        window = tk.Tk()
        window.configure(background="#DACBB5") #DACBB5 f5f0e8
        window.title("NanaHub | Forma de Entrada")
        # window.geometry("750x500")

        Widget_View_Header(window, "FORMA DE ENTRADA")
        Widget_Login_Pad(window)

        window.mainloop()

View_Clock_In_Form()

























# def clock_in_form():    

#     def wards_select_form(household):
#         cur.execute(f"SELECT name FROM wards WHERE household = {household};")
#         wards = cur.fetchall()

#         print(wards)    
        

#     live_clock()
#     live_calender()

#     window.mainloop()

# clock_in_form()



# btn_login = tk.Button(
#     master=frm_number_pad,
#     text="ENTRAR",
#     font="Roboto 16 bold",
#     relief=tk.FLAT,
#     fg="#ffffff",
#     bg="#16a2ad",
#     width=15,
#     command=wards_select_form(user_household[0])                
# )
# btn_login.grid(
#     row=4,
#     column=0,
#     columnspan=4,
#     padx=5,
#     pady=25
# )