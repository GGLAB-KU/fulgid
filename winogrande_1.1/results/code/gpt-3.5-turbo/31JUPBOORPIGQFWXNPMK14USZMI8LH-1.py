def what_is_thin():
    options = {
        'sheet': 'object',
        'space': 'location'
    }

    for option, description in options.items():
        if description == 'location':
            return option

print(what_is_thin())  # This should print 'space'