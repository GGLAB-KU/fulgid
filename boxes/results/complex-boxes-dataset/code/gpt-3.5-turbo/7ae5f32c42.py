# Initial state of boxes
boxes = {
    0: ['headphone', 'planet', 'shampoo', 'shorts'],
    1: ['cup', 'magnet', 'game', 'note'],
    2: ['key', 'thunder'],
    3: ['pillow', 'needle', 'blanket', 'boat', 'mirror'],
    4: ['horn', 'dolphin', 'freezer', 'towel']
}

# Put the violin and the bear into Box 0.
boxes[0].append('violin')
boxes[0].append('bear')

# Swap the towel in Box 4 with the shampoo in Box 0.
boxes[0].remove('shampoo')
boxes[4].remove('towel')
boxes[0].append('towel')
boxes[4].append('shampoo')

# Remove the blanket from Box 3.
boxes[3].remove('blanket')

# Replace the magnet and the cup with the plate and the book in Box 1.
boxes[1].remove('magnet')
boxes[1].remove('cup')
boxes[1].append('plate')
boxes[1].append('book')

# Swap the pillow in Box 3 with the book in Box 1.
boxes[3].remove('pillow')
boxes[1].remove('book')
boxes[3].append('book')
boxes[1].append('pillow')

# Replace the headphone and the shorts and the violin with the drum and the ring and the telescope in Box 0.
boxes[0].remove('headphone')
boxes[0].remove('shorts')
boxes[0].remove('violin')
boxes[0].append('drum')
boxes[0].append('ring')
boxes[0].append('telescope')

# Remove the telescope from Box 0.
boxes[0].remove('telescope')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")