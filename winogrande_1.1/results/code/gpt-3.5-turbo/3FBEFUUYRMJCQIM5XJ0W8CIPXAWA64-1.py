def whose_wheels_were_old():
    people = {
        'Michael': 'new_wheels',
        'Leslie': 'old_wheels'
    }

    for person, wheels in people.items():
        if wheels == 'old_wheels':
            return person

print(whose_wheels_were_old())  # This should print 'Leslie'