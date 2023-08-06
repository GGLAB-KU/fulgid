def what_was_too_small():
    items = {
        'letters': 'objects_to_read',
        'eyes': 'organs_to_read_with'
    }

    for item, description in items.items():
        if description == 'organs_to_read_with':
            return item

print(what_was_too_small())  # This should print 'eyes'