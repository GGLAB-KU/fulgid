def who_was_bored():
    people = {
        'Jessica': 'enjoyed_simple_life',
        'Betty': 'bored_with_quiet_existence'
    }

    for person, feeling in people.items():
        if feeling == 'bored_with_quiet_existence':
            return person

print(who_was_bored())  # This should print 'Betty'