def who_was_placid():
    people = {
        'Amy': 'not placid',
        'Samantha': 'placid'
    }

    for person, state in people.items():
        if state == 'placid':
            return person

print(who_was_placid())  # This should print 'Samantha'