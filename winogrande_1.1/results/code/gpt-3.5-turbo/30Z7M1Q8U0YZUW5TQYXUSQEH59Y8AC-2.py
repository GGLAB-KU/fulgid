def what_is_very_warm():
    items = {
        'cup': 'object',
        'air': 'element'
    }

    for item, description in items.items():
        if description == 'object':
            return item

print(what_is_very_warm())  # This should print 'cup'