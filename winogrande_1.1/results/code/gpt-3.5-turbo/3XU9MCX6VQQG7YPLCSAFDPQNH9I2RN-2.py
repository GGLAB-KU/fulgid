def who_ate_peanut_chicken():
    people = {
        'Aaron': 'didn\'t know about the allergy',
        'Dennis': 'had a peanut allergy'
    }

    for person, condition in people.items():
        if condition == 'had a peanut allergy':
            return person

print(who_ate_peanut_chicken())  # This should print 'Dennis'