def what_fed_more_people():
    factors = {
        'portions': 'amount_of_food',
        'sizes': 'physical_dimensions'
    }

    for factor, description in factors.items():
        if description == 'amount_of_food':
            return factor

print(what_fed_more_people())  # This should print 'portions'