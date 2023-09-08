# Initial state of boxes
boxes = {
    0: ['helmet', 'controller', 'jacket', 'coral', 'thunder'],
    1: ['forest', 'cloud', 'lion', 'scissors'],
    2: ['blanket', 'doll', 'mask', 'bicycle', 'lipstick'],
    3: ['horn', 'bear', 'desert'],
    4: ['car', 'candle'],
    5: ['thread', 'toy', 'bird', 'pen'],
    6: ['microscope'],
    7: ['shorts'],
    8: ['freezer'],
    9: ['whistle', 'bus', 'jungle', 'sock'],
    10: ['skirt', 'dress', 'shampoo', 'glasses', 'brush'],
    11: ['keyboard', 'submarine', 'charger', 'puzzle', 'hat'],
    12: ['note']
}

# Put the leaf and the ocean into Box 2.
boxes[2].append('leaf')
boxes[2].append('ocean')

# Move the bus and the whistle and the jungle from Box 9 to Box 1.
items_to_move = ['bus', 'whistle', 'jungle']
for item in items_to_move:
    boxes[9].remove(item)
    boxes[1].append(item)

# Swap the car in Box 4 with the desert in Box 3.
boxes[4], boxes[3] = boxes[3], boxes[4]

# Put the truck and the storm into Box 12.
boxes[12].append('truck')
boxes[12].append('storm')

# Move the scissors and the cloud and the jungle from Box 1 to Box 8.
items_to_move = ['scissors', 'cloud', 'jungle']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[8].append(item)

# Replace the thread and the toy with the paint and the charger in Box 5.
boxes[5].remove('thread')
boxes[5].remove('toy')
boxes[5].append('paint')
boxes[5].append('charger')

# Put the phone into Box 12.
boxes[12].append('phone')

# Replace the pen and the paint and the charger with the speaker and the tree and the coin in Box 5.
boxes[5].remove('pen')
boxes[5].remove('paint')
boxes[5].remove('charger')
boxes[5].append('speaker')
boxes[5].append('tree')
boxes[5].append('coin')

# Swap the keyboard in Box 11 with the storm in Box 12.
boxes[11], boxes[12] = boxes[12], boxes[11]

# Move the phone and the keyboard and the truck from Box 12 to Box 1.
items_to_move = ['phone', 'keyboard', 'truck']
for item in items_to_move:
    boxes[12].remove(item)
    boxes[1].append(item)

# Put the chair and the piano and the apple into Box 8.
boxes[8].append('chair')
boxes[8].append('piano')
boxes[8].append('apple')

# Swap the keyboard in Box 1 with the car in Box 3.
boxes[1], boxes[3] = boxes[3], boxes[1]

# Replace the lion with the umbrella in Box 1.
boxes[1].remove('lion')
boxes[1].append('umbrella')

# Move the keyboard from Box 3 to Box 1.
boxes[3].remove('keyboard')
boxes[1].append('keyboard')

# Swap the leaf in Box 2 with the bus in Box 1.
boxes[2], boxes[1] = boxes[1], boxes[2]

# Replace the whistle and the forest and the keyboard with the phone and the plane and the sandals in Box 1.
boxes[1].remove('whistle')
boxes[1].remove('forest')
boxes[1].remove('keyboard')
boxes[1].append('phone')
boxes[1].append('plane')
boxes[1].append('sandals')

# Put the piano into Box 2.
boxes[2].append('piano')

# Remove the helmet from Box 0.
boxes[0].remove('helmet')

# Remove the shorts from Box 7.
boxes[7].remove('shorts')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")