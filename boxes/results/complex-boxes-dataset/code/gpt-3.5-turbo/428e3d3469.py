# Initial state of boxes
boxes = {
    0: ['moon', 'island'],
    1: ['fork', 'truck', 'belt', 'drum'],
    2: [],
    3: ['grass', 'tiger', 'razor', 'branch'],
    4: ['snow']
}

# Remove the moon from Box 0.
boxes[0].remove('moon')

# Empty Box 1.
boxes[1] = []

# Put the toothbrush and the belt into Box 3.
boxes[3].append('toothbrush')
boxes[3].append('belt')

# Move the island from Box 0 to Box 2.
boxes[0].remove('island')
boxes[2].append('island')

# Remove the snow from Box 4.
boxes[4].remove('snow')

# Put the shelf and the bird and the piano into Box 2.
boxes[2].append('shelf')
boxes[2].append('bird')
boxes[2].append('piano')

# Move the island and the bird from Box 2 to Box 3.
boxes[2].remove('island')
boxes[2].remove('bird')
boxes[3].append('island')
boxes[3].append('bird')

# Move the bird and the belt and the tiger from Box 3 to Box 0.
items_to_move = ['bird', 'belt', 'tiger']
for item in items_to_move:
    boxes[3].remove(item)
    boxes[0].append(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")