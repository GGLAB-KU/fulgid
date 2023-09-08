# Initial state of boxes
boxes = {
    0: [],
    1: ['mixer'],
    2: ['pot', 'pillow'],
    3: ['skirt', 'spoon', 'cow', 'blender', 'lightning'],
    4: ['microwave'],
    5: [],
    6: [],
    7: ['bear', 'table'],
    8: ['fork'],
    9: ['soap', 'magnet', 'mirror'],
    10: []
}

# Swap the mirror in Box 9 with the table in Box 7.
boxes[9].remove('mirror')
boxes[7].remove('table')
boxes[9].append('table')
boxes[7].append('mirror')

# Move the skirt and the blender from Box 3 to Box 8.
items_to_move = ['skirt', 'blender']
for item in items_to_move:
    boxes[3].remove(item)
    boxes[8].append(item)

# Swap the table in Box 9 with the pillow in Box 2.
boxes[9].remove('table')
boxes[2].remove('pillow')
boxes[9].append('pillow')
boxes[2].append('table')

# Move the soap and the pillow and the magnet from Box 9 to Box 4.
items_to_move = ['soap', 'pillow', 'magnet']
for item in items_to_move:
    boxes[9].remove(item)
    boxes[4].append(item)

# Empty Box 4.
boxes[4] = []

# Remove the table and the pot from Box 2.
items_to_remove = ['table', 'pot']
for item in items_to_remove:
    boxes[2].remove(item)

# Put the butterfly and the tiger into Box 4.
items_to_put = ['butterfly', 'tiger']
for item in items_to_put:
    boxes[4].append(item)

# Remove the bear and the mirror from Box 7.
items_to_remove = ['bear', 'mirror']
for item in items_to_remove:
    boxes[7].remove(item)

# Swap the blender in Box 8 with the tiger in Box 4.
boxes[8].remove('blender')
boxes[4].remove('tiger')
boxes[8].append('tiger')
boxes[4].append('blender')

# Move the mixer from Box 1 to Box 3.
boxes[1].remove('mixer')
boxes[3].append('mixer')

# Replace the butterfly with the bracelet in Box 4.
boxes[4].remove('butterfly')
boxes[4].append('bracelet')

# Put the helmet and the submarine and the boat into Box 7.
items_to_put = ['helmet', 'submarine', 'boat']
for item in items_to_put:
    boxes[7].append(item)

# Remove the bracelet and the blender from Box 4.
items_to_remove = ['bracelet', 'blender']
for item in items_to_remove:
    boxes[4].remove(item)

# Put the toothbrush and the planet and the usb into Box 9.
items_to_put = ['toothbrush', 'planet', 'usb']
for item in items_to_put:
    boxes[9].append(item)

# Move the planet and the toothbrush from Box 9 to Box 1.
items_to_move = ['planet', 'toothbrush']
for item in items_to_move:
    boxes[9].remove(item)
    boxes[1].append(item)

# Empty Box 9.
boxes[9] = []

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")