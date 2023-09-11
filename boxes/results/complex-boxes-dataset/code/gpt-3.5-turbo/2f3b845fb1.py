# Initial state of boxes
boxes = {
    0: ['wig', 'fridge', 'makeup'],
    1: ['violin', 'ring', 'branch'],
    2: ['bird', 'meteor'],
    3: ['lightning', 'battery', 'ship', 'clock']
}

# Swap the violin in Box 1 with the battery in Box 3.
boxes[1].remove('violin')
boxes[3].remove('battery')
boxes[1].append('battery')
boxes[3].append('violin')

# Swap the branch in Box 1 with the clock in Box 3.
boxes[1].remove('branch')
boxes[3].remove('clock')
boxes[1].append('clock')
boxes[3].append('branch')

# Move the ship and the violin and the branch from Box 3 to Box 1.
items_to_move = ['ship', 'violin', 'branch']
for item in items_to_move:
    boxes[3].remove(item)
    boxes[1].append(item)

# Replace the makeup with the laptop in Box 0.
boxes[0].remove('makeup')
boxes[0].append('laptop')

# Remove the bird and the meteor from Box 2.
boxes[2].remove('bird')
boxes[2].remove('meteor')

# Move the laptop and the wig and the fridge from Box 0 to Box 2.
items_to_move = ['laptop', 'wig', 'fridge']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[2].append(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")