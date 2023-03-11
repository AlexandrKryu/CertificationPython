from Types.Contact import Contact
from view import MainWindow, AddNoteWindow, BasicDialogWindows
from view.ChangeContactWindow import ChangeContactDialog
import Model


def run():
    MainWindow.main_window()


def open_file():
    Model.open_file()


def show_notes(contacts_user=Model.contacts_user):
    MainWindow.main_table.delete(*MainWindow.main_table.get_children())
    for i in contacts_user:
        i = [i.note_id, i.name, i.datatime, i.note]
        MainWindow.main_table.insert('', 'end', values=i)


def save_notes():
    Model.save_notes()


def add_notes(add_entry: list):
    print(add_entry)
    print(add_entry[2].get('1.0', 'end'))
    temp = Contact(Model.next_id(), add_entry[0].get(), add_entry[1],
                   add_entry[2].get('1.0', 'end'))
    Model.contacts_user.append(temp)
    AddNoteWindow.add_window.destroy()
    show_notes()


def _get_selection_as_note() -> Contact:
    table = MainWindow.main_table
    selection_id = table.focus()
    if selection_id is None or selection_id == '':
        return

    selected_item = table.item(selection_id)

    contact_id = str(selected_item['values'][0])
    return Model.get_notes_by_id(contact_id)


def change_note():
    contact = _get_selection_as_note()
    if contact is None:
        BasicDialogWindows.show_warning_dialog('Внимание',
                                               'Пожалуйста предварительно выбирите заметку для изменения! \U0001F62E')
        return

    resul = ChangeContactDialog(
        MainWindow.first_window, 'Редактирование заиетки', contact)

    show_notes()


def delete_note():
    contact = _get_selection_as_note()
    if contact is None:
        BasicDialogWindows.show_warning_dialog('Внимание',
                                               'Пожалуйста предварительно выбирите заметку для удаления! \U0001F62E')
    Model.contacts_user.remove(contact)
    show_notes()


def search_note(search_text):
    temp_list = [i for i in Model.contacts_user if search_text in i.datatime.lower() or search_text in i.datatime]
    show_notes(temp_list)
