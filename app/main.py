from notes_app import NotesApp

app = NotesApp()
app.load_notes()

while True:
    command = input("Введите команду (add/list/edit/delete/exit): ").strip()

    if command == "add":
        title = input("Введите заголовок заметки: ")
        body = input("Введите тело заметки: ")
        app.add_note(title, body)
        print("Заметка успешно сохранена")

    elif command == "list":
        date_filter = input("Введите дату (гггг-мм-дд) для фильтрации или оставьте пустым для вывода всех заметок: ")
        app.list_notes(date_filter)

    elif command == "edit":
        note_id = int(input("Введите ID заметки для редактирования: "))
        title = input("Введите новый заголовок заметки: ")
        body = input("Введите новое тело заметки: ")
        if app.edit_note(note_id, title, body):
            print("Заметка успешно отредактирована")
        else:
            print("Заметка с указанным ID не найдена")

    elif command == "delete":
        note_id = int(input("Введите ID заметки для удаления: "))
        if app.delete_note(note_id):
            print("Заметка успешно удалена")
        else:
            print("Заметка с указанным ID не найдена")

    elif command == "exit":
        break

    else:
        print("Неверная команда. Пожалуйста, попробуйте снова.")