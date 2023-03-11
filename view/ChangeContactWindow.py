import tkinter as tk
from view.abstract.modwl_window import ModalWindow
from Types.Contact import Contact
from view import Geometry


class ChangeContactDialog(ModalWindow):
    def __init__(self, parent: tk.BaseWidget, title, contact: Contact):
        self.contact = contact
        super().__init__(parent, title)

    def _compose(self):
        # local methods:
        def set_text(entry: tk.Entry, text):
            entry.delete(0, tk.END)
            entry.insert(0, text)

        def apply_changes_and_close(event=None):
            nonlocal txtbox_name
            nonlocal txtbox_datatime
            nonlocal txtbox_note
            self.contact.name = txtbox_name.get()
            self.contact.datatime = txtbox_datatime.get()
            self.contact.note = txtbox_note.get()
            self._dispose()

        width = 280
        height = 230
        size_window = f'{width}x{height}+{Geometry.get_width(self, width)}+{Geometry.get_height(self, height)}'
        self.geometry(size_window)
        self.resizable(False, False)

        contact = self.contact
        text_header = f'Редактирование заметки ID: {contact.note_id}'

        # labels - left column:

        lbl_header = tk.Label(self, text=text_header, font='Arial 14')
        lbl_header.grid(column=0, columnspan=2, row=0, pady=20)

        lbl_name = tk.Label(self, text='Наименование:')
        lbl_name.grid(column=0, row=1, padx=5, pady=5, sticky='e')

        lbl_datatime = tk.Label(self, text='Дата:')
        lbl_datatime.grid(column=0, row=2, padx=5, pady=5, sticky='e')

        lbl_note = tk.Label(self, text='Заметка:')
        lbl_note.grid(column=0, row=3, padx=5, pady=5, sticky='e')

        # text boxes - right column:

        txtbox_name = tk.Entry(self)
        set_text(txtbox_name, contact.name)
        txtbox_name.grid(column=1, row=1, padx=10, pady=5, sticky='we')

        txtbox_datatime = tk.Entry(self)
        set_text(txtbox_datatime, contact.datatime)
        txtbox_datatime.grid(column=1, row=2, padx=10, pady=5, sticky='we')

        txtbox_note = tk.Entry(self, textvariable=contact.note)
        set_text(txtbox_note, contact.note)
        txtbox_note.grid(column=1, row=3, padx=10, pady=5, sticky='we')

        # OK Cancel:

        btn_ok = tk.Button(self, text='Сохранить',
                           command=apply_changes_and_close)
        btn_ok.grid(column=0, row=4, padx=10, pady=(30, 10), sticky='e')
        self.bind('<Return>', apply_changes_and_close)
        self.bind('<KP_Enter>', apply_changes_and_close)

        btn_cancel = tk.Button(self, text='Отменить',
                               command=self._dispose)
        btn_cancel.grid(column=1, row=4, padx=10, pady=(30, 10), sticky='w')
