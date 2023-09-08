# Initial state of boxes
boxes = {
    0: ['necklace'],
    1: [],
    2: ['tie', 'cat', 'magnet'],
    3: ['guitar', 'tree', 'belt', 'razor', 'coat'],
    4: ['sculpture'],
    5: ['pen', 'flute', 'controller', 'game', 'glove'],
    6: ['fish', 'jacket', 'toy'],
    7: ['toothbrush', 'tiger', 'octopus', 'elephant'],
    8: ['scarf', 'toaster', 'desert', 'shirt'],
    9: ['pillow', 'bear', 'rocket', 'earring'],
    10: ['wig', 'shoe'],
    11: ['polish', 'needle', 'shampoo', 'whistle', 'pants']
}

# Empty Box 6.
boxes[6] = []

# Move the sculpture from Box 4 to Box 8.
boxes[4].remove('sculpture')
boxes[8].append('sculpture')

# Remove the octopus from Box 7.
boxes[7].remove('octopus')

# Put the basket and the book and the truck into Box 5.
items_to_put = ['basket', 'book', 'truck']
for item in items_to_put:
    boxes[5].append(item)

# Move the cat and the tie and the magnet from Box 2 to Box 4.
items_to_move = ['cat', 'tie', 'magnet']
for item in items_to_move:
    boxes[2].remove(item)
    boxes[4].append(item)

# Remove the toothbrush and the elephant from Box 7.
boxes[7].remove('toothbrush')
boxes[7].remove('elephant')

# Remove the guitar and the tree from Box 3.
boxes[3].remove('guitar')
boxes[3].remove('tree')

# Remove the glove from Box 5.
boxes[5].remove('glove')

# Put the boat into Box 7.
boxes[7].append('boat')

# Swap the necklace in Box 0 with the cat in Box 4.
boxes[0], boxes[4] = boxes[4], boxes[0]

# Move the earring and the pillow from Box 9 to Box 6.
items_to_move = ['earring', 'pillow']
for item in items_to_move:
    boxes[9].remove(item)
    boxes[6].append(item)

# Move the earring and the pillow from Box 6 to Box 0.
items_to_move = ['earring', 'pillow']
for item in items_to_move:
    boxes[6].remove(item)
    boxes[0].append(item)

# Swap the necklace in Box 4 with the pillow in Box 0.
boxes[0], boxes[4] = boxes[4], boxes[0]

# Remove the wig and the shoe from Box 10.
boxes[10].remove('wig')
boxes[10].remove('shoe')

# Move the scarf and the toaster from Box 8 to Box 7.
boxes[8].remove('scarf')
boxes[8].remove('toaster')
boxes[7].append('scarf')
boxes[7].append('toaster')

# Remove the bear and the rocket from Box 9.
boxes[9].remove('bear')
boxes[9].remove('rocket')

# Swap the coat in Box 3 with the boat in Box 7.
boxes[3], boxes[7] = boxes[7], boxes[3]

# Swap the tie in Box 4 with the desert in Box 8.
boxes[4], boxes[8] = boxes[8], boxes[4]

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")