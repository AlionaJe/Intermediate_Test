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
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                notes_data = file.read().splitlines()
                return [self.parse_json(note_data) for note_data in notes_data]
        return []

    def parse_json(self, json_string):
        note_data = json.loads(json_string)
        return Note(**note_data)
    
    def save_notes(self):
        with open(self.file_path, 'w') as file:
            for note in self.notes:
                json_string = json.dumps(vars(note), separators=(',', ':'))
                file.write(json_string + '\n')
    
    def display_notes(self):
        if not self.notes:
            print("No notes available.")
        else:
            print("{:<5} {:<20} {:<20} {}".format('ID', 'Title', 'Timestamp', 'Body'))
            print("-" * 55)
            for note in self.notes:
                print("{:<5} {:<20} {:<20} {}".format(note.note_id, note.title, note.timestamp, note.body))

    def add_note(self, title, body):
        note_id = len(self.notes) + 1
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_note = Note(note_id, title, body, timestamp)
        self.notes.append(new_note)
        self.save_notes()
        print("Note added successfully.")

    def view_note(self, note_id):
        note = next((n for n in self.notes if n.note_id == note_id), None)
        if note:
            print(f"Title: {note.title}\nBody: {note.body}\nTimestamp: {note.timestamp}")
        else:
            print("Note not found.")

    def edit_note(self, note_id, new_title, new_body):
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
        self.notes = [note for note in self.notes if note.note_id != note_id]
        self.save_notes()
        print("Note deleted successfully.")

    


    
