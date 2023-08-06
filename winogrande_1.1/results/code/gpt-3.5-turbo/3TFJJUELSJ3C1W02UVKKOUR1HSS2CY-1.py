def whose_home_value_is_lower():
    homeowners = {
        'Rachel': 'old',
        'Betty': 'new'
    }

    for homeowner, roof_condition in homeowners.items():
        if roof_condition == 'old':
            return homeowner

print(whose_home_value_is_lower())  # This should print 'Rachel'