def who_had_analytical_mind():
    players = {
        'Angela': 'easy',
        'Rebecca': 'not easy'
    }

    for player, ability in players.items():
        if ability == 'not easy':
            return player

print(who_had_analytical_mind())  # This should print 'Rebecca'