def who_did_not_have_analytical_mind():
    players = {
        'Angela': 'had_analytical_mind',
        'Rebecca': 'did_not_have_analytical_mind'
    }

    for player, mind in players.items():
        if mind == 'did_not_have_analytical_mind':
            return player

print(who_did_not_have_analytical_mind())  # This should print 'Rebecca'