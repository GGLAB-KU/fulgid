# Initial state of boxes
boxes = {
    0: [],
    1: ['mixer', 'coin'],
    2: ['grinder', 'game'],
    3: ['thunder', 'lion'],
    4: ['polish'],
    5: ['shoe', 'pants', 'blender', 'clock', 'bell'],
    6: ['dolphin', 'rain', 'fridge', 'piano', 'toothpaste'],
    7: ['dog', 'mirror', 'spoon', 'sandals', 'bear'],
    8: [],
    9: ['microwave']
}

# Put the toaster and the butterfly into Box 5.
boxes[5].append('toaster')
boxes[5].append('butterfly')

# Put the car into Box 4.
boxes[4].append('car')

# Move the clock and the butterfly and the bell from Box 5 to Box 6.
items_to_move = ['clock', 'butterfly', 'bell']
for item in items_to_move:
    boxes[5].remove(item)
    boxes[6].append(item)

# Move the fridge from Box 6 to Box 8.
boxes[6].remove('fridge')
boxes[8].append('fridge')

# Empty Box 2.
boxes[2] = []

# Replace the polish with the drum in Box 4.
boxes[4].remove('polish')
boxes[4].append('drum')

# Remove the toaster and the shoe from Box 5.
boxes[5].remove('toaster')
boxes[5].remove('shoe')

# Replace the microwave with the shampoo in Box 9.
boxes[9].remove('microwave')
boxes[9].append('shampoo')

# Put the shoe and the pen and the submarine into Box 8.
boxes[8].append('shoe')
boxes[8].append('pen')
boxes[8].append('submarine')

# Replace the car with the hat in Box 4.
boxes[4].remove('car')
boxes[4].append('hat')

# Replace the hat and the drum with the moon and the beach in Box 4.
boxes[4].remove('hat')
boxes[4].remove('drum')
boxes[4].append('moon')
boxes[4].append('beach')

# Replace the bear with the puzzle in Box 7.
boxes[7].remove('bear')
boxes[7].append('puzzle')

# Move the lion from Box 3 to Box 8.
boxes[3].remove('lion')
boxes[8].append('lion')

# Move the lion from Box 8 to Box 5.
boxes[8].remove('lion')
boxes[5].append('lion')

# Remove the shampoo from Box 9.
boxes[9].remove('shampoo')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")