def who_is_materialistic():
    people = {
        'Steven': 'believes_in_buying_happiness',
        'Craig': 'thinks_otherwise'
    }

    for person, belief in people.items():
        if belief == 'thinks_otherwise':
            return person

print(who_is_materialistic())  # This should print 'Craig'