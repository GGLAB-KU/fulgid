def what_was_hard():
    items = {
        'bark': 'surface',
        'stone': 'object'
    }

    for item, description in items.items():
        if description == 'surface':
            return item

print(what_was_hard())  # This should print 'bark'