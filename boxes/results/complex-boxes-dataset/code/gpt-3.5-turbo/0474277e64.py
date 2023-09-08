# Initial state of boxes
boxes = {
    0: ['motorcycle'],
    1: ['blender', 'rocket', 'thread', 'battery', 'zipper'],
    2: ['brush'],
    3: ['thunder', 'needle', 'earring', 'scarf', 'dice'],
    4: ['gloves', 'forest', 'beach', 'train']
}

# Empty Box 2
boxes[2] = []

# Remove the train and the gloves and the beach from Box 4
items_to_remove = ['train', 'gloves', 'beach']
for item in items_to_remove:
    boxes[4].remove(item)

# Empty Box 0
boxes[0] = []

# Put the bag into Box 3
boxes[3].append('bag')

# Swap the dice in Box 3 with the rocket in Box 1
boxes[3].remove('dice')
boxes[1].remove('rocket')
boxes[3].append('rocket')
boxes[1].append('dice')

# Remove the forest from Box 4
boxes[4].remove('forest')

# Remove the earring from Box 3
boxes[3].remove('earring')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")