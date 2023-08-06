def what_was_too_big():
    items = {
        'eggplant': 'object_to_bake',
        'toaster': 'place_to_bake_in'
    }

    for item, description in items.items():
        if description == 'object_to_bake':
            return item

print(what_was_too_big())  # This should print 'eggplant'
