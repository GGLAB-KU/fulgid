def what_was_too_narrow():
    items = {
        'brush': 'object_to_paint_with',
        'crack': 'place_to_paint_on'
    }

    for item, description in items.items():
        if description == 'place_to_paint_on':
            return item

print(what_was_too_narrow())  # This should print 'crack'