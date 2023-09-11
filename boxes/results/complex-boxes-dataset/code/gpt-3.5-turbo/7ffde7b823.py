# Initial state of boxes
boxes = {
    0: ['console', 'lion', 'pillow', 'rain', 'umbrella'],
    1: ['blanket', 'ocean', 'dolphin'],
    2: ['card', 'toothpaste', 'leaf', 'telescope', 'bag'],
    3: [],
    4: ['mask', 'tie']
}

# Remove the mask from Box 4.
boxes[4].remove('mask')

# Swap the tie in Box 4 with the lion in Box 0.
boxes[0].remove('lion')
boxes[4].remove('tie')
boxes[0].append('tie')
boxes[4].append('lion')

# Move the lion from Box 4 to Box 2.
boxes[4].remove('lion')
boxes[2].append('lion')

# Remove the dolphin and the blanket and the ocean from Box 1.
items_to_remove = ['dolphin', 'blanket', 'ocean']
for item in items_to_remove:
    boxes[1].remove(item)

# Move the rain from Box 0 to Box 1.
boxes[0].remove('rain')
boxes[1].append('rain')

# Put the puzzle and the hat into Box 4.
boxes[4].append('puzzle')
boxes[4].append('hat')

# Move the lion from Box 2 to Box 4.
boxes[2].remove('lion')
boxes[4].append('lion')

# Replace the rain with the perfume in Box 1.
boxes[1].remove('rain')
boxes[1].append('perfume')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")