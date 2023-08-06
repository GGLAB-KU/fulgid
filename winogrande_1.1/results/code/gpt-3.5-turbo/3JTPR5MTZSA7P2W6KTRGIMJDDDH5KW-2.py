def who_didnt_have_second_serving():
    people = {
        'Laura': 'loved',
        'Felicia': 'hated'
    }

    for person, opinion in people.items():
        if opinion == 'loved':
            return person

print(who_didnt_have_second_serving())  # This should print 'Laura'