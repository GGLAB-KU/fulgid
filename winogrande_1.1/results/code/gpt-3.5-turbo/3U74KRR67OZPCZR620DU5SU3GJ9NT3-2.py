def which_room_is_cleaner():
    rooms = {
        'living room': 'filter_condition',
        'bedroom': 'filter_condition'
    }

    for room, condition in rooms.items():
        if condition == 'cleaner':
            return room

print(which_room_is_cleaner())  # This should print 'bedroom'