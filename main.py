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

def clock_in_form():
    class Number_Pad_Button:
        def __init__(self, master, btn_row, btn_column, number):
            self.master = master
            self.btn_row = btn_row
            self.btn_column = btn_column
            self.number = number

            btn_number = tk.Button(
                master=master,
                text=f"{number}",
                command=self.number_pad_controller,
                relief=tk.FLAT,
                font="Roboto 16 bold",
                fg="#ffffff",
                bg="#2E7DDE",
                width=4
            )
            btn_number.grid(
                row=btn_row, 
                column=btn_column,
                padx=5,
                pady=5
            )

        def number_pad_controller(self):
            index = 0
            user_input_list = list(lbl_user_id["text"])

            for char in user_input_list:
                if char == "-":
                    user_input_list[index] = str(self.number)
                    lbl_user_id.configure(text=f"{''.join(user_input_list)}")

                    if index + 2 > len(user_input_list):
                        lbl_user_id.after(500, login_controller)

                    return
                else:
                    index += 1

    def login_controller():
        user_input_list = list(lbl_user_id["text"])
        user_id = user_input_list[0] + user_input_list[3] + user_input_list[6] + user_input_list[9]

        conn = psy.connect(database_credentials)
        cur = conn.cursor()
        
        cur.execute(f"SELECT name FROM guardians WHERE id = {user_id}")
        user_name = cur.fetchone()

        if user_name == None:
            lbl_login_feedback.configure(text=f"ID de Usuario invalido", fg="#881010", font="Roboto\ slab 10 bold",)
            lbl_user_id.config(text="-  -  -  -", fg="#881010")
        else:
            user_first_name = user_name[0].split(' ')[0].title()
            lbl_login_feedback.configure(text=f"Hola {user_first_name}", fg="#16a2ad", font="Roboto\ slab 10 bold",)
            lbl_user_id.config(text="-  -  -  -", fg="#16a2ad")
            
    def live_clock():
        current_time = time.strftime("%I:%M:%S %p")
        lbl_header_time.configure(text=current_time)
        lbl_header_time.after(100, live_clock)
    
    def live_calender():
        current_date = time.strftime("%A %B %d, %Y")
        lbl_header_date.configure(text=current_date)
        lbl_header_date.after(60000, live_calender)

    window = tk.Tk()
    window.configure(background="#DACBB5") #DACBB5 f5f0e8
    window.title("NanaHub | Forma de Entrada")
    # window.geometry("750x500")

    lbl_header = tk.Label(
        master=window,
        text="FORMA DE ENTRADA",
        font="Roboto 18 bold",
        fg="#2E7DDE",
        bg="#DACBB5"
    )
    lbl_header.grid(
        row=0,
        column=0,
        padx=15,
        pady=15,
        sticky="w"
    )

    lbl_header_time = tk.Label(
        master=window,
        font="Roboto\ slab 10",
        fg="#2e7dde",
        bg="white",
        width=10
    )
    lbl_header_time.grid(
        row=0,
        column=1,
        padx=0,
        pady=5,
        sticky="e"
    )

    lbl_header_date = tk.Label(
        master=window,
        font="Roboto\ slab 10 bold",
        fg="#2e7dde",
        bg="white",
        width=20
    )
    lbl_header_date.grid(
        row=0,
        column=2,
        padx=0,
        pady=5,
        sticky="w"
    )

    live_clock()
    live_calender()
    
    frm_login = tk.Frame(
        master=window,
        relief=tk.FLAT,
        borderwidth=1,
        bg="white"
    )
    frm_login.grid(
        row=1,
        column=0,
        columnspan=3,
        pady=10
    )

    lbl_user_id = tk.Label(
        master=frm_login,
        text="-  -  -  -",
        font="Roboto 20",
        bg="white",
        fg="#2E7DDE",  #16a2ad
        width=25
    )
    lbl_user_id.grid(
        row=0,
        column=0,
        columnspan=4,
        pady=15,
        sticky="nesw"
    )

    lbl_login_feedback = tk.Label(
        master=frm_login,
        text="Ingrese su ID de Usuario para comenzar",
        font="Roboto\ slab 10",
        fg="#2e7dde",
        bg="white"
    )
    lbl_login_feedback.grid(
        row=1,
        column=0,
        columnspan=4,
        pady=5,
        sticky="nesw"
    )

    frm_number_pad = tk.Frame(
        master=frm_login,
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
            Number_Pad_Button(frm_number_pad, btn_row, btn_column, button_counter)
            button_counter += 1
        
    Number_Pad_Button(frm_number_pad, 3, 1, 0)

    btn_login = tk.Button(
        master=frm_number_pad,
        text="INGRESAR",
        font="Roboto 16 bold",
        relief=tk.FLAT,
        fg="#ffffff",
        bg="#16a2ad",
        width=15
    )
    btn_login.grid(
        row=4,
        column=0,
        columnspan=4,
        padx=5,
        pady=25
    )

    window.mainloop()

clock_in_form()