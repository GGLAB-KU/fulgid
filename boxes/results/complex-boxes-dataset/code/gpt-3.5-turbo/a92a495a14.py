# Initial state of boxes
boxes = {
    0: [],
    1: ['necklace', 'violin'],
    2: [],
    3: ['fork', 'chair'],
    4: ['belt', 'blender', 'elephant']
}

# Swap the violin in Box 1 with the blender in Box 4.
boxes[1].remove('violin')
boxes[4].remove('blender')
boxes[1].append('blender')
boxes[4].append('violin')

# Move the necklace and the blender from Box 1 to Box 3.
items_to_move = ['necklace', 'blender']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[3].append(item)

# Move the violin and the elephant and the belt from Box 4 to Box 1.
items_to_move = ['violin', 'elephant', 'belt']
for item in items_to_move:
    boxes[4].remove(item)
    boxes[1].append(item)

# Remove the elephant from Box 1.
boxes[1].remove('elephant')

# Replace the violin and the belt with the rocket and the note in Box 1.
boxes[1].remove('violin')
boxes[1].remove('belt')
boxes[1].append('rocket')
boxes[1].append('note')

# Replace the chair and the fork with the island and the coin in Box 3.
boxes[3].remove('chair')
boxes[3].remove('fork')
boxes[3].append('island')
boxes[3].append('coin')

# Empty Box 3.
boxes[3] = []

# Replace the rocket with the makeup in Box 1.
boxes[1].remove('rocket')
boxes[1].append('makeup')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")