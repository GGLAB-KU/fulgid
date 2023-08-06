def who_was_a_sinful_criminal():
    people = {
        'Monica': 'prosecuted',
        'Samantha': 'welcomed'
    }

    for person, action in people.items():
        if action == 'welcomed':
            return person

print(who_was_a_sinful_criminal())  # This should print 'Monica'