# Initial state of boxes
boxes = {
    0: [],
    1: [],
    2: ['dog'],
    3: ['bicycle', 'shirt'],
    4: [],
    5: ['coin', 'shampoo', 'guitar', 'comb'],
    6: ['toothbrush', 'game', 'toothpaste']
}

# Move the game and the toothpaste and the toothbrush from Box 6 to Box 3.
items_to_move = ['game', 'toothpaste', 'toothbrush']
for item in items_to_move:
    boxes[6].remove(item)
    boxes[3].append(item)

# Replace the game with the lamp in Box 3.
boxes[3].remove('game')
boxes[3].append('lamp')

# Empty Box 3.
boxes[3] = []

# Move the guitar and the coin from Box 5 to Box 1.
items_to_move = ['guitar', 'coin']
for item in items_to_move:
    boxes[5].remove(item)
    boxes[1].append(item)

# Put the gloves into Box 2.
boxes[2].append('gloves')

# Swap the dog in Box 2 with the comb in Box 5.
boxes[2].remove('dog')
boxes[5].remove('comb')
boxes[2].append('comb')
boxes[5].append('dog')

# Remove the guitar and the coin from Box 1.
boxes[1].remove('guitar')
boxes[1].remove('coin')

# Put the headphone and the earring into Box 6.
boxes[6].append('headphone')
boxes[6].append('earring')

# Swap the headphone in Box 6 with the gloves in Box 2.
boxes[6].remove('headphone')
boxes[2].remove('gloves')
boxes[6].append('gloves')
boxes[2].append('headphone')

# Replace the shampoo with the necklace in Box 5.
boxes[5].remove('shampoo')
boxes[5].append('necklace')

# Swap the gloves in Box 6 with the dog in Box 5.
boxes[6].remove('gloves')
boxes[5].remove('dog')
boxes[6].append('dog')
boxes[5].append('gloves')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")