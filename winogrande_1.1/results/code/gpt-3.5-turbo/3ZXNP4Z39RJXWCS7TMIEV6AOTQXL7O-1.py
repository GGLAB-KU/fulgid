def who_loves_the_color_of_their_eyes():
    people = {
        'Craig': 'clear_contacts',
        'William': 'colored_contacts'
    }

    for person, contacts in people.items():
        if contacts == 'clear_contacts':
            return person

print(who_loves_the_color_of_their_eyes())  # This should print 'Craig'