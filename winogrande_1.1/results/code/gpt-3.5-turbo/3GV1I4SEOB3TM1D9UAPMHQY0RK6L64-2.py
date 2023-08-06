def who_could_not_be_convinced():
    people = {
        'Amy': 'thought she was the mirror image',
        'Natalie': 'could not be convinced to see the similarity'
    }

    for person, belief in people.items():
        if belief == 'could not be convinced to see the similarity':
            return person

print(who_could_not_be_convinced())  # This should print 'Natalie'