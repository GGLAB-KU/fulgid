# Initial state of boxes
boxes = {
    0: ['towel', 'oven', 'battery'],
    1: ['magnet', 'table', 'polish', 'wig', 'butterfly'],
    2: ['card', 'glasses', 'game', 'dress'],
    3: ['bus', 'zipper', 'makeup', 'comb', 'branch'],
    4: ['desert'],
    5: [],
    6: ['pot', 'lipstick'],
    7: [],
    8: ['toothpaste', 'brush', 'shorts']
}

# Move the table and the wig and the magnet from Box 1 to Box 2.
items_to_move = ['table', 'wig', 'magnet']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[2].append(item)

# Move the branch from Box 3 to Box 1.
boxes[3].remove('branch')
boxes[1].append('branch')

# Move the polish and the branch and the butterfly from Box 1 to Box 4.
items_to_move = ['polish', 'branch', 'butterfly']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[4].append(item)

# Swap the toothpaste in Box 8 with the lipstick in Box 6.
boxes[8].remove('toothpaste')
boxes[6].remove('lipstick')
boxes[8].append('lipstick')
boxes[6].append('toothpaste')

# Move the battery from Box 0 to Box 4.
boxes[0].remove('battery')
boxes[4].append('battery')

# Remove the lipstick and the brush and the shorts from Box 8.
items_to_remove = ['lipstick', 'brush', 'shorts']
for item in items_to_remove:
    boxes[8].remove(item)

# Empty Box 6.
boxes[6] = []

# Remove the towel from Box 0.
boxes[0].remove('towel')

# Remove the zipper and the bus and the makeup from Box 3.
items_to_remove = ['zipper', 'bus', 'makeup']
for item in items_to_remove:
    boxes[3].remove(item)

# Replace the table and the glasses with the magnet and the tree in Box 2.
boxes[2].remove('table')
boxes[2].remove('glasses')
boxes[2].append('magnet')
boxes[2].append('tree')

# Move the comb from Box 3 to Box 7.
boxes[3].remove('comb')
boxes[7].append('comb')

# Move the comb from Box 7 to Box 4.
boxes[7].remove('comb')
boxes[4].append('comb')

# Remove the polish and the battery from Box 4.
items_to_remove = ['polish', 'battery']
for item in items_to_remove:
    boxes[4].remove(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")