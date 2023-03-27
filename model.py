import datetime
import controller
import json


class Notebook:
    note_book = []
    path = 'note_book.json'

    def open(self):
        with open(self.path, encoding='UTF-8') as data:
            file = json.load(data)  # в file записывается список словарей
        for note in file:
            self.note_book.append(note)

    def save(self):
        nb_str = []
        for note in self.note_book:
            nb_str.append(note)
        with open(self.path, 'w', encoding='UTF-8') as data:
            json.dump(nb_str, data, ensure_ascii=False, indent=2)

    def get_id(self, length_notebook: int):
        if length_notebook == 0:
            new_id = 1
        else:
            new_id = self.note_book[len(self.note_book) - 1]['id'] + 1
            i = len(self.note_book) - 1
            if self.note_book[i]['id'] == new_id:
                while True:
                    new_id += 1
        return new_id

    def new(self, new_note: dict):
        self.note_book.append(new_note)

    def delete(self, index_note_for_delete: int):
        if index_note_for_delete in range(len(self.note_book)):
            for serial_number in range(len(self.note_book)):
                if serial_number == index_note_for_delete:
                    del self.note_book[serial_number]
        else:
            return False

    def search(self, find: str):
        result = []
        for note in self.note_book:
            if find in note['data_of_create_or_change'][:10]:
                result.append(note)
        return result

    def get(self):
        return self.note_book

    def change(self, id_note_for_change: int, note_change: dict):
        date_note = datetime.datetime.now().strftime("%d.%m.%Y : %H.%M.%S")
        self.note_book[id_note_for_change]['header'] = note_change['header'] if note_change['header'] != '' else \
            self.note_book[id_note_for_change]['header']
        self.note_book[id_note_for_change]['content'] = note_change['content'] if note_change['content'] != "" else \
            self.note_book[id_note_for_change]['content']
        self.note_book[id_note_for_change]['data_of_create_or_change'] = date_note
