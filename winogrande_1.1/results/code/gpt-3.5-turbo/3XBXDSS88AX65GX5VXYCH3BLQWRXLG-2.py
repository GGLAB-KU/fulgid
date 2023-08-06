def where_he_went():
    options = {
        'cafe': 'time_to_relax',
        'library': 'paper_due_soon'
    }

    for place, reason in options.items():
        if reason == 'paper_due_soon':
            return place

print(where_he_went())  # This should print 'library'