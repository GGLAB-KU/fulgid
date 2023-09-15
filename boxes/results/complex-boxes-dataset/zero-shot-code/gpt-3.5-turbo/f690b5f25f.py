boxes = [[], [], [], [], [], []]

# Box 0
boxes[0] = ['bird', 'shark', 'shirt']

# Box 1
boxes[1] = []

# Box 2
boxes[2] = ['button', 'pan', 'motorcycle']

# Box 3
boxes[3] = ['candle', 'needle', 'earring']

# Box 4
boxes[4] = ['watch', 'dolphin', 'shampoo', 'microscope', 'speaker']

# Box 5
boxes[5] = ['sandals', 'planet', 'thunder']

# Empty Box 5
boxes[5] = []

# Move the button from Box 2 to Box 5
boxes[5].append(boxes[2].pop(0))

# Replace the umbrella with the earring in Box 3
boxes[3][2] = boxes[3][1]
boxes[3][1] = 'earring'

# Replace the card with the needle in Box 3
boxes[3][0] = 'needle'

# Swap the motorcycle in Box 2 with the blender in Box 1
boxes[2][2], boxes[1][1] = boxes[1][1], boxes[2][2]

# Replace the pot with the tree in Box 1
boxes[1][0] = 'tree'

# Empty Box 1
boxes[1] = []

# Remove the button from Box 5
boxes[5].remove('button')

# Print the contents of each box
for i, box in enumerate(boxes):
    print(f"Box {i}: {box}")