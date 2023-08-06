def who_went_to_bed_early():
    people = {
        'Jennifer': 'morning_person',
        'Natalie': 'not_morning_person'
    }

    for person, sleep_habit in people.items():
        if sleep_habit == 'not_morning_person':
            return person

print(who_went_to_bed_early())  # This should print 'Natalie'