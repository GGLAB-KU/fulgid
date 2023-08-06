def who_made_peanut_chicken():
    people = {
        'Aaron': 'didn\'t know about the allergy',
        'Dennis': 'had a peanut allergy'
    }

    for person, condition in people.items():
        if condition == 'didn\'t know about the allergy':
            return person

print(who_made_peanut_chicken())  # This should print 'Aaron'