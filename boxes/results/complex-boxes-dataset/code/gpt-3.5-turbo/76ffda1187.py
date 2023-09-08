# Initial state of boxes
boxes = {
    0: ['grass', 'sandals', 'piano'],
    1: [],
    2: ['fork', 'brush'],
    3: ['shoe', 'scissors'],
    4: ['usb']
}

# Replace the usb with the clock in Box 4.
boxes[4].remove('usb')
boxes[4].append('clock')

# Replace the piano and the sandals and the grass with the jungle and the needle and the dress in Box 0.
boxes[0].remove('piano')
boxes[0].remove('sandals')
boxes[0].remove('grass')
boxes[0].append('jungle')
boxes[0].append('needle')
boxes[0].append('dress')

# Empty Box 2.
boxes[2] = []

# Remove the shoe from Box 3.
boxes[3].remove('shoe')

# Replace the clock with the rain in Box 4.
boxes[4].remove('clock')
boxes[4].append('rain')

# Remove the rain from Box 4.
boxes[4].remove('rain')

# Swap the scissors in Box 3 with the jungle in Box 0.
boxes[3].remove('scissors')
boxes[0].remove('jungle')
boxes[3].append('jungle')
boxes[0].append('scissors')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")