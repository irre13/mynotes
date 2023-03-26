import view as view
import model as model


def start():
    nb = model.Notebook()
    choice = ''
    nb.open()
    while choice != 6:
        choice = view.main_menu()
        match choice:
            case 1:
                new_id = nb.get_id(len(nb.note_book))
                new_note = dict(view.create_new_note(new_id))
                nb.new(new_note)
                nb.save()
                view.show_new_note(nb.note_book[-1])
            case 2:
                view.show_notes(nb.get())
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            case 6:
                view.exit_prog()
            case _:
                view.input_error()
