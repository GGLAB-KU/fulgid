box = {
    0: ['river', 'blender'],
    1: ['storm', 'boot'],
    2: ['grass', 'glasses', 'helmet'],
    3: [],
    4: ['boat', 'clock', 'shirt'],
    5: ['thread', 'brush'],
    6: [],
    7: ['button', 'sun'],
    8: [],
    9: ['toothpaste', 'magnet'],
    10: ['wallet', 'book', 'lightning', 'vase', 'perfume']
}

def print_boxes():
    for i in range(11):
        if i in box:
            print(f"Box {i}: {box[i]}")
        else:
            print(f"Box {i}: []")

print_boxes()

box[2].append('scissors')
box[10].remove('vase')
box[10].remove('lightning')
box[6].append(box[7].pop())
box[2].extend(box[4].pop(0) for _ in range(2))
box[4].remove('shirt')
box[4].remove('boat')
box[4].append(box[5].pop())
box[9].append(box[0].pop(0))
box[2].remove('shirt')
box[2].remove('boat')
box[5].extend(['comb', 'boat'])
box[6].append(box[1].pop())
box[0].append(box[1].pop())
box[5].extend(['comet', 'fridge'])
box[10].remove('storm')
box[10].remove('boot')
box[0], box[10] = box[10], box[0]
box[4].append('mixer')
box[4].append('starfish')
box[6].append(box[7].pop())
box[0], box[10] = box[10], box[0]
box[4].remove('starfish')
box[9].append('toothpaste')

print_boxes()