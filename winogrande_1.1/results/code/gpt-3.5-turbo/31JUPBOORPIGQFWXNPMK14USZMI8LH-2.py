def what_is_wide():
    options = {
        'sheet': 'recovered',
        'space': 'between the space in the door'
    }

    for item, description in options.items():
        if description == 'between the space in the door':
            return item

print(what_is_wide())  # This should print 'space'