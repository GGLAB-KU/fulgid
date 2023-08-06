def where_did_joe_go_first():
    places = {
        'bakery': 'substantial_supply',
        'bank': 'limited_supply'
    }

    for place, supply in places.items():
        if supply == 'substantial_supply':
            return place

print(where_did_joe_go_first())  # This should print 'bakery'