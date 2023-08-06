def who_couldnt_afford_new_car():
    people = {
        'Brian': 'jealous',
        'Brett': 'owner_of_new_car'
    }

    for person, feeling in people.items():
        if feeling == 'jealous':
            return person

print(who_couldnt_afford_new_car())  # This should print 'Brian'