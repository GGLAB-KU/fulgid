def what_was_short():
    options = {
        'story': 'reading_material',
        'class': 'time_period'
    }

    for option, description in options.items():
        if description == 'reading_material':
            return option

print(what_was_short())  # This should print 'story'