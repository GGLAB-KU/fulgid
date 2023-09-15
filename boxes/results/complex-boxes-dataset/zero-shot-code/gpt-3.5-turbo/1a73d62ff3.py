boxes = [[], [], [], [], [], [], []]

# Box 0 contains the mountain
boxes[0] = ['mountain']

# Box 1 contains the belt and the oven
boxes[1] = ['belt', 'oven']

# Box 2 contains the glasses and the lock
boxes[2] = ['glasses', 'lock']

# Box 3 contains nothing

# Box 4 contains the blanket and the charger
boxes[4] = ['blanket', 'charger']

# Box 5 contains nothing

# Box 6 contains the camera, the scarf, and the key
boxes[6] = ['camera', 'scarf', 'key']

# Move the glasses from Box 2 to Box 5
boxes[5].append(boxes[2].pop(0))

# Put the lock into Box 0
boxes[0].append(boxes[2].pop(0))

# Empty Box 5
boxes[5] = []

# Put the oven and the desert into Box 1
boxes[1].extend(['oven', 'desert'])

# Swap the desert in Box 1 with the lock in Box 2
boxes[1][1], boxes[2][0] = boxes[2][0], boxes[1][1]

# Replace the charger and the blanket with the belt and the scissors in Box 4
boxes[4] = ['belt', 'scissors']

# Swap the scissors in Box 4 with the mountain in Box 0
boxes[0][0], boxes[4][1] = boxes[4][1], boxes[0][0]

# Move the belt from Box 4 to Box 3
boxes[3].append(boxes[4].pop(0))

# Move the desert from Box 2 to Box 5
boxes[5].append(boxes[2].pop(1))

# Replace the mountain with the camera in Box 4
boxes[4][0] = 'camera'

# Print the contents of each box
for i, box in enumerate(boxes):
    print(f"Box {i}: {box}")