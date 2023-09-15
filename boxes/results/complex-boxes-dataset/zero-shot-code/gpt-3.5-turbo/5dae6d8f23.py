box = {
    0: ['keyboard', 'battery', 'razor', 'toaster'],
    1: ['frame'],
    2: [],
    3: ['starfish', 'microwave'],
    4: ['controller', 'fork', 'necklace', 'glove', 'leaf'],
    5: ['guitar', 'scissors', 'jacket', 'horse'],
    6: ['soap', 'basket'],
    7: ['freezer', 'button', 'piano'],
    8: ['car', 'candle'],
    9: [],
    10: ['lipstick', 'harmonica', 'swimsuit', 'towel'],
    11: [],
    12: ['dog'],
    13: ['makeup', 'card']
}

box[13].extend(['shampoo', 'cow', 'bear'])
box[5].remove('scissors')
box[5].remove('guitar')
box[5].remove('horse')
box[10].remove('towel')
box[10].append('pan')
box[8].remove('car')
box[8].append('shelf')
box[9].append('sock')
box[8].remove('shelf')
box[8].remove('candle')
box[8].append('scarf')
box[8].append('fish')
box[0].remove('lipstick')
box[0].remove('harmonica')
box[0].remove('swimsuit')
box[0].extend(['lipstick', 'harmonica', 'swimsuit'])
box[3], box[0] = box[0], box[3]
box[12].append('gloves')
box[6].remove('button')
box[6].remove('freezer')
box[6].remove('piano')
box[8].extend(['soap', 'freezer', 'button'])
box[1].remove('frame')
box[13].extend(['pan', 'harmonica'])
box[9] = []
box[11].extend(['shorts', 'doll'])
box[0].remove('razor')
box[0].remove('battery')
box[0].remove('lipstick')
box[6] = []
box[11] = []
box[4].remove('jacket')
box[11].extend(['necklace', 'controller', 'fork'])
box[13].remove('pan')
box[13].remove('cow')
box[13].remove('makeup')
box[2].extend(['pan', 'cow', 'makeup'])

for i in range(14):
    print(f"Box {i}: {box[i]}")