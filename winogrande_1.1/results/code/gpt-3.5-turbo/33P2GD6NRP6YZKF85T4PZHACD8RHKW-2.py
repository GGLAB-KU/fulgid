def what_lasted_one_year():
    events = {
        'battle': 'fierce',
        'war': 'great'
    }

    for event, description in events.items():
        if description == 'fierce':
            return event

print(what_lasted_one_year())  # This should print 'battle'