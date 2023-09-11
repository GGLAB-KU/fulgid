# Initial state of boxes
boxes = {
    0: [],
    1: ['wig', 'horse', 'violin'],
    2: ['coin', 'scarf', 'toaster', 'piano', 'note'],
    3: ['moon'],
    4: [],
    5: ['forest', 'horn'],
    6: ['game', 'boat']
}

# Put the blender into Box 4.
boxes[4].append('blender')

# Put the apple and the flower and the freezer into Box 5.
items_to_move = ['apple', 'flower', 'freezer']
for item in items_to_move:
    boxes[5].remove(item)
    boxes[4].append(item)

# Empty Box 2.
boxes[2] = []

# Move the apple and the forest and the freezer from Box 5 to Box 2.
items_to_move = ['apple', 'forest', 'freezer']
for item in items_to_move:
    boxes[5].remove(item)
    boxes[2].append(item)

# Remove the blender from Box 4.
boxes[4].remove('blender')

# Move the flower from Box 5 to Box 4.
boxes[5].remove('flower')
boxes[4].append('flower')

# Swap the forest in Box 2 with the boat in Box 6.
boxes[2].remove('forest')
boxes[6].remove('boat')
boxes[2].append('boat')
boxes[6].append('forest')

# Replace the horn with the zipper in Box 5.
boxes[5].remove('horn')
boxes[5].append('zipper')

# Move the horse and the violin from Box 1 to Box 2.
items_to_move = ['horse', 'violin']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[2].append(item)

# Swap the forest in Box 6 with the flower in Box 4.
boxes[6].remove('forest')
boxes[4].remove('flower')
boxes[6].append('flower')
boxes[4].append('forest')

# Move the forest from Box 4 to Box 2.
boxes[4].remove('forest')
boxes[2].append('forest')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")