# Initial state of boxes
boxes = {
    0: ['book', 'mask', 'tree', 'submarine'],
    1: ['beach', 'needle', 'coral'],
    2: ['bird', 'branch'],
    3: ['soap', 'controller', 'tiger']
}

# Remove the controller and the tiger and the soap from Box 3.
boxes[3].remove('controller')
boxes[3].remove('tiger')
boxes[3].remove('soap')

# Replace the needle and the coral and the beach with the horn and the frame and the pillow in Box 1.
boxes[1].remove('needle')
boxes[1].remove('coral')
boxes[1].remove('beach')
boxes[1].append('horn')
boxes[1].append('frame')
boxes[1].append('pillow')

# Remove the horn and the frame and the pillow from Box 1.
boxes[1].remove('horn')
boxes[1].remove('frame')
boxes[1].remove('pillow')

# Put the guitar into Box 3.
boxes[3].append('guitar')

# Move the branch and the bird from Box 2 to Box 3.
boxes[2].remove('branch')
boxes[2].remove('bird')
boxes[3].append('branch')
boxes[3].append('bird')

# Put the sculpture and the jacket and the fork into Box 0.
items_to_move = ['sculpture', 'jacket', 'fork']
for item in items_to_move:
    boxes[0].append(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")