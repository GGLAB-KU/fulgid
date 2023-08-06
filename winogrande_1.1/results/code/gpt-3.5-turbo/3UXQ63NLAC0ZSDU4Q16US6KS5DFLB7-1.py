def what_is_large():
    items = {
        'body': 'part_of_pig',
        'grave': 'place_of_burial'
    }

    for item, description in items.items():
        if description == 'place_of_burial':
            return item

print(what_is_large())  # This should print 'grave'