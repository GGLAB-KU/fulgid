def who_bought_the_comic():
    readers = {
        'Lindsey': 'graphic_novels',
        'Natalie': 'classic_literature'
    }

    for reader, preference in readers.items():
        if preference == 'graphic_novels':
            return reader

print(who_bought_the_comic())  # This should print 'Lindsey'