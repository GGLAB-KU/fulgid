# Initial state of boxes
boxes = {
    0: ['lipstick'],
    1: ['key'],
    2: ['coral', 'pen', 'toothpaste'],
    3: ['piano', 'basket', 'toothbrush'],
    4: ['starfish'],
    5: ['dress', 'crown', 'boat', 'tiger', 'doll'],
    6: ['apple', 'rock'],
    7: [],
    8: ['button', 'charger'],
    9: [],
    10: []
}

# Replace the starfish with the motorcycle in Box 4.
boxes[4].remove('starfish')
boxes[4].append('motorcycle')

# Swap the lipstick in Box 0 with the button in Box 8.
boxes[0].remove('lipstick')
boxes[8].remove('button')
boxes[0].append('button')
boxes[8].append('lipstick')

# Move the button from Box 0 to Box 8.
boxes[0].remove('button')
boxes[8].append('button')

# Move the piano from Box 3 to Box 2.
boxes[3].remove('piano')
boxes[2].append('piano')

# Replace the pen and the piano and the toothpaste with the dog and the coat and the earring in Box 2.
boxes[2].remove('pen')
boxes[2].remove('piano')
boxes[2].remove('toothpaste')
boxes[2].append('dog')
boxes[2].append('coat')
boxes[2].append('earring')

# Remove the toothbrush from Box 3.
boxes[3].remove('toothbrush')

# Swap the motorcycle in Box 4 with the basket in Box 3.
boxes[4].remove('motorcycle')
boxes[3].remove('basket')
boxes[4].append('basket')
boxes[3].append('motorcycle')

# Put the table into Box 10.
boxes[10].append('table')

# Move the basket from Box 4 to Box 5.
boxes[4].remove('basket')
boxes[5].append('basket')

# Move the motorcycle from Box 3 to Box 0.
boxes[3].remove('motorcycle')
boxes[0].append('motorcycle')

# Remove the table from Box 10.
boxes[10].remove('table')

# Move the button and the lipstick and the charger from Box 8 to Box 7.
items_to_move = ['button', 'lipstick', 'charger']
for item in items_to_move:
    boxes[8].remove(item)
    boxes[7].append(item)

# Move the basket and the doll and the crown from Box 5 to Box 0.
items_to_move = ['basket', 'doll', 'crown']
for item in items_to_move:
    boxes[5].remove(item)
    boxes[0].append(item)

# Move the key from Box 1 to Box 4.
boxes[1].remove('key')
boxes[4].append('key')

# Put the perfume into Box 4.
boxes[4].append('perfume')

# Put the skirt and the basket and the candle into Box 9.
items_to_move = ['skirt', 'basket', 'candle']
for item in items_to_move:
    boxes[9].append(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")