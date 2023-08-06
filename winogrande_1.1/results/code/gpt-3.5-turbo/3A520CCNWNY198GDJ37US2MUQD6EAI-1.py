def what_was_flimsy():
    items = {
        'bark': 'surface',
        'stone': 'material'
    }

    for item, description in items.items():
        if description == 'surface':
            return item

print(what_was_flimsy())  # This should print 'bark'