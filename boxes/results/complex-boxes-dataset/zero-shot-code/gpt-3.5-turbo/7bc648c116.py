box = {
    0: ['boat', 'toothpaste'],
    1: ['fish', 'apple'],
    2: [],
    3: ['toothbrush', 'chair'],
    4: ['necklace', 'horse', 'hat', 'truck'],
    5: ['helmet'],
    6: ['fork', 'sandals', 'wig', 'bus'],
    7: [],
    8: ['skirt', 'grinder', 'harmonica'],
    9: ['keyboard'],
    10: ['lock', 'pan', 'piano', 'flute', 'clock'],
    11: ['paint', 'note'],
    12: ['oven', 'makeup', 'microwave'],
    13: []
}

box[10].remove('flute')
box[3].append('flute')

box[7].extend(box[1])
box[1].clear()

box[11].extend(box[8])
box[8].clear()

box[6].remove('bus')
box[6].remove('fork')
box[6].remove('sandals')

box[0].extend(['rain', 'phone'])

box[9].remove('keyboard')
box[9].append('usb')

box[0].append('helmet')
box[10].remove('chair')
box[10].append('cup')

box[9].remove('usb')
box[9].append('table')

box[9].clear()

box[10].remove('pan')
box[10].remove('cup')

box[12].extend(['elephant', 'tape'])

box[6].remove('wig')

box[11].remove('grinder')
box[10].append('grinder')
box[10].remove('lock')

box[4].remove('hat')
box[4].remove('truck')
box[4].remove('horse')

box[0].remove('phone')
box[12].append('phone')

box[12].clear()

box[4].remove('necklace')

box[1].append('whistle')

box[9].extend(['bag', 'river'])

for index, items in box.items():
    print(f"Box {index}: {items}")