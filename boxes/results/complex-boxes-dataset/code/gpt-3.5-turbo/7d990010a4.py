# Initial state of boxes
boxes = {
    0: ['glasses'],
    1: ['horse'],
    2: ['star', 'branch'],
    3: ['bus', 'battery', 'game', 'brush', 'helmet']
}

# Put the storm and the card and the boat into Box 1.
boxes[1].append('storm')
boxes[1].append('card')
boxes[1].append('boat')

# Move the bus and the helmet from Box 3 to Box 0.
boxes[0].append(boxes[3].pop(0))
boxes[0].append(boxes[3].pop(2))

# Remove the bus from Box 0.
boxes[0].remove('bus')

# Remove the branch and the star from Box 2.
boxes[2].remove('branch')
boxes[2].remove('star')

# Put the bus into Box 1.
boxes[1].append('bus')

# Replace the battery and the brush with the swimsuit and the cow in Box 3.
boxes[3].remove('battery')
boxes[3].remove('brush')
boxes[3].append('swimsuit')
boxes[3].append('cow')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")