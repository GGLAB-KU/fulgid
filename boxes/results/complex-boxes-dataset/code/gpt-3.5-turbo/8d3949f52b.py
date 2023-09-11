# Initial state of boxes
boxes = {
    0: ['speaker', 'ship'],
    1: ['headphone', 'shorts', 'fish', 'wig', 'microscope'],
    2: ['lipstick', 'spoon', 'phone', 'shark', 'octopus'],
    3: ['frame', 'bowl', 'violin'],
    4: ['blanket', 'scissors', 'necklace', 'magnet', 'book']
}

# Remove the shark from Box 2.
boxes[2].remove('shark')

# Move the spoon from Box 2 to Box 1.
boxes[2].remove('spoon')
boxes[1].append('spoon')

# Put the mixer and the clock and the magnet into Box 4.
items_to_move = ['mixer', 'clock', 'magnet']
for item in items_to_move:
    boxes[4].append(item)

# Remove the clock from Box 4.
boxes[4].remove('clock')

# Swap the octopus in Box 2 with the bowl in Box 3.
boxes[2].remove('octopus')
boxes[3].remove('bowl')
boxes[2].append('bowl')
boxes[3].append('octopus')

# Remove the spoon and the fish from Box 1.
items_to_remove = ['spoon', 'fish']
for item in items_to_remove:
    boxes[1].remove(item)

# Replace the book with the freezer in Box 4.
boxes[4].remove('book')
boxes[4].append('freezer')

# Remove the octopus from Box 3.
boxes[3].remove('octopus')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")