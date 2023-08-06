def what_was_canceled():
    events = {
        'story': 'reading_assignment',
        'class': 'class_session'
    }

    for event, description in events.items():
        if description == 'reading_assignment':
            return event

print(what_was_canceled())  # This should print 'story'