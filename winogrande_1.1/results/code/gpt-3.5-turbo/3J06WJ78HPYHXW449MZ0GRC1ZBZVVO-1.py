def who_was_the_coach():
    people = {
        'Rachel': 'pushed_limits',
        'Megan': 'got_ready'
    }

    for person, action in people.items():
        if action == 'pushed_limits':
            return person

print(who_was_the_coach())  # This should print 'Rachel'