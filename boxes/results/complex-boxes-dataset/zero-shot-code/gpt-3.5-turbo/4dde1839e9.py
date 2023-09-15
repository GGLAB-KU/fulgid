box = {
    0: ['hat', 'charger', 'moon', 'rain', 'toothbrush'],
    1: ['belt', 'shampoo', 'motorcycle', 'oven'],
    2: ['submarine', 'paint', 'microscope', 'phone'],
    3: ['branch', 'skirt', 'cat', 'star'],
    4: ['key', 'meteor', 'island', 'earring', 'pillow'],
    5: ['necklace'],
    6: ['spoon', 'grinder', 'cow', 'note', 'shelf'],
    7: ['train', 'violin', 'shoes', 'mountain', 'octopus'],
    8: ['soap', 'battery', 'card', 'plane'],
    9: ['cloud', 'forest', 'thread', 'brush', 'puzzle'],
    10: [],
    11: ['tiger'],
    12: ['mask', 'boot', 'horse', 'flower', 'coat']
}

box[5].extend(['needle', 'coin'])
box[3].remove('star')
box[3].remove('skirt')
box[2].extend(['earring', 'pillow'])
box[12].extend(['toothpaste', 'candle'])
box[7].append('cup')
box[8].remove('soap')
box[9].remove('brush')
box[2].extend(box[1])
box[1] = []
box[11], box[3] = box[3], box[11]
box[5] = ['fish', 'grass', 'freezer']
box[3].remove('tiger')
box[9].extend(box[0][:3])
box[0] = box[0][3:]
box[12].remove('candle')
box[3].extend(['card', 'plane'])
box[0], box[5] = box[5], box[0]
box[6].extend(['octopus', 'wire', 'telescope'])
box[11] = []
box[3].remove('card')
box[3].remove('plane')
box[4], box[5] = box[5], box[4]

for i in range(13):
    print(f"Box {i}: {box[i]}")