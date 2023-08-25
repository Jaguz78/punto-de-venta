# Flechitas
def avanzar(treeview):
    selected_item = treeview.selection()
    if selected_item:
        next_item = treeview.next(selected_item)
        if next_item:
            treeview.selection_set(next_item)
    else:
        treeview.selection_set(treeview.get_children()[0])

def retroceder(treeview):
    selected_item = treeview.selection() or treeview.get_children()[0]
    if selected_item:
        prev_item = treeview.prev(selected_item)
        if prev_item:
            treeview.selection_set(prev_item)
    else:
        treeview.selection_set(treeview.get_children()[-1])

def avanzarTodo(treeview):
    last_item = treeview.get_children()[-1]
    treeview.selection_set(last_item)

def retrocederTodo(treeview):
    first_item = treeview.get_children()[0]
    treeview.selection_set(first_item)