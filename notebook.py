import json
import os
import datetime

class Note:
    def __init__(self, note_id, title, body, timestamp):
        self.note_id = note_id
        self.title = title
        self.body = body
        self.timestamp = timestamp

class NoteApp:
    def __init__(self, file_path='notes.json'):
        self.file_path = file_path
        self.notes = self.load_notes()

    def load_notes(self):
        # Загрузка заметок из файла JSON, если файл существует
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                # Чтение строк из файла и преобразование каждой строки в объект Note
                notes_data = file.read().splitlines()
                return [self.parse_json(note_data) for note_data in notes_data]
        return []  # Возвращаем пустой список, если файла нет

    def parse_json(self, json_string):
        # Преобразование строки JSON в объект Note
        note_data = json.loads(json_string)
        return Note(**note_data)
    
    def save_notes(self):
        # Сохранение заметок в файл JSON
        with open(self.file_path, 'w') as file:
            for note in self.notes:
                # Преобразование объекта Note в строку JSON и запись в файл
                json_string = json.dumps(vars(note), separators=(',', ':'))
                file.write(json_string + '\n')
    
    def display_notes(self):
        # Вывод списка заметок в консоль
        if not self.notes:
            print("No notes available.")
        else:
            print("{:<5} {:<20} {:<20} {}".format('ID', 'Title', 'Timestamp', 'Body'))
            print("-" * 55)
            for note in self.notes:
                print("{:<5} {:<20} {:<20} {}".format(note.note_id, note.title, note.timestamp, note.body))

    def add_note(self, title, body):
        # Добавление новой заметки
        note_id = len(self.notes) + 1
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_note = Note(note_id, title, body, timestamp)
        self.notes.append(new_note)
        self.save_notes()
        print("Note added successfully.")

    def view_note(self, note_id):
        # Просмотр конкретной заметки
        note = next((n for n in self.notes if n.note_id == note_id), None)
        if note:
            print(f"Title: {note.title}\nBody: {note.body}\nTimestamp: {note.timestamp}")
        else:
            print("Note not found.")

    def edit_note(self, note_id, new_title, new_body):
        # Редактирование заметки
        note = next((n for n in self.notes if n.note_id == note_id), None)
        if note:
            note.title = new_title
            note.body = new_body
            note.timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.save_notes()
            print("Note edited successfully.")
        else:
            print("Note not found.")

    def delete_note(self, note_id):
        # Удаление заметки
        self.notes = [note for note in self.notes if note.note_id != note_id]
        self.save_notes()
        print("Note deleted successfully.")

if __name__ == "__main__":
    app = NoteApp()

    while True:
        # Основное меню приложения
        print("\nMenu:")
        print("1. Display Notes")
        print("2. Add Note")
        print("3. View Note")
        print("4. Edit Note")
        print("5. Delete Note")
        print("0. Exit")

        choice = input("Enter your choice: ")

        # Обработка выбора пользователя
        if choice == '1':
            app.display_notes()
        elif choice == '2':
            title = input("Enter note title: ")
            body = input("Enter note body: ")
            app.add_note(title, body)
        elif choice == '3':
            note_id = int(input("Enter note ID to view: "))
            app.view_note(note_id)
        elif choice == '4':
            note_id = int(input("Enter note ID to edit: "))
            new_title = input("Enter new title: ")
            new_body = input("Enter new body: ")
            app.edit_note(note_id, new_title, new_body)
        elif choice == '5':
            note_id = int(input("Enter note ID to delete: "))
            app.delete_note(note_id)
        elif choice == '0':
            break
        else:
            print("Invalid choice. Please try again.")