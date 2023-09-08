# Initial state of boxes
boxes = {
    0: [],
    1: ['tiger', 'branch', 'rain', 'sculpture'],
    2: ['telescope'],
    3: ['fish'],
    4: [],
    5: ['pillow', 'whistle', 'candle', 'ship'],
    6: ['frame', 'toaster', 'keyboard', 'planet', 'magnet'],
    7: ['paint', 'scissors', 'blender'],
    8: [],
    9: ['coral', 'sandals', 'makeup'],
    10: ['earring', 'truck', 'blanket', 'pan']
}

# Move the telescope from Box 2 to Box 4.
boxes[2].remove('telescope')
boxes[4].append('telescope')

# Swap the branch in Box 1 with the keyboard in Box 6.
boxes[1].remove('branch')
boxes[6].remove('keyboard')
boxes[1].append('keyboard')
boxes[6].append('branch')

# Put the storm into Box 9.
boxes[9].append('storm')

# Move the blender and the paint and the scissors from Box 7 to Box 9.
items_to_move = ['blender', 'paint', 'scissors']
for item in items_to_move:
    boxes[7].remove(item)
    boxes[9].append(item)

# Put the bear and the watch into Box 2.
boxes[2].append('bear')
boxes[2].append('watch')

# Swap the fish in Box 3 with the earring in Box 10.
boxes[3].remove('fish')
boxes[10].remove('earring')
boxes[3].append('earring')
boxes[10].append('fish')

# Move the sculpture and the tiger and the keyboard from Box 1 to Box 9.
items_to_move = ['sculpture', 'tiger', 'keyboard']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[9].append(item)

# Put the microwave into Box 7.
boxes[7].append('microwave')

# Put the controller and the sun into Box 4.
boxes[4].append('controller')
boxes[4].append('sun')

# Move the magnet from Box 6 to Box 2.
boxes[6].remove('magnet')
boxes[2].append('magnet')

# Put the note into Box 3.
boxes[3].append('note')

# Put the wig into Box 0.
boxes[0].append('wig')

# Move the earring from Box 3 to Box 1.
boxes[3].remove('earring')
boxes[1].append('earring')

# Remove the whistle and the ship from Box 5.
boxes[5].remove('whistle')
boxes[5].remove('ship')

# Put the guitar and the forest and the bird into Box 9.
boxes[9].append('guitar')
boxes[9].append('forest')
boxes[9].append('bird')

# Remove the rain and the earring from Box 1.
boxes[1].remove('rain')
boxes[1].remove('earring')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")