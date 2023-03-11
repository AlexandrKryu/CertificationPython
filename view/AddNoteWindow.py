import datetime
import tkinter as tk
from functools import partial

from Types import Contact
import Controller


add_window: tk.Tk
change_window: tk.Tk
add_entry = []
change_entry = []
temp: Contact.Contact
size_window_add = '310x100+650+350'


def open_window_add():
    global add_window
    global add_entry

    resizeble  = True

    add_window = tk.Toplevel()
    add_window.title('Создать заметку')
    add_window.resizable(resizeble, resizeble)
    add_window.wm_attributes('-topmost', 1)
    add_window.columnconfigure(index=0, weight=50)
    add_window.columnconfigure(index=1, weight=250)

    name_lable = tk.Label(add_window, text='Наименование')
    date_label = tk.Label(add_window, text='Дата')
    comment_lable = tk.Label(add_window, text='Заметка')
    name_lable.grid(column=0, row=0, stick='e')
    date_label.grid(column=0, row=1, stick='e')
    comment_lable.grid(column=0, row=2, stick='e')

    name_entry = tk.Entry(add_window, width=30)
    current_datetime = datetime.datetime.now().strftime('%d-%m-%Y %H:%M')  # дата и время
    date_value = tk.Label(add_window, text=current_datetime)
    comment_entry = tk.Text(add_window, width=30, height=10)
    name_entry.grid(column=1, row=0)
    date_value.grid(column=1, row=1)
    comment_entry.grid(column=1, row=2)
    # add_entry = [tk.Entry(add_window, width=30) for _ in range(3)]
    # for i, entry in enumerate(add_entry):
    #     add_entry[i].grid(column=1, row=i)
    add_entry = [name_entry, current_datetime, comment_entry]
    add_button = tk.Button(add_window, text='Создать', command=partial(Controller.add_notes, add_entry))
    add_button.grid(column=1, row=3)

    add_window.mainloop()
