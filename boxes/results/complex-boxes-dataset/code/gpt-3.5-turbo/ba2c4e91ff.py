# Initial state of boxes
boxes = {
    0: ['tie', 'perfume', 'magnet', 'plane'],
    1: ['mixer'],
    2: ['grinder', 'glasses', 'telescope', 'mask'],
    3: [],
    4: ['console', 'bicycle', 'wallet'],
    5: ['earring'],
    6: ['brush', 'grass', 'flower', 'book', 'tape'],
    7: ['sock', 'beach']
}

# Put the piano and the coat and the bus into Box 1.
items_to_put = ['piano', 'coat', 'bus']
for item in items_to_put:
    boxes[1].append(item)

# Remove the perfume from Box 0.
boxes[0].remove('perfume')

# Replace the flower with the thunder in Box 6.
boxes[6].remove('flower')
boxes[6].append('thunder')

# Put the cow and the toothpaste and the zipper into Box 6.
items_to_put = ['cow', 'toothpaste', 'zipper']
for item in items_to_put:
    boxes[6].append(item)

# Remove the earring from Box 5.
boxes[5].remove('earring')

# Move the bicycle and the console and the wallet from Box 4 to Box 6.
items_to_move = ['bicycle', 'console', 'wallet']
for item in items_to_move:
    boxes[4].remove(item)
    boxes[6].append(item)

# Put the scissors and the shark and the truck into Box 0.
items_to_put = ['scissors', 'shark', 'truck']
for item in items_to_put:
    boxes[0].append(item)

# Move the console and the tape from Box 6 to Box 0.
items_to_move = ['console', 'tape']
for item in items_to_move:
    boxes[6].remove(item)
    boxes[0].append(item)

# Empty Box 2.
boxes[2] = []

# Swap the sock in Box 7 with the piano in Box 1.
boxes[7].remove('sock')
boxes[1].remove('piano')
boxes[7].append('piano')
boxes[1].append('sock')

# Remove the piano from Box 7.
boxes[7].remove('piano')

# Replace the tape with the dice in Box 0.
boxes[0].remove('tape')
boxes[0].append('dice')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")