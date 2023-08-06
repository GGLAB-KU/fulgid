def who_was_too_drunk():
    people = {
        'Carrie': 'cut_off',
        'Emily': 'continued_to_serve'
    }

    for person, action in people.items():
        if action == 'continued_to_serve':
            return person

print(who_was_too_drunk())  # This should print 'Emily'