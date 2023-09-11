# Initial state of boxes
boxes = {
    0: [],
    1: ['basket', 'beach'],
    2: ['telescope'],
    3: ['pillow', 'thread'],
    4: ['spoon'],
    5: ['perfume', 'shoe', 'cup', 'dolphin', 'key'],
    6: ['flower'],
    7: ['wire'],
    8: ['mirror', 'pan'],
    9: ['scarf', 'card', 'fish', 'coat', 'polish'],
    10: []
}

# Put the umbrella and the fish into Box 1.
boxes[1].append('umbrella')
boxes[1].append('fish')

# Swap the scarf in Box 9 with the flower in Box 6.
boxes[9].remove('scarf')
boxes[6].remove('flower')
boxes[9].append('flower')
boxes[6].append('scarf')

# Remove the beach and the umbrella and the basket from Box 1.
items_to_remove = ['beach', 'umbrella', 'basket']
for item in items_to_remove:
    boxes[1].remove(item)

# Remove the spoon from Box 4.
boxes[4].remove('spoon')

# Remove the wire from Box 7.
boxes[7].remove('wire')

# Put the coral and the camera and the river into Box 3.
items_to_put = ['coral', 'camera', 'river']
for item in items_to_put:
    boxes[3].append(item)

# Put the key and the submarine into Box 7.
boxes[7].append('key')
boxes[5].remove('submarine')
boxes[7].append('submarine')

# Move the scarf from Box 6 to Box 4.
boxes[6].remove('scarf')
boxes[4].append('scarf')

# Put the rocket and the paint and the magnet into Box 3.
items_to_put = ['rocket', 'paint', 'magnet']
for item in items_to_put:
    boxes[3].append(item)

# Put the razor into Box 0.
boxes[0].append('razor')

# Remove the submarine from Box 7.
boxes[7].remove('submarine')

# Move the scarf from Box 4 to Box 6.
boxes[4].remove('scarf')
boxes[6].append('scarf')

# Replace the fish with the ocean in Box 1.
boxes[1].remove('fish')
boxes[1].append('ocean')

# Swap the telescope in Box 2 with the razor in Box 0.
boxes[2].remove('telescope')
boxes[0].remove('razor')
boxes[2].append('razor')
boxes[0].append('telescope')

# Swap the key in Box 7 with the dolphin in Box 5.
boxes[7].remove('key')
boxes[5].remove('dolphin')
boxes[7].append('dolphin')
boxes[5].append('key')

# Remove the thread from Box 3.
boxes[3].remove('thread')

# Move the ocean from Box 1 to Box 7.
boxes[1].remove('ocean')
boxes[7].append('ocean')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")