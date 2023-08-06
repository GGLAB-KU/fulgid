def who_was_disappointed():
    people = {
        'Nick': 'wanted_to_play',
        'Dennis': 'hesitant'
    }

    for person, state in people.items():
        if state == 'wanted_to_play':
            return person

print(who_was_disappointed())  # This should print 'Nick'