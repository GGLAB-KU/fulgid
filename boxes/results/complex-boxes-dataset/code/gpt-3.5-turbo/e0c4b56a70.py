# Initial state of boxes
boxes = {
    0: ['shark', 'lock', 'soap', 'dog'],
    1: ['doll', 'dolphin'],
    2: ['zipper', 'magnet', 'shoes'],
    3: ['razor', 'lamp', 'freezer', 'wallet'],
    4: ['tape', 'car', 'polish']
}

# Put the paint into Box 1.
boxes[1].append('paint')

# Remove the zipper from Box 2.
boxes[2].remove('zipper')

# Move the magnet from Box 2 to Box 3.
boxes[2].remove('magnet')
boxes[3].append('magnet')

# Replace the soap and the shark with the star and the toaster in Box 0.
boxes[0].remove('soap')
boxes[0].remove('shark')
boxes[0].append('star')
boxes[0].append('toaster')

# Replace the car with the rocket in Box 4.
boxes[4].remove('car')
boxes[4].append('rocket')

# Empty Box 0.
boxes[0] = []

# Swap the lamp in Box 3 with the shoes in Box 2.
boxes[3].remove('lamp')
boxes[2].remove('shoes')
boxes[3].append('shoes')
boxes[2].append('lamp')

# Move the rocket from Box 4 to Box 3.
boxes[4].remove('rocket')
boxes[3].append('rocket')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")