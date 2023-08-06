def which_material_is_stronger():
    items = {
        'doors': 'worse',
        'desks': 'better'
    }

    for item, quality in items.items():
        if quality == 'worse':
            return item

print(which_material_is_stronger())  # This should print 'doors'