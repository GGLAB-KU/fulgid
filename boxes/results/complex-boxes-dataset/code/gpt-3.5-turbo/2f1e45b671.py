# Initial state of boxes
boxes = {
    0: ['meteor', 'bicycle', 'ocean'],
    1: ['octopus', 'lamp', 'cat', 'button', 'dress'],
    2: ['plate'],
    3: ['violin'],
    4: [],
    5: ['grass'],
    6: ['branch', 'mountain', 'dice']
}

# Put the horse into Box 6.
boxes[6].append('horse')

# Replace the plate with the swimsuit in Box 2.
boxes[2].remove('plate')
boxes[2].append('swimsuit')

# Move the branch and the horse from Box 6 to Box 4.
boxes[6].remove('branch')
boxes[6].remove('horse')
boxes[4].extend(['branch', 'horse'])

# Put the perfume and the mixer into Box 4.
boxes[4].extend(['perfume', 'mixer'])

# Swap the violin in Box 3 with the cat in Box 1.
boxes[3], boxes[1] = boxes[1], boxes[3]

# Move the mountain from Box 6 to Box 1.
boxes[6].remove('mountain')
boxes[1].append('mountain')

# Swap the lamp in Box 1 with the grass in Box 5.
boxes[1], boxes[5] = boxes[5], boxes[1]

# Move the lamp from Box 5 to Box 3.
boxes[5].remove('lamp')
boxes[3].append('lamp')

# Swap the lamp in Box 3 with the meteor in Box 0.
boxes[3], boxes[0] = boxes[0], boxes[3]

# Replace the dice with the toy in Box 6.
boxes[6].remove('dice')
boxes[6].append('toy')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")