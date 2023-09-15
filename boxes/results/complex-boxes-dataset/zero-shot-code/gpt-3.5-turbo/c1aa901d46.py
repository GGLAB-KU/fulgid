boxes = [[], [], [], []]

# Replace the oven with the candle in Box 0
boxes[0] = ['candle']

# Swap the fridge in Box 2 with the candle in Box 0
boxes[0], boxes[2] = boxes[2], boxes[0]

# Put the butterfly and the bag into Box 0
boxes[0].extend(['butterfly', 'bag'])

# Replace the candle with the skirt in Box 2
boxes[2] = ['skirt']

# Move the skirt from Box 2 to Box 0
boxes[0].append(boxes[2][0])
boxes[2] = []

# Move the fridge and the skirt from Box 0 to Box 2
boxes[2].extend([boxes[0][0], boxes[0][1]])
boxes[0] = []

# Print the contents of each box
for i, box in enumerate(boxes):
    print(f"Box {i}: {box}")