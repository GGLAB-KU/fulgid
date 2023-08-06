def who_was_irresponsible():
    people = {
        'Craig': 'threw_cans_in_trash',
        'Benjamin': 'recycled'
    }

    for person, action in people.items():
        if action == 'threw_cans_in_trash':
            return person

print(who_was_irresponsible())  # This should print 'Craig'