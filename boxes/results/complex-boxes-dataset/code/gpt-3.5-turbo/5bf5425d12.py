# Initial state of boxes
boxes = {
    0: ['violin', 'wig'],
    1: [],
    2: ['zipper', 'shorts', 'battery'],
    3: ['umbrella', 'watch'],
    4: ['shark', 'tape', 'clock'],
    5: ['fork', 'horn', 'microwave', 'oven', 'camera'],
    6: ['brush'],
    7: ['branch', 'pot', 'beach', 'polish'],
    8: ['seaweed'],
    9: [],
    10: []
}

# Move the shorts and the zipper and the battery from Box 2 to Box 9.
items_to_move = ['shorts', 'zipper', 'battery']
for item in items_to_move:
    boxes[2].remove(item)
    boxes[9].append(item)

# Remove the shorts and the battery and the zipper from Box 9.
items_to_remove = ['shorts', 'battery', 'zipper']
for item in items_to_remove:
    boxes[9].remove(item)

# Replace the oven and the fork and the camera with the lamp and the umbrella and the branch in Box 5.
items_to_remove = ['oven', 'fork', 'camera']
items_to_add = ['lamp', 'umbrella', 'branch']
for item in items_to_remove:
    boxes[5].remove(item)
for item in items_to_add:
    boxes[5].append(item)

# Swap the lamp in Box 5 with the wig in Box 0.
boxes[0].remove('wig')
boxes[5].remove('lamp')
boxes[0].append('lamp')
boxes[5].append('wig')

# Empty Box 5.
boxes[5] = []

# Remove the brush from Box 6.
boxes[6].remove('brush')

# Replace the violin and the lamp with the drum and the dolphin in Box 0.
boxes[0].remove('violin')
boxes[0].remove('lamp')
boxes[0].append('drum')
boxes[0].append('dolphin')

# Move the pot and the branch and the beach from Box 7 to Box 0.
items_to_move = ['pot', 'branch', 'beach']
for item in items_to_move:
    boxes[7].remove(item)
    boxes[0].append(item)

# Move the umbrella from Box 3 to Box 9.
boxes[3].remove('umbrella')
boxes[9].append('umbrella')

# Remove the dolphin and the beach from Box 0.
items_to_remove = ['dolphin', 'beach']
for item in items_to_remove:
    boxes[0].remove(item)

# Swap the umbrella in Box 9 with the branch in Box 0.
boxes[9].remove('umbrella')
boxes[0].remove('branch')
boxes[9].append('branch')
boxes[0].append('umbrella')

# Replace the polish with the spoon in Box 7.
boxes[7].remove('polish')
boxes[7].append('spoon')

# Remove the watch from Box 3.
boxes[3].remove('watch')

# Put the shoes and the button and the console into Box 1.
items_to_move = ['shoes', 'button', 'console']
for item in items_to_move:
    boxes[1].append(item)

# Empty Box 8.
boxes[8] = []

# Put the thread into Box 7.
boxes[7].append('thread')

# Replace the thread and the spoon with the brush and the frame in Box 7.
boxes[7].remove('thread')
boxes[7].remove('spoon')
boxes[7].append('brush')
boxes[7].append('frame')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")