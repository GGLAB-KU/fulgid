# Initial state of boxes
boxes = {
    0: ['whistle'],
    1: [],
    2: ['polish', 'piano'],
    3: ['bracelet', 'spoon', 'telescope', 'lion']
}

# Move the spoon from Box 3 to Box 0.
boxes[3].remove('spoon')
boxes[0].append('spoon')

# Put the towel and the scissors into Box 3.
boxes[3].append('towel')
boxes[3].append('scissors')

# Put the freezer into Box 3.
boxes[3].append('freezer')

# Empty Box 3.
boxes[3] = []

# Move the polish from Box 2 to Box 1.
boxes[2].remove('polish')
boxes[1].append('polish')

# Replace the whistle and the spoon with the boot and the shoes in Box 0.
boxes[0].remove('whistle')
boxes[0].remove('spoon')
boxes[0].append('boot')
boxes[0].append('shoes')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")