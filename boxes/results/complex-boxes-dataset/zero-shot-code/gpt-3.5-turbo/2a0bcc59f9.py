box = {
    0: [],
    1: [],
    2: ['mountain', 'glove'],
    3: [],
    4: ['motorcycle', 'brush', 'basket'],
    5: [],
    6: ['dog', 'watch'],
    7: [],
    8: ['toothbrush', 'storm', 'microscope', 'tie', 'vase'],
    9: ['phone', 'candle', 'car', 'fish'],
    10: ['blender', 'plate', 'whistle', 'thunder'],
    11: ['meteor'],
    12: ['telescope', 'razor', 'gloves', 'horse']
}

def move_item(source_box, destination_box, item):
    box[source_box].remove(item)
    box[destination_box].append(item)

def swap_items(box1, item1, box2, item2):
    box[box1].remove(item1)
    box[box1].append(item2)
    box[box2].remove(item2)
    box[box2].append(item1)

move_item(11, 0, 'meteor')
move_item(6, 12, 'flower')
move_item(6, 4, 'shorts')
move_item(8, 7, 'vase')
move_item(12, 3, 'flower')
swap_items(0, 'meteor', 7, 'vase')
box[10].remove('whistle')
box[10].remove('blender')
box[10].remove('thunder')
swap_items(0, 'vase', 2, 'glove')
swap_items(7, 'meteor', 12, 'gloves')
box[6].extend(['plane', 'flute', 'ring'])
move_item(8, 10, 'tie')
move_item(8, 10, 'storm')
move_item(8, 10, 'toothbrush')
box[8].remove('microscope')
box[8].append('headphone')
move_item(3, 0, 'flower')
move_item(7, 10, 'gloves')
box[10].extend(['spoon', 'button'])
box[11].extend(['table', 'boot', 'tiger'])
box[10].extend(['book', 'jungle'])
box[6].remove('plane')
box[6].remove('ring')
move_item(0, 3, 'flower')
move_item(8, 6, 'headphone')

for i in range(13):
    print(f"Box {i}: {box[i]}")