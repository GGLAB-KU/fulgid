# Initial state of boxes
boxes = {
    0: ['coin', 'spoon'],
    1: ['rock'],
    2: ['desert', 'leaf', 'keyboard', 'shark'],
    3: ['dress', 'console', 'cat', 'laptop'],
    4: ['coat', 'toaster', 'candle', 'microscope'],
    5: ['truck', 'paint', 'bowl', 'speaker'],
    6: ['moon', 'shampoo', 'butterfly', 'jacket'],
    7: ['submarine', 'belt', 'shelf', 'shorts'],
    8: [],
    9: ['ring'],
    10: ['watch', 'wallet', 'mask']
}

# Replace the laptop and the dress with the usb and the apple in Box 3.
boxes[3].remove('laptop')
boxes[3].remove('dress')
boxes[3].append('usb')
boxes[3].append('apple')

# Put the island into Box 8.
boxes[8].append('island')

# Swap the moon in Box 6 with the submarine in Box 7.
boxes[6].remove('moon')
boxes[7].remove('submarine')
boxes[6].append('submarine')
boxes[7].append('moon')

# Swap the paint in Box 5 with the wallet in Box 10.
boxes[5].remove('paint')
boxes[10].remove('wallet')
boxes[5].append('wallet')
boxes[10].append('paint')

# Empty Box 4.
boxes[4] = []

# Move the coin from Box 0 to Box 4.
boxes[0].remove('coin')
boxes[4].append('coin')

# Move the spoon from Box 0 to Box 7.
boxes[0].remove('spoon')
boxes[7].append('spoon')

# Swap the shampoo in Box 6 with the rock in Box 1.
boxes[6].remove('shampoo')
boxes[1].remove('rock')
boxes[6].append('rock')
boxes[1].append('shampoo')

# Empty Box 7.
boxes[7] = []

# Move the ring from Box 9 to Box 0.
boxes[9].remove('ring')
boxes[0].append('ring')

# Put the leaf and the coin and the island into Box 6.
items_to_move = ['leaf', 'coin', 'island']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[6].append(item)

# Replace the ring with the vase in Box 0.
boxes[0].remove('ring')
boxes[0].append('vase')

# Put the sock into Box 0.
boxes[0].append('sock')

# Empty Box 1.
boxes[1] = []

# Remove the truck and the speaker from Box 5.
boxes[5].remove('truck')
boxes[5].remove('speaker')

# Move the rock and the butterfly and the leaf from Box 6 to Box 10.
items_to_move = ['rock', 'butterfly', 'leaf']
for item in items_to_move:
    boxes[6].remove(item)
    boxes[10].append(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")