def who_bought_small_dog_bed():
    people = {
        'Mary': 'thought_poodles_were_cool',
        'Rachel': 'thought_Great_Danes_were_cooler'
    }

    for person, opinion in people.items():
        if opinion == 'thought_poodles_were_cool':
            return person

print(who_bought_small_dog_bed())  # This should print 'Mary'