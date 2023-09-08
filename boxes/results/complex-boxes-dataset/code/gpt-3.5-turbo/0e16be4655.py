# Initial state of boxes
boxes = {
    0: [],
    1: ['charger', 'spoon'],
    2: [],
    3: [],
    4: [],
    5: ['lock', 'umbrella', 'desert', 'horse']
}

# Remove the lock and the horse and the desert from Box 5.
items_to_remove = ['lock', 'horse', 'desert']
for item in items_to_remove:
    boxes[5].remove(item)

# Replace the charger with the pot in Box 1.
boxes[1].remove('charger')
boxes[1].append('pot')

# Put the pen and the meteor into Box 4.
boxes[4].append('pen')
boxes[4].append('meteor')

# Move the umbrella from Box 5 to Box 1.
boxes[5].remove('umbrella')
boxes[1].append('umbrella')

# Put the shoe and the coin and the lamp into Box 2.
boxes[2].append('shoe')
boxes[2].append('coin')
boxes[2].append('lamp')

# Move the pot and the spoon from Box 1 to Box 3.
boxes[1].remove('pot')
boxes[1].remove('spoon')
boxes[3].append('pot')
boxes[3].append('spoon')

# Remove the pot and the spoon from Box 3.
boxes[3].remove('pot')
boxes[3].remove('spoon')

# Move the lamp and the coin from Box 2 to Box 3.
boxes[2].remove('lamp')
boxes[2].remove('coin')
boxes[3].append('lamp')
boxes[3].append('coin')

# Swap the pen in Box 4 with the umbrella in Box 1.
boxes[4].remove('pen')
boxes[1].remove('umbrella')
boxes[4].append('umbrella')
boxes[1].append('pen')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")