# Initial state of boxes
boxes = {
    0: ['basket', 'sculpture'],
    1: ['laptop'],
    2: ['button', 'piano', 'jungle', 'shoe', 'butterfly'],
    3: ['shark', 'motorcycle'],
    4: ['apple', 'sun'],
    5: ['lamp', 'mixer', 'ship', 'speaker', 'bird'],
    6: [],
    7: ['lion', 'flute']
}

# Swap the shoe in Box 2 with the lion in Box 7.
boxes[2].remove('shoe')
boxes[7].remove('lion')
boxes[2].append('lion')
boxes[7].append('shoe')

# Remove the sun from Box 4.
boxes[4].remove('sun')

# Swap the shark in Box 3 with the shoe in Box 7.
boxes[3].remove('shark')
boxes[7].remove('shoe')
boxes[3].append('shoe')
boxes[7].append('shark')

# Replace the butterfly and the lion with the keyboard and the plane in Box 2.
boxes[2].remove('butterfly')
boxes[2].remove('lion')
boxes[2].append('keyboard')
boxes[2].append('plane')

# Put the violin and the sculpture into Box 4.
boxes[4].append('violin')
boxes[4].append('sculpture')

# Move the plane and the piano and the jungle from Box 2 to Box 6.
items_to_move = ['plane', 'piano', 'jungle']
for item in items_to_move:
    boxes[2].remove(item)
    boxes[6].append(item)

# Remove the apple from Box 4.
boxes[4].remove('apple')

# Remove the sculpture and the violin from Box 4.
boxes[4].remove('sculpture')
boxes[4].remove('violin')

# Remove the basket and the sculpture from Box 0.
boxes[0].remove('basket')
boxes[0].remove('sculpture')

# Move the shoe and the motorcycle from Box 3 to Box 4.
boxes[3].remove('shoe')
boxes[3].remove('motorcycle')
boxes[4].append('shoe')
boxes[4].append('motorcycle')

# Remove the keyboard and the button from Box 2.
boxes[2].remove('keyboard')
boxes[2].remove('button')

# Remove the laptop from Box 1.
boxes[1].remove('laptop')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")