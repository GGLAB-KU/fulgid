def who_told_them():
    people = {
        'Randy': 'giver',
        'Brian': 'receiver'
    }

    for person, role in people.items():
        if role == 'receiver':
            return person

print(who_told_them())  # This should print 'Brian'