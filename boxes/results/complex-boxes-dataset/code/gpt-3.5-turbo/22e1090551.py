# Initial state of boxes
boxes = {
    0: ['dolphin', 'ring', 'fridge'],
    1: ['lightning', 'magnet', 'earring', 'beach', 'island'],
    2: ['jungle', 'shelf'],
    3: ['swimsuit', 'doll', 'blanket']
}

# Put the lipstick and the train into Box 3.
boxes[3].append('lipstick')
boxes[3].append('train')

# Replace the jungle with the bell in Box 2.
boxes[2].remove('jungle')
boxes[2].append('bell')

# Put the microscope and the usb into Box 1.
boxes[1].append('microscope')
boxes[1].append('usb')

# Remove the lipstick and the swimsuit from Box 3.
boxes[3].remove('lipstick')
boxes[3].remove('swimsuit')

# Replace the bell with the horn in Box 2.
boxes[2].remove('bell')
boxes[2].append('horn')

# Replace the beach with the dress in Box 1.
boxes[1].remove('beach')
boxes[1].append('dress')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")