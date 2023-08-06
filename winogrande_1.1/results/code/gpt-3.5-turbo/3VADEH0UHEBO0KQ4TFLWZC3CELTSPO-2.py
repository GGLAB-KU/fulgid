def who_confesses():
    people = {
        'Angela': 'thinks_husband_cheating',
        'Lindsey': 'suspected_as_cheating_partner'
    }

    for person, suspicion in people.items():
        if suspicion == 'thinks_husband_cheating':
            return person

print(who_confesses())  # This should print 'Angela'