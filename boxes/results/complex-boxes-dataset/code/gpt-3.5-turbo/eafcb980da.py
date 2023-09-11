# Initial state of boxes
boxes = {
    0: ['horn', 'branch', 'needle', 'basket'],
    1: ['wire', 'coat', 'starfish'],
    2: ['pot', 'usb', 'planet', 'thunder', 'spoon'],
    3: ['swimsuit', 'earring', 'console']
}

# Remove the wire and the starfish from Box 1.
boxes[1].remove('wire')
boxes[1].remove('starfish')

# Remove the coat from Box 1.
boxes[1].remove('coat')

# Replace the swimsuit and the console with the coral and the blanket in Box 3.
boxes[3].remove('swimsuit')
boxes[3].remove('console')
boxes[3].append('coral')
boxes[3].append('blanket')

# Remove the coral and the blanket from Box 3.
boxes[3].remove('coral')
boxes[3].remove('blanket')

# Replace the horn and the branch with the keyboard and the seaweed in Box 0.
boxes[0].remove('horn')
boxes[0].remove('branch')
boxes[0].append('keyboard')
boxes[0].append('seaweed')

# Move the seaweed from Box 0 to Box 2.
boxes[0].remove('seaweed')
boxes[2].append('seaweed')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")