def who_is_energized_by_cleaning():
    people = {
        'Leslie': 'excited',
        'Derrick': 'not excited'
    }

    for person, excitement in people.items():
        if excitement == 'not excited':
            return person

print(who_is_energized_by_cleaning())  # This should print 'Derrick'