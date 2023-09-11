# Initial state of boxes
boxes = {
    0: [],
    1: [],
    2: ['mountain', 'glove'],
    3: [],
    4: ['motorcycle', 'brush', 'basket'],
    5: [],
    6: ['flower', 'shorts', 'dog', 'watch'],
    7: [],
    8: ['toothbrush', 'storm', 'microscope', 'tie', 'vase'],
    9: ['phone', 'candle', 'car', 'fish'],
    10: ['blender', 'plate', 'whistle', 'thunder'],
    11: ['meteor'],
    12: ['telescope', 'razor', 'gloves', 'horse']
}

# Move the meteor from Box 11 to Box 0.
boxes[0].append(boxes[11].pop())

# Move the flower from Box 6 to Box 12.
boxes[12].append(boxes[6].pop(boxes[6].index('flower')))

# Move the shorts from Box 6 to Box 4.
boxes[4].append(boxes[6].pop(boxes[6].index('shorts')))

# Move the vase from Box 8 to Box 7.
boxes[7].append(boxes[8].pop(boxes[8].index('vase')))

# Move the flower from Box 12 to Box 3.
boxes[3].append(boxes[12].pop(boxes[12].index('flower')))

# Swap the meteor in Box 0 with the vase in Box 7.
boxes[0][0], boxes[7][0] = boxes[7][0], boxes[0][0]

# Remove the whistle and the blender and the thunder from Box 10.
items_to_remove = ['whistle', 'blender', 'thunder']
for item in items_to_remove:
    boxes[10].remove(item)

# Swap the vase in Box 0 with the glove in Box 2.
boxes[0][0], boxes[2][1] = boxes[2][1], boxes[0][0]

# Swap the meteor in Box 7 with the gloves in Box 12.
boxes[7][0], boxes[12][3] = boxes[12][3], boxes[7][0]

# Put the plane and the flute and the ring into Box 6.
items_to_put = ['plane', 'flute', 'ring']
for item in items_to_put:
    boxes[6].append(item)

# Move the tie and the storm and the toothbrush from Box 8 to Box 10.
items_to_move = ['tie', 'storm', 'toothbrush']
for item in items_to_move:
    boxes[8].remove(item)
    boxes[10].append(item)

# Replace the microscope with the headphone in Box 8.
boxes[8].remove('microscope')
boxes[8].append('headphone')

# Move the flower from Box 3 to Box 0.
boxes[0].append(boxes[3].pop())

# Move the gloves from Box 7 to Box 10.
boxes[10].extend(boxes[7])
boxes[7] = []

# Put the spoon and the button into Box 10.
items_to_put = ['spoon', 'button']
for item in items_to_put:
    boxes[10].append(item)

# Put the table and the boot and the tiger into Box 11.
items_to_put = ['table', 'boot', 'tiger']
for item in items_to_put:
    boxes[11].append(item)

# Put the book and the jungle into Box 10.
items_to_put = ['book', 'jungle']
for item in items_to_put:
    boxes[10].append(item)

# Remove the plane and the ring from Box 6.
items_to_remove = ['plane', 'ring']
for item in items_to_remove:
    boxes[6].remove(item)

# Move the flower from Box 0 to Box 3.
boxes[3].append(boxes[0].pop())

# Move the headphone from Box 8 to Box 6.
boxes[6].append(boxes[8].pop(boxes[8].index('headphone')))

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")