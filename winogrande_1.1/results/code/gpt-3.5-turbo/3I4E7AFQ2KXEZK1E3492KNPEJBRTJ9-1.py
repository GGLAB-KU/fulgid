def what_was_too_wide():
    items = {
        'brush': 'object_to_paint_with',
        'crack': 'object_to_paint'
    }

    for item, description in items.items():
        if description == 'object_to_paint':
            return item

print(what_was_too_wide())  # This should print 'crack'