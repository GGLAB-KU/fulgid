def which_material_is_cheaper():
    items = {
        'doors': 'worse',
        'desks': 'better'
    }

    for item, quality in items.items():
        if quality == 'worse':
            return item

print(which_material_is_cheaper())  # This should print 'doors'