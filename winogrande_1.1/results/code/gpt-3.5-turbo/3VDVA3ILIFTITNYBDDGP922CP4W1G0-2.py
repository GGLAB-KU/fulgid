def who_is_more_likely_professor():
    people = {
        'Donald': 'understanding_of_math',
        'Joseph': 'understanding_of_math'
    }

    for person, understanding in people.items():
        if understanding == 'understanding_of_math':
            return person

print(who_is_more_likely_professor())  # This should print 'Joseph'