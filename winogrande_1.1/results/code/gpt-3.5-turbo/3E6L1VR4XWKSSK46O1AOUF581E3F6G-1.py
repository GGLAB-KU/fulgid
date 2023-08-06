def who_thought_magician_was_good():
    people = {
        'Tanya': 'spent_more',
        'Amy': 'spent_less'
    }

    for person, spending in people.items():
        if spending == 'spent_more':
            return person

print(who_thought_magician_was_good())  # This should print 'Tanya'