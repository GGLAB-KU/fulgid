# Initial state of boxes
boxes = {
    0: ['seaweed', 'bag', 'dog', 'makeup', 'dice'],
    1: ['pan', 'tiger', 'freezer'],
    2: ['bicycle', 'mask', 'plane', 'tie', 'glasses'],
    3: ['rocket', 'headphone', 'drum', 'table', 'thread'],
    4: [],
    5: ['starfish', 'snow']
}

# Move the bicycle from Box 2 to Box 4.
boxes[2].remove('bicycle')
boxes[4].append('bicycle')

# Empty Box 1.
boxes[1] = []

# Remove the table from Box 3.
boxes[3].remove('table')

# Put the blender into Box 4.
boxes[4].append('blender')

# Put the jungle into Box 1.
boxes[1].append('jungle')

# Put the flower into Box 5.
boxes[5].append('flower')

# Swap the jungle in Box 1 with the tie in Box 2.
boxes[1].remove('jungle')
boxes[2].remove('tie')
boxes[1].append('tie')
boxes[2].append('jungle')

# Swap the mask in Box 2 with the drum in Box 3.
boxes[2].remove('mask')
boxes[3].remove('drum')
boxes[2].append('drum')
boxes[3].append('mask')

# Remove the headphone and the thread and the rocket from Box 3.
items_to_remove = ['headphone', 'thread', 'rocket']
for item in items_to_remove:
    boxes[3].remove(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")