def who_was_always_cold():
    people = {
        'Joel': 'heater_turner',
        'Joseph': 'not_as_cold'
    }

    for person, reason in people.items():
        if reason == 'heater_turner':
            return person

print(who_was_always_cold())  # This should print 'Joel'