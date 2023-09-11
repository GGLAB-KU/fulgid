# Initial state of boxes
boxes = {
    0: ['shampoo'],
    1: ['ocean', 'bird', 'thread', 'dolphin'],
    2: ['piano', 'phone'],
    3: ['freezer'],
    4: [],
    5: ['wig', 'dice', 'gloves'],
    6: ['shelf', 'tiger'],
    7: ['butterfly'],
    8: ['boat', 'rocket'],
    9: [],
    10: ['skirt', 'coin', 'note', 'grinder']
}

# Swap the shampoo in Box 0 with the freezer in Box 3.
boxes[0], boxes[3] = boxes[3], boxes[0]

# Put the grinder and the piano into Box 3.
boxes[3].append('grinder')
boxes[3].append('piano')

# Move the grinder and the piano and the shampoo from Box 3 to Box 4.
items_to_move = ['grinder', 'piano', 'shampoo']
for item in items_to_move:
    boxes[3].remove(item)
    boxes[4].append(item)

# Swap the shelf in Box 6 with the dice in Box 5.
boxes[6], boxes[5] = boxes[5], boxes[6]

# Move the gloves and the wig from Box 5 to Box 7.
items_to_move = ['gloves', 'wig']
for item in items_to_move:
    boxes[5].remove(item)
    boxes[7].append(item)

# Replace the freezer with the charger in Box 0.
boxes[0].remove('freezer')
boxes[0].append('charger')

# Replace the charger with the bird in Box 0.
boxes[0].remove('charger')
boxes[0].append('bird')

# Replace the dolphin and the bird with the headphone and the table in Box 1.
boxes[1].remove('dolphin')
boxes[1].remove('bird')
boxes[1].append('headphone')
boxes[1].append('table')

# Remove the bird from Box 0.
boxes[0].remove('bird')

# Remove the note from Box 10.
boxes[10].remove('note')

# Empty Box 8.
boxes[8] = []

# Put the submarine and the candle and the toaster into Box 9.
boxes[9].append('submarine')
boxes[9].append('candle')
boxes[9].append('toaster')

# Move the gloves and the butterfly from Box 7 to Box 4.
items_to_move = ['gloves', 'butterfly']
for item in items_to_move:
    boxes[7].remove(item)
    boxes[4].append(item)

# Replace the shelf with the lamp in Box 5.
boxes[5].remove('shelf')
boxes[5].append('lamp')

# Put the pants and the doll into Box 8.
boxes[8].append('pants')
boxes[8].append('doll')

# Move the coin from Box 10 to Box 3.
boxes[10].remove('coin')
boxes[3].append('coin')

# Swap the candle in Box 9 with the coin in Box 3.
boxes[9], boxes[3] = boxes[3], boxes[9]

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")