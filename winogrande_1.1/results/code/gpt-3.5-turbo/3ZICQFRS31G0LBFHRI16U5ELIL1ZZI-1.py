def who_was_bitten_by_a_bird():
    people = {
        'Leslie': 'nervous',
        'Neil': 'not nervous'
    }

    for person, behavior in people.items():
        if behavior == 'not nervous':
            return person

print(who_was_bitten_by_a_bird())  # This should print 'Neil'