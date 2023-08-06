def who_could_not_persuade():
    people = {
        'Amy': 'persuader',
        'Natalie': 'persuadee'
    }

    for person, role in people.items():
        if role == 'persuadee':
            return person

print(who_could_not_persuade())  # This should print 'Natalie'