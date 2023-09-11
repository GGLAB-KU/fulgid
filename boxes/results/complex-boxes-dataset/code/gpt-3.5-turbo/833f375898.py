# Initial state of boxes
boxes = {
    0: ['scarf', 'clock'],
    1: ['bus', 'rain', 'sculpture', 'fish'],
    2: ['mask', 'piano', 'bicycle', 'shampoo', 'star'],
    3: ['gloves', 'flute', 'umbrella', 'submarine'],
    4: ['helmet', 'comb', 'speaker', 'sandals', 'telescope'],
    5: ['laptop', 'watch', 'lipstick'],
    6: [],
    7: ['pot', 'fork', 'table', 'polish', 'blanket'],
    8: ['toy', 'wig', 'starfish', 'truck']
}

# Remove the clock from Box 0.
boxes[0].remove('clock')

# Put the rocket and the beach and the ship into Box 4.
boxes[4].extend(['rocket', 'beach', 'ship'])

# Swap the watch in Box 5 with the scarf in Box 0.
boxes[0].remove('scarf')
boxes[5].remove('watch')
boxes[0].append('watch')
boxes[5].append('scarf')

# Remove the wig and the truck from Box 8.
boxes[8].remove('wig')
boxes[8].remove('truck')

# Replace the submarine and the gloves and the umbrella with the glasses and the camera and the charger in Box 3.
boxes[3].remove('submarine')
boxes[3].remove('gloves')
boxes[3].remove('umbrella')
boxes[3].append('glasses')
boxes[3].append('camera')
boxes[3].append('charger')

# Swap the lipstick in Box 5 with the bus in Box 1.
boxes[1].remove('bus')
boxes[5].remove('lipstick')
boxes[1].append('lipstick')
boxes[5].append('bus')

# Swap the sandals in Box 4 with the bus in Box 5.
boxes[4].remove('sandals')
boxes[5].remove('bus')
boxes[4].append('bus')
boxes[5].append('sandals')

# Move the fish and the sculpture from Box 1 to Box 7.
items_to_move = ['fish', 'sculpture']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[7].append(item)

# Move the comb and the telescope from Box 4 to Box 8.
items_to_move = ['comb', 'telescope']
for item in items_to_move:
    boxes[4].remove(item)
    boxes[8].append(item)

# Remove the scarf and the sandals from Box 5.
boxes[5].remove('scarf')
boxes[5].remove('sandals')

# Swap the piano in Box 2 with the blanket in Box 7.
boxes[2].remove('piano')
boxes[7].remove('blanket')
boxes[2].append('blanket')
boxes[7].append('piano')

# Move the fish and the table and the fork from Box 7 to Box 8.
items_to_move = ['fish', 'table', 'fork']
for item in items_to_move:
    boxes[7].remove(item)
    boxes[8].append(item)

# Move the watch from Box 0 to Box 4.
boxes[0].remove('watch')
boxes[4].append('watch')

# Replace the camera and the flute with the fork and the table in Box 3.
boxes[3].remove('camera')
boxes[3].remove('flute')
boxes[3].append('fork')
boxes[3].append('table')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")