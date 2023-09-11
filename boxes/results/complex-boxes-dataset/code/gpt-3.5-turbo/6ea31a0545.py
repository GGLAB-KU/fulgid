# Initial state of boxes
boxes = {
    0: ['boat', 'laptop', 'bag', 'key'],
    1: ['comb'],
    2: ['cow', 'toy', 'rock', 'comet', 'bell'],
    3: ['mountain', 'controller', 'console', 'tie', 'glasses'],
    4: ['seaweed', 'flute', 'telescope', 'magnet'],
    5: ['towel', 'dress', 'note'],
    6: ['scarf', 'sandals', 'belt'],
    7: ['crown', 'guitar', 'bowl', 'dolphin'],
    8: ['chair'],
    9: [],
    10: ['table'],
    11: [],
    12: ['book', 'shoe', 'skirt']
}

# Remove the telescope and the magnet and the flute from Box 4.
items_to_remove = ['telescope', 'magnet', 'flute']
for item in items_to_remove:
    boxes[4].remove(item)

# Put the cow and the paint into Box 1.
boxes[1].append('cow')
boxes[1].append('paint')

# Put the mixer and the swimsuit into Box 2.
boxes[2].append('mixer')
boxes[2].append('swimsuit')

# Swap the chair in Box 8 with the console in Box 3.
boxes[8], boxes[3][2] = boxes[3][2], boxes[8]

# Replace the mountain and the tie with the note and the shelf in Box 3.
boxes[3].remove('mountain')
boxes[3].remove('tie')
boxes[3].append('note')
boxes[3].append('shelf')

# Remove the belt and the sandals from Box 6.
boxes[6].remove('belt')
boxes[6].remove('sandals')

# Replace the table with the shoes in Box 10.
boxes[10].remove('table')
boxes[10].append('shoes')

# Put the makeup into Box 12.
boxes[12].append('makeup')

# Move the note and the dress from Box 5 to Box 0.
items_to_move = ['note', 'dress']
for item in items_to_move:
    boxes[5].remove(item)
    boxes[0].append(item)

# Put the cloud into Box 11.
boxes[11].append('cloud')

# Swap the cloud in Box 11 with the dress in Box 0.
boxes[11], boxes[0][1] = boxes[0][1], boxes[11]

# Put the bowl into Box 10.
boxes[10].append('bowl')

# Move the seaweed from Box 4 to Box 2.
boxes[4].remove('seaweed')
boxes[2].append('seaweed')

# Swap the shoes in Box 10 with the guitar in Box 7.
boxes[10], boxes[7][1] = boxes[7][1], boxes[10]

# Put the ship into Box 8.
boxes[8].append('ship')

# Move the mixer and the swimsuit and the rock from Box 2 to Box 0.
items_to_move = ['mixer', 'swimsuit', 'rock']
for item in items_to_move:
    boxes[2].remove(item)
    boxes[0].append(item)

# Replace the comb with the star in Box 1.
boxes[1].remove('comb')
boxes[1].append('star')

# Put the controller and the bus and the card into Box 6.
boxes[6].append('controller')
boxes[6].append('bus')
boxes[6].append('card')

# Move the cow and the paint from Box 1 to Box 11.
boxes[1].remove('cow')
boxes[1].remove('paint')
boxes[11].append('cow')
boxes[11].append('paint')

# Put the ocean and the scissors and the swimsuit into Box 6.
boxes[6].append('ocean')
boxes[6].append('scissors')
boxes[6].append('swimsuit')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")