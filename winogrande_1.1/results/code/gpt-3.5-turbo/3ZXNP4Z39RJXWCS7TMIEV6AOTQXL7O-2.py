def who_dislikes_eye_color():
    people = {
        'Craig': 'clear_contacts',
        'William': 'colored_contacts'
    }

    for person, contacts in people.items():
        if contacts == 'colored_contacts':
            return person

print(who_dislikes_eye_color())  # This should print 'William'