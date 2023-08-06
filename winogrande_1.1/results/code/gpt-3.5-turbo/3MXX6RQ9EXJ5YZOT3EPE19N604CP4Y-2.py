def what_is_soft():
    items = {
        'phone': 'object_that_fell',
        'table': 'surface_it_fell_on'
    }

    for item, description in items.items():
        if description == 'surface_it_fell_on':
            return item

print(what_is_soft())  # This should print 'table'