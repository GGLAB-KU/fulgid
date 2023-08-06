def who_is_energetic():
    people = {
        'Christine': 'not_energetic',
        'Jessica': 'energetic'
    }

    for person, energy in people.items():
        if energy == 'energetic':
            return person

print(who_is_energetic())  # This should print 'Jessica'