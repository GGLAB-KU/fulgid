# Initial state of boxes
boxes = {
    0: ['earring', 'star'],
    1: ['frame', 'toothpaste'],
    2: ['shoes', 'beach', 'mountain', 'pants'],
    3: ['branch', 'crown', 'storm', 'towel']
}

# Move the storm from Box 3 to Box 2.
boxes[3].remove('storm')
boxes[2].append('storm')

# Remove the frame from Box 1.
boxes[1].remove('frame')

# Replace the star with the plane in Box 0.
boxes[0].remove('star')
boxes[0].append('plane')

# Remove the towel and the crown from Box 3.
boxes[3].remove('towel')
boxes[3].remove('crown')

# Remove the shoes and the mountain and the pants from Box 2.
items_to_remove = ['shoes', 'mountain', 'pants']
for item in items_to_remove:
    boxes[2].remove(item)

# Put the blanket and the lipstick and the helmet into Box 3.
items_to_add = ['blanket', 'lipstick', 'helmet']
for item in items_to_add:
    boxes[3].append(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")