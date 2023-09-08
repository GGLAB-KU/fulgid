# Initial state of boxes
boxes = {
    0: ['bowl'],
    1: ['jacket', 'telescope'],
    2: ['octopus', 'card', 'forest'],
    3: ['table', 'fridge'],
    4: ['thunder'],
    5: ['shelf'],
    6: ['beach', 'hat']
}

# Replace the shelf with the branch in Box 5.
boxes[5].remove('shelf')
boxes[5].append('branch')

# Remove the branch from Box 5.
boxes[5].remove('branch')

# Put the island into Box 1.
boxes[1].append('island')

# Put the toothbrush and the tree and the umbrella into Box 1.
items_to_add = ['toothbrush', 'tree', 'umbrella']
for item in items_to_add:
    boxes[1].append(item)

# Empty Box 0.
boxes[0] = []

# Swap the octopus in Box 2 with the fridge in Box 3.
boxes[2].remove('octopus')
boxes[3].remove('fridge')
boxes[2].append('fridge')
boxes[3].append('octopus')

# Remove the table and the octopus from Box 3.
boxes[3].remove('table')
boxes[3].remove('octopus')

# Move the hat from Box 6 to Box 1.
boxes[6].remove('hat')
boxes[1].append('hat')

# Swap the beach in Box 6 with the thunder in Box 4.
boxes[6].remove('beach')
boxes[4].remove('thunder')
boxes[6].append('thunder')
boxes[4].append('beach')

# Replace the thunder with the beach in Box 6.
boxes[4].remove('beach')
boxes[6].remove('thunder')
boxes[4].append('beach')
boxes[6].append('thunder')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")