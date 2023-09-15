box = {
    0: ['toaster'],
    1: ['sandals', 'dog'],
    2: ['tape'],
    3: ['laptop'],
    4: [],
    5: ['makeup'],
    6: ['headphone', 'drum'],
    7: ['horn', 'butterfly'],
    8: [],
    9: [],
    10: ['pan', 'sock', 'swimsuit', 'oven']
}

box[5] = ['magnet']
box[5], box[3] = box[3], box[5]
box[2] = ['mirror']
box[6].remove('laptop')
box[1], box[3] = box[3], box[1]
box[2] = ['jungle']
box[5] = ['crown']
box[6].remove('headphone')
box[8] = ['razor', 'wallet']
box[10] = ['dolphin', 'gloves', 'bus']
box[4] = box[1].pop(1)
box[4] = box[1].pop(0)
box[2] = []
box[7] = box[8]
box[3] = box[4]
box[1] = box[5]

for i in range(11):
    print(f"Box {i}: {box.get(i, [])}")