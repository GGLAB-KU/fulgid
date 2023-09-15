box = {
    0: ['car', 'moon', 'plate', 'blanket', 'desert'],
    1: [],
    2: ['planet', 'comb', 'meteor'],
    3: ['game', 'console', 'glasses'],
    4: ['phone', 'soap', 'tape', 'ocean', 'card'],
    5: ['lock', 'blender', 'cat', 'bowl', 'butterfly'],
    6: ['doll'],
    7: ['toothpaste', 'frame', 'sun', 'dress'],
    8: [],
    9: [],
    10: ['makeup'],
    11: ['snow', 'needle', 'island', 'earring']
}

def print_boxes():
    for i in range(12):
        if i in box:
            print(f"Box {i}: {box[i]}")
        else:
            print(f"Box {i}: []")

print_boxes()

box[8].append(box[6].pop(0))
box[2].remove('planet')
box[2].remove('meteor')
box[10].remove('makeup')
box[9].append(box[8].pop(0))
box[2].remove('comb')
box[11].remove('island')
box[11].remove('snow')
box[11].remove('earring')
box[7].append(box[11].pop(0))
box[3].remove('game')
box[3].remove('console')
box[1].append(box[9].pop(0))
box[0], box[5] = box[5], box[0]
box[1].pop(0)
box[3].extend(['skirt', 'coin', 'soap'])
box[6].append('belt')
box[7].remove('frame')
box[7].remove('toothpaste')
box[6].extend(['guitar', 'violin'])
box[7], box[0] = box[0], box[7]
box[3].extend(['moon', 'sun'])
box[3].extend(['skirt', 'glasses'])
box[9].extend(['sun', 'moon', 'glasses'])

print_boxes()