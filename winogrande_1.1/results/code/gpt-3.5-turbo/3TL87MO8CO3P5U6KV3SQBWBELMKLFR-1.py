def who_was_lying():
    people = {
        'Tanya': 'excuse',
        'Emily': 'reason'
    }

    for person, role in people.items():
        if role == 'excuse':
            return person

print(who_was_lying())  # This should print 'Tanya'