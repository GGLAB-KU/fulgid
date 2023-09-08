# Initial state of boxes
boxes = {
    0: ['forest', 'skirt'],
    1: ['cow', 'pen', 'cloud', 'scarf', 'pillow'],
    2: ['pants', 'needle', 'toaster', 'grass', 'pot'],
    3: ['shirt', 'scissors', 'comet', 'sock', 'basket'],
    4: ['train', 'motorcycle', 'planet', 'keyboard', 'shelf'],
    5: ['controller', 'lightning', 'meteor', 'butterfly', 'lipstick']
}

# Remove the pen from Box 1.
boxes[1].remove('pen')

# Move the sock from Box 3 to Box 2.
boxes[2].append(boxes[3].pop(boxes[3].index('sock')))

# Empty Box 4.
boxes[4] = []

# Move the comet and the basket and the shirt from Box 3 to Box 5.
items_to_move = ['comet', 'basket', 'shirt']
for item in items_to_move:
    boxes[5].append(boxes[3].pop(boxes[3].index(item)))

# Swap the skirt in Box 0 with the pants in Box 2.
boxes[0], boxes[2] = boxes[2], boxes[0]

# Move the forest and the pants from Box 0 to Box 3.
items_to_move = ['forest', 'pants']
for item in items_to_move:
    boxes[3].append(boxes[0].pop(boxes[0].index(item)))

# Swap the cow in Box 1 with the basket in Box 5.
boxes[1], boxes[5] = boxes[5], boxes[1]

# Swap the scarf in Box 1 with the forest in Box 3.
boxes[1], boxes[3] = boxes[3], boxes[1]

# Remove the scissors and the pants and the scarf from Box 3.
items_to_remove = ['scissors', 'pants', 'scarf']
for item in items_to_remove:
    boxes[3].remove(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")