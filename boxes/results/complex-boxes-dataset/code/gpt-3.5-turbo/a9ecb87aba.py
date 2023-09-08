# Initial state of boxes
boxes = {
    0: [],
    1: ['snow', 'butterfly', 'bowl', 'meteor'],
    2: ['cup'],
    3: ['ocean', 'violin', 'glasses', 'tape'],
    4: ['freezer', 'oven', 'bell']
}

# Move the tape from Box 3 to Box 0.
boxes[3].remove('tape')
boxes[0].append('tape')

# Put the soap into Box 1.
boxes[1].append('soap')

# Put the keyboard and the game into Box 4.
boxes[4].append('keyboard')
boxes[4].append('game')

# Replace the violin with the clock in Box 3.
boxes[3].remove('violin')
boxes[3].append('clock')

# Remove the clock from Box 3.
boxes[3].remove('clock')

# Move the cup from Box 2 to Box 1.
boxes[2].remove('cup')
boxes[1].append('cup')

# Move the tape from Box 0 to Box 2.
boxes[0].remove('tape')
boxes[2].append('tape')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")