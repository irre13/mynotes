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