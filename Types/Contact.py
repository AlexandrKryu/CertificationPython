class Contact:
    note_id: str
    name: str
    datatime: str
    note: str

    def __init__(self, note_id: str, name: str, datatime: str, note: str):
        self.note_id = note_id
        self.name = name
        self.datatime = datatime
        self.note = note

    def items(self):
        return (self.note_id, self.name, self.datatime, self.note)

    def show(self):
        print(f'{self.note_id} {self.name} {self.datatime} {self.note}')

    def __str__(self):
        comment_safe = self.note.replace('\n', '\\n')
        return ';'.join(map(str, (self.note_id, self.name, self.datatime, comment_safe)))

    def __copy__(self):
        return Contact(self.note_id, self.name, self.datatime, self.note)
