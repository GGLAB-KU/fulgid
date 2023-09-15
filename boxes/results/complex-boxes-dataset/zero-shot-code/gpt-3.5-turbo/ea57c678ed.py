box = {
    0: ['moon', 'flower', 'bracelet', 'console'],
    1: [],
    2: [],
    3: ['earring', 'whistle'],
    4: ['submarine', 'microwave', 'charger'],
    5: ['apple', 'shoe', 'cloud', 'drum', 'seaweed'],
    6: ['grass'],
    7: ['razor', 'motorcycle'],
    8: ['sun', 'speaker', 'bell', 'comb'],
    9: ['star', 'horn', 'mirror', 'shorts', 'grinder'],
    10: ['watch', 'mask', 'telescope'],
    11: ['tape'],
    12: ['violin', 'sculpture'],
    13: ['lipstick', 'sandals']
}

def print_box_contents():
    for i in range(14):
        if i in box:
            print(f"Box {i}: {box[i]}")
        else:
            print(f"Box {i}: []")

print_box_contents()

# Perform operations
box[7].append('watch')
box[11].extend(['scarf', 'lock'])
box[0].remove('flower')
box[5][box[5].index('apple')] = 'sandals'
box[13][box[13].index('sandals')] = 'apple'
box[13].extend(box[4].pop(1))
box[13].extend(box[4].pop(0))
box[6].extend(box[13].pop(box[13].index('apple')))
box[6].extend(box[13].pop(box[13].index('microwave')))
box[5].append('toothpaste')
box[5][box[5].index('seaweed')], box[3][box[3].index('whistle')] = box[3][box[3].index('whistle')], box[5][box[5].index('seaweed')]
box[13][box[13].index('charger')] = 'coin'
box[1].extend([box[5].pop(box[5].index('whistle')), box[5].pop(box[5].index('toothpaste'))])
box[12].extend(box[0].pop(box[0].index('console')))
box[12].extend(box[0].pop(box[0].index('bracelet')))
box[12].extend(box[0].pop(box[0].index('moon')))
box[5].append('truck')
box[11].remove('scarf')
box[11].remove('lock')
box[11].remove('tape')
box[3][box[3].index('seaweed')], box[8][box[8].index('bell')] = box[8][box[8].index('bell')], box[3][box[3].index('seaweed')]
box[12].extend(box[9].pop(box[9].index('mirror')))
box[12].extend(box[9].pop(box[9].index('grinder')))
box[12].extend(box[9].pop(box[9].index('shorts')))
box[12].clear()
box[9][box[9].index('horn')], box[9][box[9].index('star')] = 'dolphin', 'battery'
box[10].extend(['ocean', 'skirt'])
box[13].append('truck')
box[6].extend([box[5].pop(box[5].index('drum')), box[5].pop(box[5].index('shoe'))])
box[10].append(box[4].pop(box[4].index('submarine')))

print_box_contents()