# Initial state of boxes
boxes = {
    0: ['star', 'toothbrush', 'pot', 'razor'],
    1: [],
    2: ['makeup', 'glove', 'sun', 'horn'],
    3: ['magnet', 'car', 'mirror', 'pen', 'cow'],
    4: ['shark', 'zipper', 'mask', 'chair'],
    5: ['laptop', 'shoe', 'starfish', 'oven'],
    6: ['wire'],
    7: [],
    8: ['leaf', 'piano'],
    9: ['seaweed']
}

# Replace the pot with the frame in Box 0.
boxes[0].remove('pot')
boxes[0].append('frame')

# Swap the seaweed in Box 9 with the oven in Box 5.
boxes[9], boxes[5] = boxes[5], boxes[9]

# Move the piano from Box 8 to Box 3.
boxes[8].remove('piano')
boxes[3].append('piano')

# Replace the oven with the toaster in Box 9.
boxes[9].remove('oven')
boxes[9].append('toaster')

# Put the tree and the pan into Box 2.
boxes[2].append('tree')
boxes[2].append('pan')

# Replace the wire with the game in Box 6.
boxes[6].remove('wire')
boxes[6].append('game')

# Remove the sun and the horn and the pan from Box 2.
items_to_remove = ['sun', 'horn', 'pan']
for item in items_to_remove:
    boxes[2].remove(item)

# Replace the game with the swimsuit in Box 6.
boxes[6].remove('game')
boxes[6].append('swimsuit')

# Move the cow and the mirror and the pen from Box 3 to Box 4.
items_to_move = ['cow', 'mirror', 'pen']
for item in items_to_move:
    boxes[3].remove(item)
    boxes[4].append(item)

# Empty Box 8.
boxes[8] = []

# Put the oven and the meteor into Box 2.
boxes[2].append('oven')
boxes[2].append('meteor')

# Replace the car with the fork in Box 3.
boxes[3].remove('car')
boxes[3].append('fork')

# Move the piano and the magnet from Box 3 to Box 7.
items_to_move = ['piano', 'magnet']
for item in items_to_move:
    boxes[3].remove(item)
    boxes[7].append(item)

# Put the doll and the tiger and the planet into Box 1.
boxes[1].append('doll')
boxes[1].append('tiger')
boxes[1].append('planet')

# Swap the fork in Box 3 with the swimsuit in Box 6.
boxes[3], boxes[6] = boxes[6], boxes[3]

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")