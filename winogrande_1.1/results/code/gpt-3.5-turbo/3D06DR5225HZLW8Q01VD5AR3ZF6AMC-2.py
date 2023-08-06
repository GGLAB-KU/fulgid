def what_was_too_little():
    options = {
        'work': 'activity',
        'strength': 'physical_ability'
    }

    for option, description in options.items():
        if description == 'physical_ability':
            return option

print(what_was_too_little())  # This should print 'strength'