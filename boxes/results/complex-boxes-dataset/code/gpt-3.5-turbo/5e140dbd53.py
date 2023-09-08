# Initial state of boxes
boxes = {
    0: ['cat', 'fork', 'blender', 'microwave', 'toaster'],
    1: ['helmet', 'starfish', 'comb'],
    2: ['frame', 'pan'],
    3: ['toothbrush', 'gloves', 'controller', 'bell', 'whistle'],
    4: ['tree', 'plane', 'charger', 'coral', 'sun'],
    5: ['scarf'],
    6: ['rain', 'jungle', 'harmonica', 'camera', 'key'],
    7: [],
    8: ['wallet', 'button', 'thunder', 'fish']
}

# Remove the frame and the pan from Box 2.
boxes[2].remove('frame')
boxes[2].remove('pan')

# Swap the plane in Box 4 with the microwave in Box 0.
boxes[0].remove('microwave')
boxes[4].remove('plane')
boxes[0].append('plane')
boxes[4].append('microwave')

# Move the cat and the blender and the plane from Box 0 to Box 1.
items_to_move = ['cat', 'blender', 'plane']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[1].append(item)

# Replace the charger with the pen in Box 4.
boxes[4].remove('charger')
boxes[4].append('pen')

# Put the puzzle and the mountain into Box 5.
boxes[5].append('puzzle')
boxes[5].append('mountain')

# Move the fork and the toaster from Box 0 to Box 8.
items_to_move = ['fork', 'toaster']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[8].append(item)

# Move the thunder from Box 8 to Box 3.
boxes[8].remove('thunder')
boxes[3].append('thunder')

# Remove the coral from Box 4.
boxes[4].remove('coral')

# Move the puzzle and the mountain and the scarf from Box 5 to Box 8.
items_to_move = ['puzzle', 'mountain', 'scarf']
for item in items_to_move:
    boxes[5].remove(item)
    boxes[8].append(item)

# Move the camera and the rain and the jungle from Box 6 to Box 1.
items_to_move = ['camera', 'rain', 'jungle']
for item in items_to_move:
    boxes[6].remove(item)
    boxes[1].append(item)

# Swap the pen in Box 4 with the fork in Box 8.
boxes[4].remove('pen')
boxes[8].remove('fork')
boxes[4].append('fork')
boxes[8].append('pen')

# Move the microwave and the fork from Box 4 to Box 6.
items_to_move = ['microwave', 'fork']
for item in items_to_move:
    boxes[4].remove(item)
    boxes[6].append(item)

# Replace the gloves and the whistle with the plate and the mask in Box 3.
boxes[3].remove('gloves')
boxes[3].remove('whistle')
boxes[3].append('plate')
boxes[3].append('mask')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")