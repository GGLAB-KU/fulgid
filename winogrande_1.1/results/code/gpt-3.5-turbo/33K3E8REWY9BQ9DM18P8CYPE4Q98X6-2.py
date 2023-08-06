def who_does_not_like_fried_eggs():
    people = {
        'Patricia': 'likes_fried_eggs',
        'Felicia': 'does_not_like_fried_eggs'
    }

    for person, preference in people.items():
        if preference == 'does_not_like_fried_eggs':
            return person

print(who_does_not_like_fried_eggs())  # This should print 'Felicia'