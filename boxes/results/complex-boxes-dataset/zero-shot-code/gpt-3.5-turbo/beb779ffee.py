boxes = [[], [], [], [], []]

# Box 0 contains the jacket and the comb and the violin
boxes[0] = ['jacket', 'comb', 'violin']

# Empty Box 0
boxes[0] = []

# Move the umbrella and the doll from Box 4 to Box 2
boxes[2].extend(['umbrella', 'doll'])
boxes[4] = []

# Move the tiger and the pants from Box 1 to Box 2
boxes[2].extend(['tiger', 'pants'])
boxes[1] = []

# Put the frame into Box 4
boxes[4] = ['frame']

# Remove the frame from Box 4
boxes[4] = []

# Swap the microscope in Box 3 with the doll in Box 2
boxes[3], boxes[2] = boxes[2], boxes[3]

# Swap the doll in Box 3 with the tiger in Box 2
boxes[3], boxes[2] = boxes[2], boxes[3]

# Print the contents of each box
for i, box in enumerate(boxes):
    print(f"Box {i}: {box}")