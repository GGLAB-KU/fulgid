# Initial state of boxes
boxes = {
    0: [],
    1: [],
    2: ['bird', 'toothbrush', 'car', 'seaweed', 'rain'],
    3: ['shampoo', 'puzzle', 'train', 'plane', 'freezer'],
    4: ['piano', 'toothpaste', 'storm'],
    5: ['cloud'],
    6: [],
    7: ['sculpture', 'fish', 'grass'],
    8: ['keyboard']
}

# Swap the sculpture in Box 7 with the keyboard in Box 8.
boxes[7].remove('sculpture')
boxes[8].remove('keyboard')
boxes[7].append('keyboard')
boxes[8].append('sculpture')

# Move the keyboard from Box 7 to Box 0.
boxes[7].remove('keyboard')
boxes[0].append('keyboard')

# Empty Box 8.
boxes[8] = []

# Put the puzzle into Box 8.
boxes[8].append('puzzle')

# Remove the keyboard from Box 0.
boxes[0].remove('keyboard')

# Move the toothbrush from Box 2 to Box 3.
boxes[2].remove('toothbrush')
boxes[3].append('toothbrush')

# Remove the puzzle from Box 8.
boxes[8].remove('puzzle')

# Move the cloud from Box 5 to Box 1.
boxes[5].remove('cloud')
boxes[1].append('cloud')

# Move the cloud from Box 1 to Box 2.
boxes[1].remove('cloud')
boxes[2].append('cloud')

# Put the meteor and the oven into Box 4.
boxes[4].append('meteor')
boxes[4].append('oven')

# Swap the puzzle in Box 3 with the fish in Box 7.
boxes[3].remove('puzzle')
boxes[7].remove('fish')
boxes[3].append('fish')
boxes[7].append('puzzle')

# Replace the storm and the oven and the piano with the shirt and the boat and the pan in Box 4.
boxes[4].remove('storm')
boxes[4].remove('oven')
boxes[4].remove('piano')
boxes[4].append('shirt')
boxes[4].append('boat')
boxes[4].append('pan')

# Remove the puzzle and the grass from Box 7.
boxes[7].remove('puzzle')
boxes[7].remove('grass')

# Swap the bird in Box 2 with the shampoo in Box 3.
boxes[2].remove('bird')
boxes[3].remove('shampoo')
boxes[2].append('shampoo')
boxes[3].append('bird')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")