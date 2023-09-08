# Initial state of boxes
boxes = {
    0: ['dice', 'zipper', 'violin'],
    1: ['fridge'],
    2: ['desert', 'brush', 'shelf', 'candle', 'blender'],
    3: ['octopus', 'paint', 'bird', 'ring', 'truck'],
    4: ['coin', 'lion', 'perfume', 'plane', 'console']
}

# Move the lion from Box 4 to Box 1.
boxes[4].remove('lion')
boxes[1].append('lion')

# Remove the console and the plane and the coin from Box 4.
items_to_remove = ['console', 'plane', 'coin']
for item in items_to_remove:
    boxes[4].remove(item)

# Remove the perfume from Box 4.
boxes[4].remove('perfume')

# Move the lion and the fridge from Box 1 to Box 3.
boxes[1].remove('lion')
boxes[3].append('lion')
boxes[1].remove('fridge')
boxes[3].append('fridge')

# Replace the bird and the truck and the ring with the snow and the chair and the bicycle in Box 3.
boxes[3].remove('bird')
boxes[3].remove('truck')
boxes[3].remove('ring')
boxes[3].append('snow')
boxes[3].append('chair')
boxes[3].append('bicycle')

# Put the hat into Box 3.
boxes[3].append('hat')

# Put the glove and the rain and the game into Box 1.
items_to_add = ['glove', 'rain', 'game']
for item in items_to_add:
    boxes[1].append(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")