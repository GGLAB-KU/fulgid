# Initial state of boxes
boxes = {
    0: ['crown', 'submarine', 'zipper'],
    1: ['makeup', 'scissors', 'belt', 'fish'],
    2: ['umbrella', 'book'],
    3: ['seaweed', 'tiger', 'glasses', 'necklace'],
    4: ['polish', 'jungle'],
    5: ['camera', 'puzzle', 'pen'],
    6: ['leaf', 'clock', 'cloud', 'keyboard']
}

# Remove the clock and the cloud and the leaf from Box 6.
boxes[6].remove('clock')
boxes[6].remove('cloud')
boxes[6].remove('leaf')

# Move the camera and the puzzle and the pen from Box 5 to Box 0.
items_to_move = ['camera', 'puzzle', 'pen']
for item in items_to_move:
    boxes[5].remove(item)
    boxes[0].append(item)

# Swap the pen in Box 0 with the book in Box 2.
boxes[0].remove('pen')
boxes[2].remove('book')
boxes[0].append('book')
boxes[2].append('pen')

# Move the glasses from Box 3 to Box 0.
boxes[3].remove('glasses')
boxes[0].append('glasses')

# Replace the tiger and the seaweed with the camera and the microscope in Box 3.
boxes[3].remove('tiger')
boxes[3].remove('seaweed')
boxes[3].append('camera')
boxes[3].append('microscope')

# Replace the camera and the crown and the zipper with the spoon and the lipstick and the bear in Box 0.
boxes[0].remove('camera')
boxes[0].remove('crown')
boxes[0].remove('zipper')
boxes[0].append('spoon')
boxes[0].append('lipstick')
boxes[0].append('bear')

# Remove the spoon from Box 0.
boxes[0].remove('spoon')

# Put the polish and the doll and the button into Box 4.
items_to_put = ['polish', 'doll', 'button']
for item in items_to_put:
    boxes[4].append(item)

# Empty Box 6.
boxes[6] = []

# Put the shoe and the fork into Box 0.
items_to_put = ['shoe', 'fork']
for item in items_to_put:
    boxes[0].append(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")