def where_was_fun():
    places = {
        'playground': 'not_fun',
        'house': 'fun'
    }

    for place, atmosphere in places.items():
        if atmosphere == 'fun':
            return place

print(where_was_fun())  # This should print 'house'