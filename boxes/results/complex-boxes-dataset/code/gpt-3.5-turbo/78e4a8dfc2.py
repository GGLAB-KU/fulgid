# Initial state of boxes
boxes = {
    0: ['ocean', 'key', 'tiger', 'whistle'],
    1: ['forest', 'chair', 'telescope', 'tree'],
    2: ['shark'],
    3: ['mirror', 'paint', 'snow', 'microwave', 'scarf']
}

# Remove the whistle and the key and the ocean from Box 0.
items_to_remove = ['whistle', 'key', 'ocean']
for item in items_to_remove:
    boxes[0].remove(item)

# Move the shark from Box 2 to Box 3.
shark = boxes[2].pop()
boxes[3].append(shark)

# Replace the telescope with the whistle in Box 1.
boxes[1].remove('telescope')
boxes[1].append('whistle')

# Remove the tree and the chair and the forest from Box 1.
items_to_remove = ['tree', 'chair', 'forest']
for item in items_to_remove:
    boxes[1].remove(item)

# Remove the shark and the scarf and the paint from Box 3.
items_to_remove = ['shark', 'scarf', 'paint']
for item in items_to_remove:
    boxes[3].remove(item)

# Move the whistle from Box 1 to Box 2.
whistle = boxes[1].pop()
boxes[2].append(whistle)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")