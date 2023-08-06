def who_made_the_mess():
    bakers = {
        'Hunter': 'better',
        'Logan': 'not as good'
    }

    for baker, skill in bakers.items():
        if skill == 'not as good':
            return baker

print(who_made_the_mess())  # This should print 'Logan'