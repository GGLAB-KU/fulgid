# Initial state of boxes
boxes = {
    0: ['bear', 'thunder', 'blender', 'earring'],
    1: ['towel', 'console'],
    2: ['car', 'lamp'],
    3: ['truck', 'spoon', 'pan', 'beach', 'comet'],
    4: ['laptop', 'plate', 'skirt'],
    5: [],
    6: ['microscope', 'oven']
}

# Remove the comet and the beach and the spoon from Box 3.
items_to_remove = ['comet', 'beach', 'spoon']
for item in items_to_remove:
    boxes[3].remove(item)

# Put the keyboard into Box 0.
boxes[0].append('keyboard')

# Move the console and the towel from Box 1 to Box 3.
items_to_move = ['console', 'towel']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[3].append(item)

# Move the oven and the microscope from Box 6 to Box 2.
items_to_move = ['oven', 'microscope']
for item in items_to_move:
    boxes[6].remove(item)
    boxes[2].append(item)

# Put the wig and the grinder and the bowl into Box 4.
items_to_put = ['wig', 'grinder', 'bowl']
for item in items_to_put:
    boxes[4].append(item)

# Swap the lamp in Box 2 with the laptop in Box 4.
boxes[2].remove('lamp')
boxes[4].remove('laptop')
boxes[2].append('laptop')
boxes[4].append('lamp')

# Move the microscope from Box 2 to Box 0.
boxes[2].remove('microscope')
boxes[0].append('microscope')

# Empty Box 4.
boxes[4] = []

# Swap the car in Box 2 with the microscope in Box 0.
boxes[2].remove('car')
boxes[0].remove('microscope')
boxes[2].append('microscope')
boxes[0].append('car')

# Put the bracelet and the blender into Box 3.
items_to_put = ['bracelet', 'blender']
for item in items_to_put:
    boxes[3].append(item)

# Empty Box 3.
boxes[3] = []

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")