# Initial state of boxes
boxes = {
    0: ['snow', 'chair'],
    1: ['dice'],
    2: ['doll'],
    3: ['lipstick', 'elephant'],
    4: [],
    5: ['boat', 'usb', 'shirt'],
    6: ['battery', 'paint', 'dog', 'controller', 'blender'],
    7: ['earring', 'guitar', 'comet', 'thread'],
    8: ['planet'],
    9: [],
    10: ['basket'],
    11: ['shelf']
}

# Put the storm into Box 6.
boxes[6].append('storm')

# Put the swimsuit and the jungle and the pot into Box 1.
items_to_add = ['swimsuit', 'jungle', 'pot']
for item in items_to_add:
    boxes[1].append(item)

# Remove the chair from Box 0.
boxes[0].remove('chair')

# Replace the doll with the earring in Box 2.
boxes[2].remove('doll')
boxes[2].append('earring')

# Replace the planet with the lamp in Box 8.
boxes[8].remove('planet')
boxes[8].append('lamp')

# Replace the earring with the bicycle in Box 2.
boxes[2].remove('earring')
boxes[2].append('bicycle')

# Move the comet and the thread and the earring from Box 7 to Box 0.
items_to_move = ['comet', 'thread', 'earring']
for item in items_to_move:
    boxes[7].remove(item)
    boxes[0].append(item)

# Put the scissors and the thunder into Box 0.
items_to_add = ['scissors', 'thunder']
for item in items_to_add:
    boxes[0].append(item)

# Remove the storm from Box 6.
boxes[6].remove('storm')

# Swap the basket in Box 10 with the snow in Box 0.
boxes[10], boxes[0] = boxes[0], boxes[10]

# Put the dice into Box 9.
boxes[9].append('dice')

# Move the thunder from Box 0 to Box 5.
boxes[0].remove('thunder')
boxes[5].append('thunder')

# Move the elephant from Box 3 to Box 10.
boxes[3].remove('elephant')
boxes[10].append('elephant')

# Remove the lipstick from Box 3.
boxes[3].remove('lipstick')

# Move the jungle and the dice and the pot from Box 1 to Box 6.
items_to_move = ['jungle', 'dice', 'pot']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[6].append(item)

# Swap the lamp in Box 8 with the elephant in Box 10.
boxes[8], boxes[10] = boxes[10], boxes[8]

# Swap the shelf in Box 11 with the swimsuit in Box 1.
boxes[11], boxes[1] = boxes[1], boxes[11]

# Move the swimsuit from Box 11 to Box 10.
boxes[11].remove('swimsuit')
boxes[10].append('swimsuit')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")