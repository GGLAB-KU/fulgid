# Initial state of boxes
boxes = {
    0: [],
    1: ['book', 'desert', 'key', 'grinder', 'storm'],
    2: ['mixer', 'bell', 'brush', 'comb', 'violin'],
    3: ['microscope']
}

# Move the microscope from Box 3 to Box 2.
boxes[3].remove('microscope')
boxes[2].append('microscope')

# Replace the bell and the violin with the starfish and the drum in Box 2.
boxes[2].remove('bell')
boxes[2].remove('violin')
boxes[2].append('starfish')
boxes[2].append('drum')

# Replace the desert and the grinder with the razor and the mountain in Box 1.
boxes[1].remove('desert')
boxes[1].remove('grinder')
boxes[1].append('razor')
boxes[1].append('mountain')

# Remove the storm from Box 1.
boxes[1].remove('storm')

# Remove the mountain and the key from Box 1.
boxes[1].remove('mountain')
boxes[1].remove('key')

# Replace the razor with the ship in Box 1.
boxes[1].remove('razor')
boxes[1].append('ship')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")