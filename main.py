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

def clock_in_form():
    window = tk.Tk()
    
    lbl_header = tk.Label(
        master=window,
        text="FORMA DE ENTRADA",
        font=("Arial", 16),
        fg="#1989c0"
    )
    lbl_header.grid(
        row=0,
        column=0,
        padx=5,
        pady=5,
        sticky="w"
    )

    frm_login = tk.Frame(
        master=window,
        bg="#1989c0",
        relief=tk.RIDGE,
        borderwidth=1
    )
    frm_login.grid(
        row=1,
        column=0,
        padx=5,
        pady=5
    )

    lbl_parent_id = tk.Label(
        master=frm_login,
        text="ID Del Padre:",
        font=("Arial", 14),
        bg="#1989c0",
        fg="#ffffff"
    )
    lbl_parent_id.grid(
        row=0,
        column=0,
        padx=5,
        pady=5,
        sticky="w"
    )

    ent_parent_id = tk.Entry(
        master=frm_login,
        font=("Arial", 14)
    )
    ent_parent_id.grid(
        row=0,
        column=1,
        padx=5,
        pady=5,
        sticky="w"
    )

    btn_login = tk.Button(
        master=frm_login,
        text="Ingresar",
        width=15,
        font=("Arial", 12),
        fg="#ffffff",
        bg="#25cd7e"
    )
    btn_login.grid(
        row=1,
        column=0,
        padx=5,
        pady=5,
        sticky="w"
    )

    btn_cancel = tk.Button(
        master=frm_login,
        text="Cancelar",
        width=15,
        font=("Arial", 12),
        fg="#ffffff",
        bg="#B7404B"
    )
    btn_cancel.grid(
        row=1,
        column=1,
        pady=5,
        sticky="w"
    )
        
    window.mainloop()

clock_in_form()