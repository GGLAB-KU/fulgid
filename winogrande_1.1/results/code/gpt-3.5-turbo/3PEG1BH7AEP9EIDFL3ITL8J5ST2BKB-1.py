def what_was_too_tiny():
    options = {
        'ear': 'body_part',
        'piercing': 'object_to_get'
    }

    for option, description in options.items():
        if description == 'object_to_get':
            return option

print(what_was_too_tiny())  # This should print 'piercing'