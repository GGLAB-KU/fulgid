# Initial state of boxes
boxes = {
    0: ['mountain', 'blanket', 'razor'],
    1: [],
    2: ['pan', 'pants', 'forest', 'vase', 'butterfly'],
    3: ['controller', 'umbrella', 'bicycle'],
    4: ['ring']
}

# Move the blanket and the mountain and the razor from Box 0 to Box 4.
items_to_move = ['blanket', 'mountain', 'razor']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[4].append(item)

# Move the forest and the pants and the butterfly from Box 2 to Box 0.
items_to_move = ['forest', 'pants', 'butterfly']
for item in items_to_move:
    boxes[2].remove(item)
    boxes[0].append(item)

# Swap the bicycle in Box 3 with the ring in Box 4.
boxes[3].remove('bicycle')
boxes[4].remove('ring')
boxes[3].append('ring')
boxes[4].append('bicycle')

# Remove the mountain and the razor from Box 4.
boxes[4].remove('mountain')
boxes[4].remove('razor')

# Remove the forest and the butterfly from Box 0.
boxes[0].remove('forest')
boxes[0].remove('butterfly')

# Put the polish into Box 3.
boxes[3].append('polish')

# Remove the blanket from Box 4.
boxes[4].remove('blanket')

# Swap the ring in Box 3 with the pants in Box 0.
boxes[3].remove('ring')
boxes[0].remove('pants')
boxes[3].append('pants')
boxes[0].append('ring')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")