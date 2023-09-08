# Initial state of boxes
boxes = {
    0: [],
    1: [],
    2: ['camera', 'butterfly', 'helmet', 'bag'],
    3: [],
    4: ['sandals', 'seaweed']
}

# Put the mountain into Box 1.
boxes[1].append('mountain')

# Put the bag and the laptop into Box 4.
boxes[4].append('bag')
boxes[4].append('laptop')

# Remove the camera and the helmet and the bag from Box 2.
items_to_remove = ['camera', 'helmet', 'bag']
for item in items_to_remove:
    boxes[2].remove(item)

# Remove the bag and the laptop from Box 4.
boxes[4].remove('bag')
boxes[4].remove('laptop')

# Put the scissors into Box 1.
boxes[1].append('scissors')

# Move the mountain from Box 1 to Box 2.
boxes[1].remove('mountain')
boxes[2].append('mountain')

# Move the butterfly and the mountain from Box 2 to Box 4.
boxes[2].remove('butterfly')
boxes[2].remove('mountain')
boxes[4].append('butterfly')
boxes[4].append('mountain')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")