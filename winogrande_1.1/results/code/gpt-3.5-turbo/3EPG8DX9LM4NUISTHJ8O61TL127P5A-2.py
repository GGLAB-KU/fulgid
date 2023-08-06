def who_watches_makeup_tutorials():
    people = {
        'Mary': 'helping',
        'Patricia': "daughter's mother"
    }

    for person, role in people.items():
        if role == "daughter's mother":
            return person

print(who_watches_makeup_tutorials())  # This should print 'Patricia'