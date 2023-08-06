def what_was_too_much():
    options = {
        'work': 'activity',
        'strength': 'attribute'
    }

    for option, category in options.items():
        if category == 'activity':
            return option

print(what_was_too_much())  # This should print 'work'