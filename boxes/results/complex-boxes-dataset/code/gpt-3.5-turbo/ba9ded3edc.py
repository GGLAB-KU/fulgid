# Initial state of boxes
boxes = {
    0: ['leaf', 'table'],
    1: [],
    2: ['rocket', 'blender', 'piano', 'controller'],
    3: ['violin', 'shoe', 'starfish'],
    4: [],
    5: ['train', 'pants'],
    6: [],
    7: ['shelf', 'cloud', 'star']
}

# Put the grass into Box 1.
boxes[1].append('grass')

# Move the cloud and the shelf and the star from Box 7 to Box 5.
items_to_move = ['cloud', 'shelf', 'star']
for item in items_to_move:
    boxes[7].remove(item)
    boxes[5].append(item)

# Replace the leaf with the cup in Box 0.
boxes[0].remove('leaf')
boxes[0].append('cup')

# Remove the blender and the rocket and the controller from Box 2.
items_to_remove = ['blender', 'rocket', 'controller']
for item in items_to_remove:
    boxes[2].remove(item)

# Remove the grass from Box 1.
boxes[1].remove('grass')

# Put the brush into Box 2.
boxes[2].append('brush')

# Replace the piano and the brush with the shoes and the toothbrush in Box 2.
boxes[2].remove('piano')
boxes[2].remove('brush')
boxes[2].append('shoes')
boxes[2].append('toothbrush')

# Swap the cup in Box 0 with the cloud in Box 5.
boxes[0].remove('cup')
boxes[5].remove('cloud')
boxes[0].append('cloud')
boxes[5].append('cup')

# Move the pants from Box 5 to Box 6.
boxes[5].remove('pants')
boxes[6].append('pants')

# Move the table from Box 0 to Box 7.
boxes[0].remove('table')
boxes[7].append('table')

# Remove the toothbrush and the shoes from Box 2.
boxes[2].remove('toothbrush')
boxes[2].remove('shoes')

# Remove the cup and the train from Box 5.
boxes[5].remove('cup')
boxes[5].remove('train')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")