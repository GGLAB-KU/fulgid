def who_was_less_experienced():
    artists = {
        'Benjamin': 'more experienced',
        'Brett': 'less experienced'
    }

    for artist, experience in artists.items():
        if experience == 'less experienced':
            return artist

print(who_was_less_experienced())  # This should print 'Brett'