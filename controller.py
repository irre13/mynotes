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
                view.show_notes(nb.get())
                id_note_for_del = view.select_del_note()
                index_note_for_del = None
                try:
                    for j in range(len(nb.note_book)):
                        if nb.note_book[j]['id'] == id_note_for_del:
                            index_note_for_del = j
                    confirm = view.del_confirm(nb.note_book[index_note_for_del]['header'])
                    if confirm:
                        nb.delete(index_note_for_del)
                        view.view_changes()
                        nb.save()
                    else:
                        view.undo_changes()

                except TypeError:
                    view.input_error()
            case 4:
                pass
            case 5:
                find = view.find_note()
                result = nb.search(find)
                if result:
                    view.show_notes(result)
                else:
                    view.search_error()
            case 6:
                view.exit_prog()
            case _:
                view.input_error()
