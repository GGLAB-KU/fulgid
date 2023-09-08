# Initial state of boxes
boxes = {
    0: [],
    1: ['chair', 'microscope', 'jungle', 'mountain'],
    2: ['rocket', 'perfume', 'puzzle', 'lock'],
    3: ['magnet', 'thunder', 'table'],
    4: [],
    5: [],
    6: ['sandals', 'cat', 'car', 'island'],
    7: ['forest', 'elephant', 'cloud', 'butterfly', 'bicycle'],
    8: ['soap', 'controller'],
    9: [],
    10: []
}

# Replace the jungle with the fork in Box 1.
boxes[1].remove('jungle')
boxes[1].append('fork')

# Replace the cloud with the rock in Box 7.
boxes[7].remove('cloud')
boxes[7].append('rock')

# Empty Box 7.
boxes[7] = []

# Put the pants into Box 2.
boxes[2].append('pants')

# Move the thunder from Box 3 to Box 9.
boxes[9].append(boxes[3].pop(boxes[3].index('thunder')))

# Move the controller from Box 8 to Box 7.
boxes[7].append(boxes[8].pop(boxes[8].index('controller')))

# Replace the controller with the thread in Box 7.
boxes[7].remove('controller')
boxes[7].append('thread')

# Remove the puzzle from Box 2.
boxes[2].remove('puzzle')

# Put the shark and the controller and the drum into Box 2.
boxes[2].extend(['shark', 'controller', 'drum'])

# Remove the fork from Box 1.
boxes[1].remove('fork')

# Remove the thunder from Box 9.
boxes[9].remove('thunder')

# Move the table from Box 3 to Box 2.
boxes[2].append(boxes[3].pop(boxes[3].index('table')))

# Remove the magnet from Box 3.
boxes[3].remove('magnet')

# Remove the thread from Box 7.
boxes[7].remove('thread')

# Swap the mountain in Box 1 with the soap in Box 8.
boxes[1].remove('mountain')
boxes[8].remove('soap')
boxes[1].append('soap')
boxes[8].append('mountain')

# Move the mountain from Box 8 to Box 4.
boxes[4].append(boxes[8].pop(boxes[8].index('mountain')))

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")