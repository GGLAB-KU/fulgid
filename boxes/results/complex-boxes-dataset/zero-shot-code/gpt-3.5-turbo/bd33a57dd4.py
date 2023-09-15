boxes = [[], [], [], [], []]

boxes[0] = []
boxes[1] = ['seaweed']
boxes[3] = ['cup']
boxes[4] = ['swimsuit']

# Swap seaweed in Box 1 with cup in Box 3
boxes[1], boxes[3] = boxes[3], boxes[1]

# Swap swimsuit in Box 4 with cup in Box 1
boxes[1], boxes[4] = boxes[4], boxes[1]

# Move hat and cup from Box 4 to Box 3
boxes[3].extend(boxes[4])
boxes[4] = []

# Swap hat in Box 3 with swimsuit in Box 1
boxes[1], boxes[3] = boxes[3], boxes[1]

# Remove cup and seaweed from Box 3
boxes[3] = []

# Put keyboard, cloud, and coat into Box 1
boxes[1].extend(['keyboard', 'cloud', 'coat'])

# Print the contents of each box
for i, box in enumerate(boxes):
    print(f"Box {i}: {box}")