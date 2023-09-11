# Initial state of boxes
boxes = {
    0: ['phone', 'star', 'jungle'],
    1: ['branch', 'ship', 'shorts', 'wig'],
    2: [],
    3: ['candle']
}

# Move the candle from Box 3 to Box 1.
boxes[3].remove('candle')
boxes[1].append('candle')

# Remove the star and the jungle from Box 0.
boxes[0].remove('star')
boxes[0].remove('jungle')

# Replace the phone with the thunder in Box 0.
boxes[0].remove('phone')
boxes[0].append('thunder')

# Remove the thunder from Box 0.
boxes[0].remove('thunder')

# Replace the branch and the wig with the meteor and the leaf in Box 1.
boxes[1].remove('branch')
boxes[1].remove('wig')
boxes[1].append('meteor')
boxes[1].append('leaf')

# Remove the shorts from Box 1.
boxes[1].remove('shorts')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")