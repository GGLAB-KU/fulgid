def what_was_too_much():
    items = {
        'food': 'amount_given',
        'distance': 'amount_traveled'
    }

    for item, description in items.items():
        if description == 'amount_traveled':
            return item

print(what_was_too_much())  # This should print 'distance'