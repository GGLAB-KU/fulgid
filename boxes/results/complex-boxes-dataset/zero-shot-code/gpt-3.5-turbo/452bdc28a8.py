box = {
    0: ['crown', 'cup', 'lion'],
    1: ['scissors', 'cloud', 'rocket'],
    2: ['moon', 'speaker'],
    3: ['lightning', 'planet', 'razor', 'star'],
    4: ['shorts', 'shoes'],
    5: ['dog'],
    6: ['grass', 'table'],
    7: ['violin', 'soap', 'plane'],
    8: ['pillow', 'mirror', 'meteor'],
    9: ['button'],
    10: ['lipstick'],
    11: []
}

def print_boxes():
    for i in range(12):
        print(f"Box {i}: {box.get(i, [])}")

print_boxes()

box[6] = []
box[2] += ['swimsuit', 'toaster', 'button']
box[1] += ['spoon', 'wig']
box[0] = []
box[8] = ['coin', 'storm', 'magnet']
box[10] = ['swimsuit']
box[4].append(box[2].pop(box[2].index('button')))
box[5], box[2] = box[2], box[5]
box[6].append(box[5].pop(box[5].index('moon')))
box[9], box[10] = box[10], box[9]
box[3] = ['tape', 'fridge', 'apple']
box[10], box[3] = box[3], box[10]
box[11] += box[7]
box[11].append(box[10].pop(box[10].index('planet')))
box[1][2] = 'earring'
box[10][box[10].index('violin')] = 'rocket'
box[3] = []
box[8] = []

print_boxes()