# Initial state of boxes
boxes = {
    0: ['microscope', 'toothpaste', 'shorts'],
    1: [],
    2: ['clock', 'fridge', 'mask', 'telescope'],
    3: [],
    4: ['puzzle', 'flute']
}

# Replace the telescope with the vase in Box 2.
boxes[2].remove('telescope')
boxes[2].append('vase')

# Swap the flute in Box 4 with the mask in Box 2.
boxes[4].remove('flute')
boxes[2].remove('mask')
boxes[4].append('mask')
boxes[2].append('flute')

# Swap the flute in Box 2 with the puzzle in Box 4.
boxes[2].remove('flute')
boxes[4].remove('puzzle')
boxes[2].append('puzzle')
boxes[4].append('flute')

# Swap the mask in Box 4 with the microscope in Box 0.
boxes[4].remove('mask')
boxes[0].remove('microscope')
boxes[4].append('microscope')
boxes[0].append('mask')

# Replace the clock and the vase with the beach and the usb in Box 2.
boxes[2].remove('clock')
boxes[2].remove('vase')
boxes[2].append('beach')
boxes[2].append('usb')

# Put the swimsuit and the coat and the horn into Box 2.
items_to_put = ['swimsuit', 'coat', 'horn']
for item in items_to_put:
    boxes[2].append(item)

# Put the glasses into Box 3.
boxes[3].append('glasses')

# Swap the microscope in Box 4 with the mask in Box 0.
boxes[4].remove('microscope')
boxes[0].remove('mask')
boxes[4].append('mask')
boxes[0].append('microscope')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")