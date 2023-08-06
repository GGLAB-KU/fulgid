def who_bought_gigantic_dog_bed():
    people = {
        'Mary': 'cool_dog',
        'Rachel': 'cooler_dog'
    }

    for person, opinion in people.items():
        if opinion == 'cooler_dog':
            return person

print(who_bought_gigantic_dog_bed())  # This should print 'Rachel'