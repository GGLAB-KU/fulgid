# Initial state of boxes
boxes = {
    0: ['shoe', 'basket'],
    1: ['snow', 'spoon', 'belt'],
    2: ['keyboard', 'umbrella'],
    3: ['magnet'],
    4: ['tie', 'sun', 'card', 'whistle'],
    5: ['wig', 'mixer', 'jacket'],
    6: [],
    7: ['harmonica', 'lamp', 'soap', 'cup', 'pen'],
    8: ['pot', 'dress'],
    9: ['necklace', 'rocket', 'telescope'],
    10: ['thread'],
    11: [],
    12: ['butterfly', 'ring', 'gloves', 'hat', 'fish'],
    13: ['chair']
}

# Empty Box 2.
boxes[2] = []

# Move the hat and the fish from Box 12 to Box 10.
items_to_move = ['hat', 'fish']
for item in items_to_move:
    boxes[12].remove(item)
    boxes[10].append(item)

# Remove the shoe from Box 0.
boxes[0].remove('shoe')

# Replace the fish and the hat and the thread with the sock and the cup and the scarf in Box 10.
boxes[10].remove('fish')
boxes[10].remove('hat')
boxes[10].remove('thread')
boxes[10].append('sock')
boxes[10].append('cup')
boxes[10].append('scarf')

# Put the crown into Box 5.
boxes[5].append('crown')

# Move the basket from Box 0 to Box 7.
boxes[0].remove('basket')
boxes[7].append('basket')

# Swap the magnet in Box 3 with the dress in Box 8.
boxes[3], boxes[8] = boxes[8], boxes[3]

# Replace the crown and the wig and the jacket with the motorcycle and the perfume and the mask in Box 5.
boxes[5].remove('crown')
boxes[5].remove('wig')
boxes[5].remove('jacket')
boxes[5].append('motorcycle')
boxes[5].append('perfume')
boxes[5].append('mask')

# Swap the chair in Box 13 with the snow in Box 1.
boxes[13], boxes[1] = boxes[1], boxes[13]

# Swap the mask in Box 5 with the necklace in Box 9.
boxes[5], boxes[9] = boxes[9], boxes[5]

# Move the butterfly from Box 12 to Box 6.
boxes[12].remove('butterfly')
boxes[6].append('butterfly')

# Swap the dress in Box 3 with the whistle in Box 4.
boxes[3], boxes[4] = boxes[4], boxes[3]

# Move the lamp and the pen and the basket from Box 7 to Box 3.
items_to_move = ['lamp', 'pen', 'basket']
for item in items_to_move:
    boxes[7].remove(item)
    boxes[3].append(item)

# Move the snow from Box 13 to Box 5.
boxes[13].remove('snow')
boxes[5].append('snow')

# Remove the chair from Box 1.
boxes[1].remove('chair')

# Replace the butterfly with the paint in Box 6.
boxes[6].remove('butterfly')
boxes[6].append('paint')

# Move the cup and the scarf from Box 10 to Box 4.
items_to_move = ['cup', 'scarf']
for item in items_to_move:
    boxes[10].remove(item)
    boxes[4].append(item)

# Move the ring and the gloves from Box 12 to Box 1.
items_to_move = ['ring', 'gloves']
for item in items_to_move:
    boxes[12].remove(item)
    boxes[1].append(item)

# Replace the telescope with the octopus in Box 9.
boxes[9].remove('telescope')
boxes[9].append('octopus')

# Put the paint and the sun into Box 7.
boxes[7].append('paint')
boxes[7].append('sun')

# Put the cup and the microwave into Box 8.
boxes[8].append('cup')
boxes[8].append('microwave')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")