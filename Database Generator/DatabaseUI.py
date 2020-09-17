import tkinter
from tkinter import *
from DatabaseGenerator import export_excel


def export_excel_button() -> None:
    export_excel(int(first_name_txt.get()), int(last_name_txt.get()),
                 int(sin_txt.get()), int(ssn_txt.get()))


main_window = Tk()
main_window.title("Database Generator")

export_btn = Button(main_window, text="Export_to_excel",
                    command = export_excel_button)
export_btn.grid(column=0, row=0, columnspan=2, sticky=NSEW)

number_lbl = Label(main_window, text="# of generations", anchor=W)
number_lbl.grid(column=1, row=1, sticky = NSEW)

first_name_lbl = Label(main_window, text="First Name", anchor=W)
first_name_lbl.grid(column=0, row=2, sticky=NSEW)

first_name_txt = Entry(main_window)
first_name_txt.grid(column=1, row=2, sticky=NSEW)
first_name_txt.insert(0, '0')

last_name_lbl = Label(main_window, text="Last Name", anchor=W)
last_name_lbl.grid(column=0, row=3, sticky=NSEW)

last_name_txt = Entry(main_window)
last_name_txt.grid(column=1, row=3, sticky=NSEW)
last_name_txt.insert(0, '0')

sin_lbl = Label(main_window, text="SIN Number", anchor=W)
sin_lbl.grid(column=0, row=4, sticky=NSEW)

sin_txt = Entry(main_window)
sin_txt.grid(column=1, row=4, sticky=NSEW)
sin_txt.insert(0, '0')

ssn_lbl = Label(main_window, text="SSN Number", anchor=W)
ssn_lbl.grid(column=0, row=5, sticky=NSEW)

ssn_txt = Entry(main_window)
ssn_txt.grid(column=1, row=5, sticky=NSEW)
ssn_txt.insert(0, '0')

snid_lbl = Label(main_window, text="SSN Number", anchor=W)
snid_lbl.grid(column=0, row=6, sticky=NSEW)

snid_txt = Entry(main_window)
snid_txt.grid(column=1, row=6, sticky=NSEW)
snid_txt.insert(0, '0')

main_window.mainloop()
