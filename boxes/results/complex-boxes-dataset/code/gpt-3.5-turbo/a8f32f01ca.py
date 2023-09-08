# Initial state of boxes
boxes = {
    0: ['scarf', 'ocean', 'octopus', 'pants', 'freezer'],
    1: ['branch', 'telescope'],
    2: ['coat', 'bowl', 'shirt'],
    3: ['rocket', 'boot', 'shelf', 'toothbrush'],
    4: [],
    5: ['car'],
    6: ['tape', 'beach', 'dog', 'sun', 'console'],
    7: ['rain', 'laptop'],
    8: ['keyboard', 'cow'],
    9: []
}

# Remove the beach and the dog from Box 6.
boxes[6].remove('beach')
boxes[6].remove('dog')

# Move the sun and the console and the tape from Box 6 to Box 4.
items_to_move = ['sun', 'console', 'tape']
for item in items_to_move:
    boxes[6].remove(item)
    boxes[4].append(item)

# Move the keyboard and the cow from Box 8 to Box 4.
items_to_move = ['keyboard', 'cow']
for item in items_to_move:
    boxes[8].remove(item)
    boxes[4].append(item)

# Replace the cow and the console and the keyboard with the gloves and the comet and the branch in Box 4.
boxes[4].remove('cow')
boxes[4].remove('console')
boxes[4].remove('keyboard')
boxes[4].append('gloves')
boxes[4].append('comet')
boxes[4].append('branch')

# Swap the tape in Box 4 with the branch in Box 1.
boxes[4].remove('tape')
boxes[1].remove('branch')
boxes[4].append('branch')
boxes[1].append('tape')

# Put the keyboard into Box 5.
boxes[8].remove('keyboard')
boxes[5].append('keyboard')

# Remove the sun and the branch from Box 4.
boxes[4].remove('sun')
boxes[4].remove('branch')

# Move the shelf and the boot from Box 3 to Box 1.
items_to_move = ['shelf', 'boot']
for item in items_to_move:
    boxes[3].remove(item)
    boxes[1].append(item)

# Empty Box 1.
boxes[1] = []

# Swap the car in Box 5 with the gloves in Box 4.
boxes[5].remove('car')
boxes[4].remove('gloves')
boxes[5].append('gloves')
boxes[4].append('car')

# Move the rain from Box 7 to Box 4.
boxes[7].remove('rain')
boxes[4].append('rain')

# Put the shorts and the coral into Box 4.
boxes[4].append('shorts')
boxes[4].append('coral')

# Remove the laptop from Box 7.
boxes[7].remove('laptop')

# Move the bowl from Box 2 to Box 5.
boxes[2].remove('bowl')
boxes[5].append('bowl')

# Remove the bowl and the gloves and the keyboard from Box 5.
items_to_remove = ['bowl', 'gloves', 'keyboard']
for item in items_to_remove:
    boxes[5].remove(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")