# Initial state of boxes
boxes = {
    0: ['pen'],
    1: ['bear'],
    2: ['desert', 'pants', 'ring', 'branch'],
    3: ['soap'],
    4: [],
    5: ['razor', 'pot', 'keyboard', 'needle'],
    6: ['flute', 'harmonica'],
    7: [],
    8: ['tree', 'shoe', 'microscope', 'paint'],
    9: ['skirt', 'charger', 'ocean'],
    10: ['apple', 'sock', 'clock'],
    11: ['mountain', 'mirror', 'tie']
}

# Replace the pen with the lipstick in Box 0.
boxes[0].remove('pen')
boxes[0].append('lipstick')

# Move the soap from Box 3 to Box 5.
boxes[3].remove('soap')
boxes[5].append('soap')

# Remove the lipstick from Box 0.
boxes[0].remove('lipstick')

# Move the mirror and the mountain and the tie from Box 11 to Box 8.
items_to_move = ['mirror', 'mountain', 'tie']
for item in items_to_move:
    boxes[11].remove(item)
    boxes[8].append(item)

# Move the soap and the keyboard and the pot from Box 5 to Box 11.
items_to_move = ['soap', 'keyboard', 'pot']
for item in items_to_move:
    boxes[5].remove(item)
    boxes[11].append(item)

# Remove the keyboard and the soap and the pot from Box 11.
items_to_remove = ['keyboard', 'soap', 'pot']
for item in items_to_remove:
    boxes[11].remove(item)

# Put the toothbrush into Box 0.
boxes[0].append('toothbrush')

# Replace the harmonica with the coin in Box 6.
boxes[6].remove('harmonica')
boxes[6].append('coin')

# Put the puzzle and the toy and the bird into Box 0.
items_to_put = ['puzzle', 'toy', 'bird']
for item in items_to_put:
    boxes[0].append(item)

# Move the skirt and the charger and the ocean from Box 9 to Box 3.
items_to_move = ['skirt', 'charger', 'ocean']
for item in items_to_move:
    boxes[9].remove(item)
    boxes[3].append(item)

# Remove the bird and the toy and the puzzle from Box 0.
items_to_remove = ['bird', 'toy', 'puzzle']
for item in items_to_remove:
    boxes[0].remove(item)

# Put the harmonica into Box 3.
boxes[3].append('harmonica')

# Remove the branch and the desert and the ring from Box 2.
items_to_remove = ['branch', 'desert', 'ring']
for item in items_to_remove:
    boxes[2].remove(item)

# Remove the mountain from Box 8.
boxes[8].remove('mountain')

# Replace the needle with the glove in Box 5.
boxes[5].remove('needle')
boxes[5].append('glove')

# Move the ocean from Box 3 to Box 1.
boxes[3].remove('ocean')
boxes[1].append('ocean')

# Replace the bear with the starfish in Box 1.
boxes[1].remove('bear')
boxes[1].append('starfish')

# Remove the glove and the razor from Box 5.
items_to_remove = ['glove', 'razor']
for item in items_to_remove:
    boxes[5].remove(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")