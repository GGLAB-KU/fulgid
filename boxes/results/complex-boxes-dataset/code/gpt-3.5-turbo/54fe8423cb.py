# Initial state of boxes
boxes = {
    0: ['lion', 'bicycle'],
    1: ['oven', 'forest', 'dice', 'pants'],
    2: ['vase', 'watch', 'leaf', 'key', 'glasses'],
    3: []
}

# Move the vase and the watch and the glasses from Box 2 to Box 3.
items_to_move = ['vase', 'watch', 'glasses']
for item in items_to_move:
    boxes[2].remove(item)
    boxes[3].append(item)

# Swap the lion in Box 0 with the forest in Box 1.
boxes[0], boxes[1] = boxes[1], boxes[0]

# Remove the dice and the oven from Box 1.
items_to_remove = ['dice', 'oven']
for item in items_to_remove:
    boxes[1].remove(item)

# Move the pants and the lion from Box 1 to Box 2.
items_to_move = ['pants', 'lion']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[2].append(item)

# Remove the key and the lion from Box 2.
items_to_remove = ['key', 'lion']
for item in items_to_remove:
    boxes[2].remove(item)

# Replace the forest and the bicycle with the rocket and the shelf in Box 0.
boxes[0].remove('lion')
boxes[0].remove('bicycle')
boxes[0].append('rocket')
boxes[0].append('shelf')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")