def what_was_cool_to_wear():
    items = {
        'hat': 'substitute_for_shirt',
        'shirt': 'cool_to_wear_to_school'
    }

    for item, description in items.items():
        if description == 'cool_to_wear_to_school':
            return item

print(what_was_cool_to_wear())  # This should print 'shirt'