def who_was_never_cold():
    people = {
        'Joel': 'liked_to_turn_heater_up',
        'Joseph': 'did_not_like_to_turn_heater_up'
    }

    for person, reason in people.items():
        if reason == 'liked_to_turn_heater_up':
            return person

print(who_was_never_cold())  # This should print 'Joel'