# Initial state of boxes
boxes = {
    0: ['jacket', 'comb', 'violin'],
    1: ['pants', 'tiger'],
    2: [],
    3: ['microscope'],
    4: ['umbrella', 'doll']
}

# Empty Box 0
boxes[0] = []

# Move the umbrella and the doll from Box 4 to Box 2
items_to_move = ['umbrella', 'doll']
for item in items_to_move:
    boxes[4].remove(item)
    boxes[2].append(item)

# Move the tiger and the pants from Box 1 to Box 2
items_to_move = ['tiger', 'pants']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[2].append(item)

# Put the frame into Box 4
boxes[4].append('frame')

# Remove the frame from Box 4
boxes[4].remove('frame')

# Swap the microscope in Box 3 with the doll in Box 2
boxes[3], boxes[2] = boxes[2], boxes[3]

# Swap the doll in Box 3 with the tiger in Box 2
boxes[3], boxes[2] = boxes[2], boxes[3]

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")