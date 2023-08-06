def what_was_too_huge():
    options = {
        'ear': 'body_part',
        'piercing': 'object'
    }

    for option, description in options.items():
        if description == 'body_part':
            return option

print(what_was_too_huge())  # This should print 'ear'