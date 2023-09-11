# Initial state of boxes
boxes = {
    0: ['bell', 'drum', 'blender', 'thread', 'brush'],
    1: [],
    2: [],
    3: ['ship', 'charger', 'fridge']
}

# Replace the fridge with the coat in Box 3.
boxes[3].remove('fridge')
boxes[3].append('coat')

# Move the brush and the drum and the bell from Box 0 to Box 3.
items_to_move = ['brush', 'drum', 'bell']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[3].append(item)

# Move the blender and the thread from Box 0 to Box 3.
items_to_move = ['blender', 'thread']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[3].append(item)

# Move the blender from Box 3 to Box 0.
boxes[3].remove('blender')
boxes[0].append('blender')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")