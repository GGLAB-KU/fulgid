def who_watches_makeup_tutorials():
    people = {
        'Mary': 'helping',
        'Patricia': "Mary's daughter"
    }

    for person, role in people.items():
        if role == "helping":
            return person

print(who_watches_makeup_tutorials())  # This should print 'Mary'