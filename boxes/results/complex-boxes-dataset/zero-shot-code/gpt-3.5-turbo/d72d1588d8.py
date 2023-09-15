box = {
    0: [],
    1: ['boot', 'star'],
    2: ['comet', 'note', 'horn'],
    3: ['flute', 'truck', 'piano', 'train', 'octopus'],
    4: [],
    5: [],
    6: ['sock', 'lamp', 'jacket', 'submarine', 'microscope'],
    7: ['mixer', 'boat'],
    8: ['spoon', 'starfish', 'fridge', 'makeup', 'bag'],
    9: ['magnet', 'glove']
}

box[8].remove('bag')
box[8].remove('spoon')
box[8].remove('fridge')
box[0].extend(['dress', 'rock', 'lipstick'])
box[8].remove('starfish')
box[8].append('mirror')
box[9].extend(['leaf', 'bicycle', 'frame'])
box[4].append('plate')
box[2].extend(['rock', 'lipstick', 'dress'])
box[7].remove('mixer')
box[7].append('desert')
box[1].remove('star')
box[6].remove('submarine')
box[1].extend(['starfish', 'mountain', 'button'])
box[9].remove('frame')
box[6].append('frame')
box[7].remove('boat')
box[7].append('truck')
box[9].remove('magnet')
box[9].append('piano')
box[6].remove('microscope')
box[6].append('truck')
box[1].remove('mountain')
box[9].remove('leaf')
box[1].append('leaf')
box[1].remove('boot')
box[4].remove('plate')
box[4].append('boot')

for i in range(10):
    print(f"Box {i}: {box[i]}")