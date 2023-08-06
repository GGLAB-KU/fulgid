def whose_wheels_were_new():
    people = {
        'Michael': 'new_wheels',
        'Leslie': 'old_wheels'
    }

    for person, wheels in people.items():
        if wheels == 'old_wheels':
            return person

print(whose_wheels_were_new())  # This should print 'Leslie'