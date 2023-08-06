def who_felt_abandoned():
    people = {
        'Leslie': 'had_issues',
        'Kyle': 'tired_of_dealing'
    }

    for person, issue in people.items():
        if issue == 'had_issues':
            return person

print(who_felt_abandoned())  # This should print 'Leslie'