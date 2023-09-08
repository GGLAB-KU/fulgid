# Initial state of boxes
boxes = {
    0: ['blanket', 'shirt', 'shelf'],
    1: ['wig', 'shark', 'storm', 'card'],
    2: ['watch'],
    3: ['guitar', 'dolphin', 'scarf'],
    4: ['flower']
}

# Put the lamp and the mountain and the clock into Box 3.
boxes[3].append('lamp')
boxes[3].append('mountain')
boxes[3].append('clock')

# Swap the flower in Box 4 with the clock in Box 3.
boxes[4], boxes[3][boxes[3].index('clock')] = boxes[3][boxes[3].index('clock')], boxes[4]

# Move the watch from Box 2 to Box 3.
boxes[2].remove('watch')
boxes[3].append('watch')

# Remove the clock from Box 4.
boxes[4].remove('clock')

# Remove the dolphin from Box 3.
boxes[3].remove('dolphin')

# Replace the guitar and the watch with the pillow and the plane in Box 3.
boxes[3].remove('guitar')
boxes[3].remove('watch')
boxes[3].append('pillow')
boxes[3].append('plane')

# Remove the shirt from Box 0.
boxes[0].remove('shirt')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")