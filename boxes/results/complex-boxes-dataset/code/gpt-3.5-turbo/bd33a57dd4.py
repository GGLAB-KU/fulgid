# Initial state of boxes
boxes = {
    0: ['rock', 'train', 'shoe', 'dolphin'],
    1: ['seaweed'],
    2: ['laptop', 'sandals', 'forest', 'helmet', 'coin'],
    3: ['cup'],
    4: ['speaker', 'hat', 'swimsuit']
}

# Empty Box 0
boxes[0] = []

# Swap the seaweed in Box 1 with the cup in Box 3.
boxes[1], boxes[3] = boxes[3], boxes[1]

# Swap the swimsuit in Box 4 with the cup in Box 1.
boxes[4], boxes[1] = boxes[1], boxes[4]

# Move the hat and the cup from Box 4 to Box 3.
items_to_move = ['hat', 'cup']
for item in items_to_move:
    boxes[4].remove(item)
    boxes[3].append(item)

# Swap the hat in Box 3 with the swimsuit in Box 1.
boxes[3], boxes[1] = boxes[1], boxes[3]

# Remove the cup and the seaweed from Box 3.
items_to_remove = ['cup', 'seaweed']
for item in items_to_remove:
    boxes[3].remove(item)

# Put the keyboard and the cloud and the coat into Box 1.
items_to_add = ['keyboard', 'cloud', 'coat']
for item in items_to_add:
    boxes[1].append(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")