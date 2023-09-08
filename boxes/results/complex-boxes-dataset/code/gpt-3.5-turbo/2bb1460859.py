# Initial state of boxes
boxes = {
    0: [],
    1: ['dog', 'piano', 'belt', 'toaster', 'violin'],
    2: ['branch', 'pillow', 'card', 'tiger', 'glasses'],
    3: ['rock'],
    4: [],
    5: ['harmonica', 'blanket', 'scissors', 'forest', 'shark'],
    6: ['octopus', 'sock'],
    7: ['toy']
}

# Remove the forest and the shark from Box 5.
boxes[5].remove('forest')
boxes[5].remove('shark')

# Move the toy from Box 7 to Box 0.
boxes[7].remove('toy')
boxes[0].append('toy')

# Swap the toy in Box 0 with the octopus in Box 6.
boxes[0].remove('toy')
boxes[6].remove('octopus')
boxes[0].append('octopus')
boxes[6].append('toy')

# Remove the octopus from Box 0.
boxes[0].remove('octopus')

# Remove the violin and the piano from Box 1.
boxes[1].remove('violin')
boxes[1].remove('piano')

# Put the perfume into Box 2.
boxes[2].append('perfume')

# Replace the rock with the octopus in Box 3.
boxes[3].remove('rock')
boxes[3].append('octopus')

# Empty Box 3.
boxes[3] = []

# Put the scissors and the umbrella into Box 0.
boxes[0].append('scissors')
boxes[0].append('umbrella')

# Swap the toaster in Box 1 with the toy in Box 6.
boxes[1].remove('toaster')
boxes[6].remove('toy')
boxes[1].append('toy')
boxes[6].append('toaster')

# Remove the belt from Box 1.
boxes[1].remove('belt')

# Empty Box 0.
boxes[0] = []

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")