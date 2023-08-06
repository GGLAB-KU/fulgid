def which_was_dirtier():
    rooms = {
        'living room': 'filter_dirtiness',
        'bedroom': 'filter_dirtiness'
    }

    for room, dirtiness in rooms.items():
        if dirtiness == 'filter_dirtiness':
            return room

print(which_was_dirtier())  # This should print 'living room'