def who_is_a_sober_alcoholic():
    people = {
        'Matthew': 'loves alcohol',
        'Ryan': 'can\'t stand alcohol'
    }

    for person, attitude in people.items():
        if attitude == 'can\'t stand alcohol':
            return person

print(who_is_a_sober_alcoholic())  # This should print 'Ryan'