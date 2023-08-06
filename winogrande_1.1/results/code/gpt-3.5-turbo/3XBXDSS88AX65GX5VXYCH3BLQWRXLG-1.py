def where_did_he_go():
    options = {
        'cafe': 'paper_could_wait',
        'library': 'paper_could_not_wait'
    }

    for place, reason in options.items():
        if reason == 'paper_could_wait':
            return place

print(where_did_he_go())  # This should print 'cafe'