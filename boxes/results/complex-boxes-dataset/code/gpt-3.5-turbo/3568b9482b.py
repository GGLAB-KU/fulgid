# Initial state of boxes
boxes = {
    0: ['needle', 'ring', 'puzzle'],
    1: ['ocean'],
    2: [],
    3: ['wig'],
    4: ['microwave', 'fish', 'shoes', 'coat'],
    5: [],
    6: ['speaker', 'helmet'],
    7: ['violin', 'forest', 'tree'],
    8: ['leaf', 'toothpaste'],
    9: [],
    10: ['soap', 'zipper', 'guitar', 'cloud', 'ship']
}

# Swap the wig in Box 3 with the helmet in Box 6.
boxes[3].remove('wig')
boxes[6].remove('helmet')
boxes[3].append('helmet')
boxes[6].append('wig')

# Put the skirt and the bag and the dog into Box 5.
items_to_move = ['skirt', 'bag', 'dog']
for item in items_to_move:
    boxes[5].append(item)

# Put the perfume into Box 2.
boxes[2].append('perfume')

# Put the apple and the shark and the bag into Box 9.
items_to_move = ['apple', 'shark', 'bag']
for item in items_to_move:
    boxes[9].append(item)

# Move the shark and the bag and the apple from Box 9 to Box 2.
items_to_move = ['shark', 'bag', 'apple']
for item in items_to_move:
    boxes[9].remove(item)
    boxes[2].append(item)

# Remove the ocean from Box 1.
boxes[1].remove('ocean')

# Empty Box 3.
boxes[3] = []

# Move the dog and the skirt and the bag from Box 5 to Box 3.
items_to_move = ['dog', 'skirt', 'bag']
for item in items_to_move:
    boxes[5].remove(item)
    boxes[3].append(item)

# Replace the leaf and the toothpaste with the butterfly and the mountain in Box 8.
boxes[8].remove('leaf')
boxes[8].remove('toothpaste')
boxes[8].append('butterfly')
boxes[8].append('mountain')

# Remove the wig and the speaker from Box 6.
boxes[6].remove('wig')
boxes[6].remove('speaker')

# Remove the perfume from Box 2.
boxes[2].remove('perfume')

# Replace the apple and the bag with the whistle and the plate in Box 2.
boxes[2].remove('apple')
boxes[2].remove('bag')
boxes[2].append('whistle')
boxes[2].append('plate')

# Swap the shoes in Box 4 with the tree in Box 7.
boxes[4].remove('shoes')
boxes[7].remove('tree')
boxes[4].append('tree')
boxes[7].append('shoes')

# Put the starfish into Box 7.
boxes[7].append('starfish')

# Replace the butterfly with the toothpaste in Box 8.
boxes[8].remove('butterfly')
boxes[8].append('toothpaste')

# Remove the zipper and the cloud from Box 10.
boxes[10].remove('zipper')
boxes[10].remove('cloud')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")