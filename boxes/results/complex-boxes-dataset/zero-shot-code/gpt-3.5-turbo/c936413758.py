boxes = [[], [], [], [], [], []]

# Initial state
boxes[0] = ['dog', 'vase', 'candle', 'shampoo', 'speaker']
boxes[1] = ['dress']
boxes[2] = ['tiger', 'scarf', 'polish']
boxes[3] = ['microwave']
boxes[4] = ['card', 'lock']
boxes[5] = []

# Swap the microwave in Box 3 with the tiger in Box 2
boxes[2].remove('tiger')
boxes[3].remove('microwave')
boxes[2].append('microwave')
boxes[3].append('tiger')

# Remove the shampoo from Box 0
boxes[0].remove('shampoo')

# Empty Box 3
boxes[3] = []

# Move the vase from Box 0 to Box 2
boxes[0].remove('vase')
boxes[2].append('vase')

# Move the dog from Box 0 to Box 4
boxes[0].remove('dog')
boxes[4].append('dog')

# Put the magnet and the headphone into Box 4
boxes[4].extend(['magnet', 'headphone'])

# Swap the dress in Box 1 with the microwave in Box 2
boxes[1].remove('dress')
boxes[2].remove('microwave')
boxes[1].append('microwave')
boxes[2].append('dress')

# Swap the vase in Box 2 with the microwave in Box 1
boxes[2].remove('vase')
boxes[1].remove('microwave')
boxes[2].append('microwave')
boxes[1].append('vase')

# Put the scissors and the scarf into Box 1
boxes[1].extend(['scissors', 'scarf'])

# Print the final state of the boxes
for i, box in enumerate(boxes):
    print(f"Box {i}: {box}")