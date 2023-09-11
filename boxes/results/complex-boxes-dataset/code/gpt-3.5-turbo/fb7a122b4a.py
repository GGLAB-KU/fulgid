# Initial state of boxes
boxes = {
    0: ['scissors', 'shark'],
    1: ['wire'],
    2: [],
    3: [],
    4: ['train'],
    5: ['gloves', 'shelf', 'tree', 'paint'],
    6: ['oven']
}

# Swap the oven in Box 6 with the train in Box 4.
boxes[4].remove('train')
boxes[6].remove('oven')
boxes[4].append('oven')
boxes[6].append('train')

# Swap the wire in Box 1 with the shark in Box 0.
boxes[0].remove('shark')
boxes[1].remove('wire')
boxes[0].append('wire')
boxes[1].append('shark')

# Put the shoes and the tree and the camera into Box 1.
items_to_add = ['shoes', 'tree', 'camera']
for item in items_to_add:
    boxes[1].append(item)

# Empty Box 6.
boxes[6] = []

# Put the mountain into Box 0.
boxes[0].append('mountain')

# Swap the paint in Box 5 with the oven in Box 4.
boxes[4].remove('oven')
boxes[5].remove('paint')
boxes[4].append('paint')
boxes[5].append('oven')

# Remove the oven and the shelf from Box 5.
boxes[5].remove('oven')
boxes[5].remove('shelf')

# Replace the mountain and the wire with the pillow and the ocean in Box 0.
boxes[0].remove('mountain')
boxes[0].remove('wire')
boxes[0].append('pillow')
boxes[0].append('ocean')

# Remove the tree and the gloves from Box 5.
boxes[5].remove('tree')
boxes[5].remove('gloves')

# Remove the paint from Box 4.
boxes[4].remove('paint')

# Empty Box 0.
boxes[0] = []

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")