# Initial state of boxes
boxes = {
    0: ['keyboard', 'flower'],
    1: ['belt', 'apple', 'battery', 'forest'],
    2: [],
    3: [],
    4: ['earring', 'horn', 'mask', 'note'],
    5: ['harmonica', 'microscope', 'blender'],
    6: ['dice', 'submarine', 'card', 'snow'],
    7: ['mixer', 'laptop']
}

# Move the keyboard from Box 0 to Box 7.
boxes[0].remove('keyboard')
boxes[7].append('keyboard')

# Swap the forest in Box 1 with the flower in Box 0.
boxes[1].remove('forest')
boxes[0].remove('flower')
boxes[1].append('flower')
boxes[0].append('forest')

# Remove the horn and the mask from Box 4.
boxes[4].remove('horn')
boxes[4].remove('mask')

# Remove the blender and the microscope and the harmonica from Box 5.
items_to_remove = ['blender', 'microscope', 'harmonica']
for item in items_to_remove:
    boxes[5].remove(item)

# Replace the apple with the desert in Box 1.
boxes[1].remove('apple')
boxes[1].append('desert')

# Move the snow and the dice and the submarine from Box 6 to Box 2.
items_to_move = ['snow', 'dice', 'submarine']
for item in items_to_move:
    boxes[6].remove(item)
    boxes[2].append(item)

# Remove the earring and the note from Box 4.
boxes[4].remove('earring')
boxes[4].remove('note')

# Remove the card from Box 6.
boxes[6].remove('card')

# Move the snow and the dice and the submarine from Box 2 to Box 5.
for item in items_to_move:
    boxes[2].remove(item)
    boxes[5].append(item)

# Put the ocean and the elephant and the wig into Box 2.
items_to_add = ['ocean', 'elephant', 'wig']
for item in items_to_add:
    boxes[2].append(item)

# Remove the dice and the submarine and the snow from Box 5.
for item in items_to_move:
    boxes[5].remove(item)

# Remove the belt and the desert and the battery from Box 1.
items_to_remove = ['belt', 'desert', 'battery']
for item in items_to_remove:
    boxes[1].remove(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")