def who_felt_burdened():
    people = {
        'Brett': 'asked_for_advice',
        'Joel': 'gave_advice'
    }

    for person, action in people.items():
        if action == 'gave_advice':
            return person

print(who_felt_burdened())  # This should print 'Joel'