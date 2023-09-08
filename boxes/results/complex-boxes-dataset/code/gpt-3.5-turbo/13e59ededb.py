# Initial state of boxes
boxes = {
    0: ['makeup', 'card', 'cloud', 'magnet', 'toothpaste'],
    1: ['toaster'],
    2: ['river', 'glove'],
    3: ['sun', 'meteor'],
    4: ['car'],
    5: ['coral', 'tree', 'necklace'],
    6: ['pan', 'paint'],
    7: [],
    8: ['boat', 'comb'],
    9: ['star', 'whistle'],
    10: [],
    11: ['sandals', 'desert', 'battery', 'needle']
}

# Put the comb into Box 6.
boxes[6].append('comb')

# Move the river from Box 2 to Box 9.
boxes[2].remove('river')
boxes[9].append('river')

# Move the sun from Box 3 to Box 11.
boxes[3].remove('sun')
boxes[11].append('sun')

# Put the rock into Box 4.
boxes[4].append('rock')

# Swap the boat in Box 8 with the sun in Box 11.
boxes[8].remove('boat')
boxes[11].remove('sun')
boxes[8].append('sun')
boxes[11].append('boat')

# Swap the toaster in Box 1 with the glove in Box 2.
boxes[1].remove('toaster')
boxes[2].remove('glove')
boxes[1].append('glove')
boxes[2].append('toaster')

# Put the piano and the speaker and the tree into Box 10.
items_to_move = ['piano', 'speaker', 'tree']
for item in items_to_move:
    boxes[10].append(item)

# Put the skirt into Box 8.
boxes[8].append('skirt')

# Put the beach and the pen and the doll into Box 5.
items_to_move = ['beach', 'pen', 'doll']
for item in items_to_move:
    boxes[5].append(item)

# Move the car and the rock from Box 4 to Box 10.
items_to_move = ['car', 'rock']
for item in items_to_move:
    boxes[4].remove(item)
    boxes[10].append(item)

# Move the coral and the beach and the necklace from Box 5 to Box 11.
items_to_move = ['coral', 'beach', 'necklace']
for item in items_to_move:
    boxes[5].remove(item)
    boxes[11].append(item)

# Move the glove from Box 1 to Box 5.
boxes[1].remove('glove')
boxes[5].append('glove')

# Remove the paint and the pan and the comb from Box 6.
items_to_remove = ['paint', 'pan', 'comb']
for item in items_to_remove:
    boxes[6].remove(item)

# Move the glove and the doll and the pen from Box 5 to Box 0.
items_to_move = ['glove', 'doll', 'pen']
for item in items_to_move:
    boxes[5].remove(item)
    boxes[0].append(item)

# Move the tree from Box 5 to Box 6.
boxes[5].remove('tree')
boxes[6].append('tree')

# Put the lion and the magnet and the shirt into Box 2.
items_to_put = ['lion', 'magnet', 'shirt']
for item in items_to_put:
    boxes[2].append(item)

# Swap the speaker in Box 10 with the toothpaste in Box 0.
boxes[10].remove('speaker')
boxes[0].remove('toothpaste')
boxes[10].append('toothpaste')
boxes[0].append('speaker')

# Put the dress and the bag into Box 4.
items_to_put = ['dress', 'bag']
for item in items_to_put:
    boxes[4].append(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")