# Initial state of boxes
boxes = {
    0: ['keyboard', 'car'],
    1: [],
    2: ['thunder'],
    3: [],
    4: ['grinder', 'chair', 'island', 'leaf', 'blanket']
}

# Remove the grinder from Box 4.
boxes[4].remove('grinder')

# Replace the island with the towel in Box 4.
boxes[4].remove('island')
boxes[4].append('towel')

# Swap the thunder in Box 2 with the chair in Box 4.
boxes[2].remove('thunder')
boxes[4].remove('chair')
boxes[2].append('chair')
boxes[4].append('thunder')

# Remove the keyboard from Box 0.
boxes[0].remove('keyboard')

# Replace the thunder with the freezer in Box 4.
boxes[4].remove('thunder')
boxes[4].append('freezer')

# Replace the towel and the blanket and the leaf with the microwave and the elephant and the shelf in Box 4.
boxes[4].remove('towel')
boxes[4].remove('blanket')
boxes[4].remove('leaf')
boxes[4].append('microwave')
boxes[4].append('elephant')
boxes[4].append('shelf')

# Remove the microwave and the freezer and the elephant from Box 4.
boxes[4].remove('microwave')
boxes[4].remove('freezer')
boxes[4].remove('elephant')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")