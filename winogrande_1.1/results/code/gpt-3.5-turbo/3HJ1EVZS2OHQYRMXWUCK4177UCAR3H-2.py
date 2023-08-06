def who_missed_the_taste():
    people = {
        'Angela': 'could_become_vegetarian',
        'Kayla': 'could_not_become_vegetarian'
    }

    for person, ability in people.items():
        if ability == 'could_not_become_vegetarian':
            return person

print(who_missed_the_taste())  # This should print 'Kayla'