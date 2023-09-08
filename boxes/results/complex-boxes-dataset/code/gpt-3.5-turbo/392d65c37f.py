# Initial state of boxes
boxes = {
    0: ['helmet', 'speaker'],
    1: ['bear', 'violin', 'crown', 'tie', 'polish'],
    2: ['storm', 'scissors', 'pants', 'tree'],
    3: ['dolphin', 'dice'],
    4: ['camera'],
    5: ['piano', 'usb'],
    6: ['thread', 'wallet'],
    7: ['bus', 'microwave']
}

# Move the thread from Box 6 to Box 1.
boxes[6].remove('thread')
boxes[1].append('thread')

# Put the guitar and the shorts and the tree into Box 1.
items_to_move = ['guitar', 'shorts', 'tree']
for item in items_to_move:
    boxes[1].append(item)

# Move the wallet from Box 6 to Box 5.
boxes[6].remove('wallet')
boxes[5].append('wallet')

# Move the pants and the scissors from Box 2 to Box 0.
items_to_move = ['pants', 'scissors']
for item in items_to_move:
    boxes[2].remove(item)
    boxes[0].append(item)

# Move the tree and the storm from Box 2 to Box 7.
items_to_move = ['tree', 'storm']
for item in items_to_move:
    boxes[2].remove(item)
    boxes[7].append(item)

# Move the storm and the bus from Box 7 to Box 4.
items_to_move = ['storm', 'bus']
for item in items_to_move:
    boxes[7].remove(item)
    boxes[4].append(item)

# Put the charger into Box 6.
boxes[6].append('charger')

# Replace the tree and the microwave with the seaweed and the polish in Box 7.
boxes[7].remove('tree')
boxes[7].remove('microwave')
boxes[7].append('seaweed')
boxes[7].append('polish')

# Move the charger from Box 6 to Box 1.
boxes[6].remove('charger')
boxes[1].append('charger')

# Swap the storm in Box 4 with the tie in Box 1.
boxes[4].remove('storm')
boxes[1].remove('tie')
boxes[4].append('tie')
boxes[1].append('storm')

# Move the dolphin and the dice from Box 3 to Box 5.
items_to_move = ['dolphin', 'dice']
for item in items_to_move:
    boxes[3].remove(item)
    boxes[5].append(item)

# Put the helmet and the watch into Box 6.
items_to_move = ['helmet', 'watch']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[6].append(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")