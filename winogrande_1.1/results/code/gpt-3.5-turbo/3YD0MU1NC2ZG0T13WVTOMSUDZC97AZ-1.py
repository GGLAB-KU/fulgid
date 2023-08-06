def who_did_not_try():
    people = {
        'Christine': 'planner',
        'Kayla': 'target'
    }

    for person, role in people.items():
        if role == 'planner':
            return person

print(who_did_not_try())  # This should print 'Christine'