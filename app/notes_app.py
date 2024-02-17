import json
from datetime import datetime

class NotesApp:
    """
    Класс NotesApp представляет консольное приложение для работы с заметками.
    """

    def __init__(self):
        """
        Инициализирует новый экземпляр приложения NotesApp.
        """
        self.notes = []

    def load_notes(self):
        """
        Загружает заметки из файла 'notes.json' в список заметок приложения.
        """
        try:
            with open('notes.json', 'r') as file:
                self.notes = json.load(file)
        except FileNotFoundError:
            pass

    def save_notes(self):
        """
        Сохраняет текущие заметки в файл 'notes.json'.
        """
        with open('notes.json', 'w') as file:
            json.dump(self.notes, file)

    def list_notes(self, date_filter=None):
        """
        Выводит список заметок на экран.

        Параметры:
        - date_filter (str): Фильтр даты в формате 'гггг-мм-дд'.
        """
        for note in self.notes:
            if date_filter is None or date_filter in note['date']:
                print(f"ID: {note['id']}, Title: {note['title']}, Body: {note['body']}, Date: {note['date']}")

    def add_note(self, title, body):
        """
        Добавляет новую заметку с указанным заголовком и телом.

        Параметры:
        - title (str): Заголовок новой заметки.
        - body (str): Тело новой заметки.
        """
        note = {
            'id': len(self.notes) + 1,
            'title': title,
            'body': body,
            'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        self.notes.append(note)
        self.save_notes()

    def edit_note(self, note_id, title, body):
        """
        Редактирует существующую заметку с указанным идентификатором.

        Параметры:
        - note_id (int): Идентификатор заметки для редактирования.
        - title (str): Новый заголовок заметки.
        - body (str): Новое тело заметки.

        Возвращает:
        - bool: True, если заметка была успешно отредактирована, иначе False.
        """
        for note in self.notes:
            if note['id'] == note_id:
                note['title'] = title
                note['body'] = body
                note['date'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                self.save_notes()
                return True
        return False

    def delete_note(self, note_id):
        """
        Удаляет заметку с указанным идентификатором.

        Параметры:
        - note_id (int): Идентификатор заметки для удаления.

        Возвращает:
        - bool: True, если заметка была успешно удалена, иначе False.
        """
        for note in self.notes:
            if note['id'] == note_id:
                self.notes.remove(note)
                self.save_notes()
                return True
        return False