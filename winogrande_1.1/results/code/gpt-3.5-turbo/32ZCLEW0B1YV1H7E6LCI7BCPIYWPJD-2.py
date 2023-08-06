def who_violated_rights():
    people = {
        'Cynthia': 'violator',
        'Amy': 'passive_person'
    }

    for person, role in people.items():
        if role == 'passive_person':
            return person

print(who_violated_rights())  # This should print 'Amy'