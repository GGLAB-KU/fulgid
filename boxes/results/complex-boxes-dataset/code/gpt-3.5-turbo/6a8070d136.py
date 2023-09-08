# Initial state of boxes
boxes = {
    0: ['branch'],
    1: ['car', 'console', 'shoe', 'pillow'],
    2: ['needle', 'sock', 'desert'],
    3: ['snow', 'flower', 'elephant', 'note'],
    4: ['meteor', 'earring'],
    5: [],
    6: ['shampoo', 'candle', 'toaster', 'beach', 'flute'],
    7: ['basket', 'toothbrush'],
    8: ['lion'],
    9: [],
    10: ['bowl', 'shelf', 'razor', 'puzzle'],
    11: ['bus', 'oven'],
    12: ['coral', 'boat', 'chair'],
    13: ['glove']
}

# Swap the desert in Box 2 with the coral in Box 12.
boxes[2].remove('desert')
boxes[12].remove('coral')
boxes[2].append('coral')
boxes[12].append('desert')

# Put the sock and the snow and the motorcycle into Box 6.
items_to_move = ['sock', 'snow', 'motorcycle']
for item in items_to_move:
    boxes[2].remove(item)
    boxes[6].append(item)

# Empty Box 2.
boxes[2] = []

# Move the earring from Box 4 to Box 12.
boxes[4].remove('earring')
boxes[12].append('earring')

# Put the jungle into Box 11.
boxes[11].append('jungle')

# Remove the bus and the jungle from Box 11.
boxes[11].remove('bus')
boxes[11].remove('jungle')

# Swap the oven in Box 11 with the branch in Box 0.
boxes[11].remove('oven')
boxes[0].remove('branch')
boxes[11].append('branch')
boxes[0].append('oven')

# Empty Box 8.
boxes[8] = []

# Put the violin and the headphone and the sock into Box 7.
items_to_move = ['violin', 'headphone', 'sock']
for item in items_to_move:
    boxes[7].append(item)

# Move the meteor from Box 4 to Box 2.
boxes[4].remove('meteor')
boxes[2].append('meteor')

# Move the meteor from Box 2 to Box 12.
boxes[2].remove('meteor')
boxes[12].append('meteor')

# Remove the toaster from Box 6.
boxes[6].remove('toaster')

# Swap the branch in Box 11 with the razor in Box 10.
boxes[11].remove('branch')
boxes[10].remove('razor')
boxes[11].append('razor')
boxes[10].append('branch')

# Move the boat and the chair and the desert from Box 12 to Box 13.
items_to_move = ['boat', 'chair', 'desert']
for item in items_to_move:
    boxes[12].remove(item)
    boxes[13].append(item)

# Put the chair and the sock into Box 4.
items_to_move = ['chair', 'sock']
for item in items_to_move:
    boxes[4].append(item)

# Move the shoe and the console from Box 1 to Box 3.
items_to_move = ['shoe', 'console']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[3].append(item)

# Move the meteor from Box 12 to Box 7.
boxes[12].remove('meteor')
boxes[7].append('meteor')

# Swap the glove in Box 13 with the razor in Box 11.
boxes[13].remove('glove')
boxes[11].remove('razor')
boxes[13].append('razor')
boxes[11].append('glove')

# Swap the car in Box 1 with the razor in Box 13.
boxes[1].remove('car')
boxes[13].remove('razor')
boxes[1].append('razor')
boxes[13].append('car')

# Put the grass and the soap into Box 1.
items_to_move = ['grass', 'soap']
for item in items_to_move:
    boxes[1].append(item)

# Put the dolphin into Box 8.
boxes[8].append('dolphin')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")