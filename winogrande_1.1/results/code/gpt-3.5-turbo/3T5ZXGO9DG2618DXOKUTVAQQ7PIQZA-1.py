def what_was_full_of_sugar():
    options = {
        'pie': 'dessert_option',
        'cookie': 'dessert_option'
    }

    for dessert, description in options.items():
        if description == 'dessert_option':
            return dessert

print(what_was_full_of_sugar())  # This should print 'pie'