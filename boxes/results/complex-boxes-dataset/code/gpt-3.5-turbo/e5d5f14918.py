# Initial state of boxes
boxes = {
    0: ['lamp'],
    1: ['cup', 'freezer'],
    2: ['starfish', 'candle', 'horn', 'ring', 'coin'],
    3: ['battery', 'tie', 'coral', 'pillow'],
    4: ['lock', 'crown', 'submarine'],
    5: ['comet'],
    6: ['truck', 'branch', 'mask'],
    7: ['magnet', 'shoes', 'flower'],
    8: ['towel', 'car', 'pen']
}

# Replace the coral and the tie and the pillow with the cow and the horn and the glove in Box 3.
boxes[3].remove('coral')
boxes[3].remove('tie')
boxes[3].remove('pillow')
boxes[3].append('cow')
boxes[3].append('horn')
boxes[3].append('glove')

# Move the branch from Box 6 to Box 4.
boxes[6].remove('branch')
boxes[4].append('branch')

# Replace the mask and the truck with the watch and the microscope in Box 6.
boxes[6].remove('mask')
boxes[6].remove('truck')
boxes[6].append('watch')
boxes[6].append('microscope')

# Put the tree and the dolphin into Box 4.
boxes[4].append('tree')
boxes[4].append('dolphin')

# Move the towel and the car and the pen from Box 8 to Box 3.
items_to_move = ['towel', 'car', 'pen']
for item in items_to_move:
    boxes[8].remove(item)
    boxes[3].append(item)

# Empty Box 6.
boxes[6] = []

# Swap the comet in Box 5 with the cup in Box 1.
boxes[5], boxes[1] = boxes[1], boxes[5]

# Remove the crown and the dolphin and the submarine from Box 4.
items_to_remove = ['crown', 'dolphin', 'submarine']
for item in items_to_remove:
    boxes[4].remove(item)

# Swap the candle in Box 2 with the lock in Box 4.
boxes[2], boxes[4] = boxes[4], boxes[2]

# Move the cup from Box 5 to Box 8.
boxes[5].remove('cup')
boxes[8].append('cup')

# Put the bicycle into Box 3.
boxes[3].append('bicycle')

# Replace the car and the cow and the bicycle with the wire and the oven and the shoe in Box 3.
boxes[3].remove('car')
boxes[3].remove('cow')
boxes[3].remove('bicycle')
boxes[3].append('wire')
boxes[3].append('oven')
boxes[3].append('shoe')

# Put the controller into Box 8.
boxes[8].append('controller')

# Put the mixer and the boot and the cup into Box 6.
boxes[6].append('mixer')
boxes[6].append('boot')
boxes[6].append('cup')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")