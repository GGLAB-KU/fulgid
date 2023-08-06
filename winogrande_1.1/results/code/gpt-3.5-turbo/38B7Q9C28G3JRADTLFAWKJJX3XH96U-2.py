def what_was_dirty():
    items = {
        'nozzles': 'object_polished',
        'rags': 'object_used_to_polish'
    }

    for item, description in items.items():
        if description == 'object_polished':
            return item

print(what_was_dirty())  # This should print 'nozzles'