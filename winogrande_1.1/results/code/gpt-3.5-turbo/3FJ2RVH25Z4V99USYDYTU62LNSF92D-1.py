def what_was_too_big():
    items = {
        'glow sticks': 'objects_to_use',
        'jars': 'containers'
    }

    for item, description in items.items():
        if description == 'containers':
            return item

print(what_was_too_big())  # This should print 'jars'