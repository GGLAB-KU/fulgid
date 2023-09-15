box = {
    0: [],
    1: [],
    2: ['desert', 'pants', 'ring', 'branch'],
    3: [],
    4: [],
    5: ['razor', 'pot', 'keyboard', 'needle'],
    6: ['flute', 'harmonica'],
    7: [],
    8: ['tree', 'shoe', 'microscope', 'paint'],
    9: ['skirt', 'charger', 'ocean'],
    10: ['apple', 'sock', 'clock'],
    11: ['mountain', 'mirror', 'tie']
}

box[0] = ['lipstick']
box[5].remove('soap')
box[11].extend(['mirror', 'mountain', 'tie'])
box[11].extend(['soap', 'keyboard', 'pot'])
box[11].remove('keyboard')
box[11].remove('soap')
box[11].remove('pot')
box[0] = ['toothbrush']
box[6] = ['coin']
box[0].extend(['puzzle', 'toy', 'bird'])
box[9].remove('skirt')
box[9].remove('charger')
box[9].remove('ocean')
box[3].extend(['harmonica'])
box[2].remove('branch')
box[2].remove('desert')
box[2].remove('ring')
box[8].remove('mountain')
box[5] = ['glove']
box[1] = ['ocean']
box[1] = ['starfish']
box[5].remove('glove')
box[5].remove('razor')

for i in range(12):
    print(f"Box {i}: {box[i]}")