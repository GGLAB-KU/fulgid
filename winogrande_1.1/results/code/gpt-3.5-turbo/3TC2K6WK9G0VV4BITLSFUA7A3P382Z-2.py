def who_had_a_good_job():
    people = {
        'Emily': 'not as much money',
        'Carrie': 'more money'
    }

    for person, financial_status in people.items():
        if financial_status == 'more money':
            return person

print(who_had_a_good_job())  # This should print 'Carrie'