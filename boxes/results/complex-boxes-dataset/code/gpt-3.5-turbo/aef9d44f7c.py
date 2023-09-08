# Initial state of boxes
boxes = {
    0: ['puzzle', 'chair', 'moon', 'apple'],
    1: ['candle', 'scarf'],
    2: ['lamp'],
    3: ['tape', 'blender', 'boot', 'lipstick'],
    4: ['game', 'perfume', 'laptop'],
    5: ['basket'],
    6: [],
    7: ['mask', 'ocean', 'magnet', 'storm', 'watch'],
    8: [],
    9: ['skirt'],
    10: ['doll', 'shoe']
}

# Swap the ocean in Box 7 with the skirt in Box 9.
boxes[7].remove('ocean')
boxes[9].remove('skirt')
boxes[7].append('skirt')
boxes[9].append('ocean')

# Swap the lamp in Box 2 with the perfume in Box 4.
boxes[2].remove('lamp')
boxes[4].remove('perfume')
boxes[2].append('perfume')
boxes[4].append('lamp')

# Move the lamp and the laptop from Box 4 to Box 5.
items_to_move = ['lamp', 'laptop']
for item in items_to_move:
    boxes[4].remove(item)
    boxes[5].append(item)

# Move the game from Box 4 to Box 1.
boxes[4].remove('game')
boxes[1].append('game')

# Put the headphone into Box 7.
boxes[7].append('headphone')

# Put the scarf into Box 10.
boxes[10].append('scarf')

# Put the shampoo and the charger and the umbrella into Box 2.
items_to_put = ['shampoo', 'charger', 'umbrella']
for item in items_to_put:
    boxes[2].append(item)

# Remove the skirt and the storm from Box 7.
boxes[7].remove('skirt')
boxes[7].remove('storm')

# Move the moon from Box 0 to Box 10.
boxes[0].remove('moon')
boxes[10].append('moon')

# Move the apple and the puzzle from Box 0 to Box 9.
items_to_move = ['apple', 'puzzle']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[9].append(item)

# Replace the perfume and the umbrella and the charger with the basket and the elephant and the keyboard in Box 2.
boxes[2].remove('perfume')
boxes[2].remove('umbrella')
boxes[2].remove('charger')
boxes[2].append('basket')
boxes[2].append('elephant')
boxes[2].append('keyboard')

# Remove the headphone and the mask from Box 7.
boxes[7].remove('headphone')
boxes[7].remove('mask')

# Move the apple and the puzzle from Box 9 to Box 10.
items_to_move = ['apple', 'puzzle']
for item in items_to_move:
    boxes[9].remove(item)
    boxes[10].append(item)

# Empty Box 2.
boxes[2] = []

# Move the game and the scarf from Box 1 to Box 2.
items_to_move = ['game', 'scarf']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[2].append(item)

# Move the doll from Box 10 to Box 4.
boxes[10].remove('doll')
boxes[4].append('doll')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")