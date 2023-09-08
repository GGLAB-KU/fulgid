# Initial state of boxes
boxes = {
    0: ['usb', 'frame', 'perfume', 'vase'],
    1: ['pan', 'sock', 'battery'],
    2: ['zipper'],
    3: ['fish', 'cow'],
    4: ['telescope', 'mask', 'scarf']
}

# Replace the cow and the fish with the cat and the comet in Box 3.
boxes[3].remove('cow')
boxes[3].remove('fish')
boxes[3].append('cat')
boxes[3].append('comet')

# Move the scarf and the telescope and the mask from Box 4 to Box 0.
items_to_move = ['scarf', 'telescope', 'mask']
for item in items_to_move:
    boxes[4].remove(item)
    boxes[0].append(item)

# Swap the zipper in Box 2 with the sock in Box 1.
boxes[2], boxes[1] = boxes[1], boxes[2]

# Put the leaf into Box 0.
boxes[0].append('leaf')

# Remove the frame from Box 0.
boxes[0].remove('frame')

# Replace the comet and the cat with the motorcycle and the umbrella in Box 3.
boxes[3].remove('comet')
boxes[3].remove('cat')
boxes[3].append('motorcycle')
boxes[3].append('umbrella')

# Remove the sock from Box 2.
boxes[2].remove('sock')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")