# Initial state of boxes
boxes = {
    0: ['makeup'],
    1: ['violin', 'sun'],
    2: ['ship', 'piano', 'shark', 'skirt'],
    3: ['octopus', 'hat', 'towel', 'cup', 'dolphin']
}

# Remove the octopus from Box 3.
boxes[3].remove('octopus')

# Move the makeup from Box 0 to Box 2.
boxes[0].remove('makeup')
boxes[2].append('makeup')

# Move the sun from Box 1 to Box 2.
boxes[1].remove('sun')
boxes[2].append('sun')

# Empty Box 2.
boxes[2] = []

# Empty Box 3.
boxes[3] = []

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")