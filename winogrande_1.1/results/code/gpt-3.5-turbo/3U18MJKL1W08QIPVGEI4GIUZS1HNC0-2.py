def who_is_good_with_kids():
    people = {
        'Joel': 'researched_laws',
        'Eric': 'preschool_opening'
    }

    for person, skill in people.items():
        if skill == 'preschool_opening':
            return person

print(who_is_good_with_kids())  # This should print 'Eric'