def who_was_a_Jew():
    people = {
        'Eric': 'not_a_Jew',
        'Adam': 'a_Jew'
    }

    for person, religion in people.items():
        if religion == 'a_Jew':
            return person

print(who_was_a_Jew())  # This should print 'Adam'