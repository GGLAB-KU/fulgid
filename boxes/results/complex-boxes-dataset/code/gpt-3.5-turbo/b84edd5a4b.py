# Initial state of boxes
boxes = {
    0: ['game', 'battery', 'island', 'gloves', 'violin'],
    1: [],
    2: ['shampoo', 'snow'],
    3: ['toaster', 'sandals', 'boot', 'pillow', 'mixer'],
    4: ['truck', 'paint', 'clock', 'wire', 'sculpture'],
    5: [],
    6: ['candle', 'skirt', 'harmonica'],
    7: ['rock', 'dolphin', 'ocean', 'seaweed', 'flower'],
    8: ['glove'],
    9: ['storm', 'submarine', 'thunder', 'controller', 'lightning'],
    10: ['toothbrush'],
    11: ['apple', 'shirt', 'console', 'motorcycle', 'guitar'],
    12: ['ship', 'perfume', 'dice']
}

# Swap the truck in Box 4 with the console in Box 11.
boxes[4].remove('truck')
boxes[11].remove('console')
boxes[4].append('console')
boxes[11].append('truck')

# Move the clock and the wire and the paint from Box 4 to Box 9.
items_to_move = ['clock', 'wire', 'paint']
for item in items_to_move:
    boxes[4].remove(item)
    boxes[9].append(item)

# Swap the flower in Box 7 with the violin in Box 0.
boxes[7].remove('flower')
boxes[0].remove('violin')
boxes[7].append('violin')
boxes[0].append('flower')

# Put the tree into Box 8.
boxes[8].append('tree')

# Swap the shampoo in Box 2 with the skirt in Box 6.
boxes[2].remove('shampoo')
boxes[6].remove('skirt')
boxes[2].append('skirt')
boxes[6].append('shampoo')

# Put the doll and the hat and the card into Box 2.
items_to_move = ['doll', 'hat', 'card']
for item in items_to_move:
    boxes[2].append(item)

# Empty Box 7.
boxes[7] = []

# Put the truck and the fridge into Box 12.
items_to_move = ['truck', 'fridge']
for item in items_to_move:
    boxes[12].append(item)

# Move the pillow from Box 3 to Box 1.
boxes[3].remove('pillow')
boxes[1].append('pillow')

# Swap the card in Box 2 with the toaster in Box 3.
boxes[2].remove('card')
boxes[3].remove('toaster')
boxes[2].append('toaster')
boxes[3].append('card')

# Put the rocket into Box 3.
boxes[3].append('rocket')

# Put the lipstick and the toothbrush into Box 7.
items_to_move = ['lipstick', 'toothbrush']
for item in items_to_move:
    boxes[7].append(item)

# Empty Box 11.
boxes[11] = []

# Move the pillow from Box 1 to Box 7.
boxes[1].remove('pillow')
boxes[7].append('pillow')

# Put the octopus and the needle into Box 10.
items_to_move = ['octopus', 'needle']
for item in items_to_move:
    boxes[10].append(item)

# Put the storm and the boat into Box 4.
items_to_move = ['storm', 'boat']
for item in items_to_move:
    boxes[4].append(item)

# Swap the tree in Box 8 with the needle in Box 10.
boxes[8].remove('tree')
boxes[10].remove('needle')
boxes[8].append('needle')
boxes[10].append('tree')

# Move the storm and the controller and the submarine from Box 9 to Box 8.
items_to_move = ['storm', 'controller', 'submarine']
for item in items_to_move:
    boxes[9].remove(item)
    boxes[8].append(item)

# Replace the rocket and the card with the shoes and the shoe in Box 3.
boxes[3].remove('rocket')
boxes[3].remove('card')
boxes[3].append('shoes')
boxes[3].append('shoe')

# Move the controller and the glove and the needle from Box 8 to Box 4.
items_to_move = ['controller', 'glove', 'needle']
for item in items_to_move:
    boxes[8].remove(item)
    boxes[4].append(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")