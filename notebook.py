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
