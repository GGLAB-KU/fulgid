# Initial state of boxes
boxes = {
    0: ['swimsuit', 'shoes', 'scarf', 'ring'],
    1: ['earring'],
    2: ['fork', 'grinder', 'note', 'speaker'],
    3: ['meteor', 'umbrella'],
    4: ['sun', 'pen', 'ocean', 'bell'],
    5: ['harmonica']
}

# Empty Box 5
boxes[5] = []

# Swap the ocean in Box 4 with the meteor in Box 3
boxes[4].remove('ocean')
boxes[3].remove('meteor')
boxes[4].append('meteor')
boxes[3].append('ocean')

# Put the chair and the car into Box 5
boxes[5].append('chair')
boxes[5].append('car')

# Swap the chair in Box 5 with the earring in Box 1
boxes[5].remove('chair')
boxes[1].remove('earring')
boxes[5].append('earring')
boxes[1].append('chair')

# Replace the fork with the magnet in Box 2
boxes[2].remove('fork')
boxes[2].append('magnet')

# Move the meteor and the bell and the sun from Box 4 to Box 3
items_to_move = ['meteor', 'bell', 'sun']
for item in items_to_move:
    boxes[4].remove(item)
    boxes[3].append(item)

# Replace the shoes and the swimsuit and the scarf with the game and the spoon and the shampoo in Box 0
items_to_remove = ['shoes', 'swimsuit', 'scarf']
items_to_add = ['game', 'spoon', 'shampoo']
for item in items_to_remove:
    boxes[0].remove(item)
for item in items_to_add:
    boxes[0].append(item)

# Move the speaker and the magnet and the note from Box 2 to Box 1
items_to_move = ['speaker', 'magnet', 'note']
for item in items_to_move:
    boxes[2].remove(item)
    boxes[1].append(item)

# Replace the pen with the truck in Box 4
boxes[4].remove('pen')
boxes[4].append('truck')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")