# Initial state of boxes
boxes = {
    0: ['razor', 'camera'],
    1: ['elephant', 'belt', 'moon'],
    2: [],
    3: ['perfume', 'ship', 'ring'],
    4: ['gloves', 'earring', 'console'],
    5: ['spoon'],
    6: ['bowl', 'submarine', 'lock'],
    7: [],
    8: []
}

# Replace the gloves with the desert in Box 4.
boxes[4].remove('gloves')
boxes[4].append('desert')

# Move the moon from Box 1 to Box 0.
boxes[1].remove('moon')
boxes[0].append('moon')

# Move the razor and the moon and the camera from Box 0 to Box 2.
items_to_move = ['razor', 'moon', 'camera']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[2].append(item)

# Put the makeup and the magnet and the pot into Box 7.
items_to_put = ['makeup', 'magnet', 'pot']
for item in items_to_put:
    boxes[7].append(item)

# Move the perfume and the ship from Box 3 to Box 7.
items_to_move = ['perfume', 'ship']
for item in items_to_move:
    boxes[3].remove(item)
    boxes[7].append(item)

# Swap the spoon in Box 5 with the camera in Box 2.
boxes[5].remove('spoon')
boxes[2].remove('camera')
boxes[5].append('camera')
boxes[2].append('spoon')

# Empty Box 4.
boxes[4] = []

# Replace the camera with the harmonica in Box 5.
boxes[5].remove('camera')
boxes[5].append('harmonica')

# Put the planet into Box 0.
boxes[0].append('planet')

# Move the planet from Box 0 to Box 8.
boxes[0].remove('planet')
boxes[8].append('planet')

# Remove the spoon and the moon and the razor from Box 2.
items_to_remove = ['spoon', 'moon', 'razor']
for item in items_to_remove:
    boxes[2].remove(item)

# Move the planet from Box 8 to Box 4.
boxes[8].remove('planet')
boxes[4].append('planet')

# Replace the planet with the motorcycle in Box 4.
boxes[4].remove('planet')
boxes[4].append('motorcycle')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")