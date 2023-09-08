# Initial state of boxes
boxes = {
    0: ['lion', 'towel'],
    1: ['branch', 'boot', 'shampoo', 'mask', 'river'],
    2: ['vase', 'mountain', 'toothbrush', 'bowl'],
    3: ['helmet', 'shorts', 'plate', 'thread', 'spoon'],
    4: ['scarf', 'desert', 'starfish', 'elephant', 'comb'],
    5: ['dice', 'microwave']
}

# Remove the branch and the boot and the shampoo from Box 1.
items_to_remove = ['branch', 'boot', 'shampoo']
for item in items_to_remove:
    boxes[1].remove(item)

# Move the microwave from Box 5 to Box 1.
boxes[5].remove('microwave')
boxes[1].append('microwave')

# Put the train and the island into Box 1.
boxes[1].append('train')
boxes[1].append('island')

# Swap the towel in Box 0 with the microwave in Box 1.
boxes[0].remove('towel')
boxes[1].remove('microwave')
boxes[0].append('microwave')
boxes[1].append('towel')

# Put the needle and the elephant and the note into Box 0.
boxes[0].append('needle')
boxes[0].append('elephant')
boxes[0].append('note')

# Move the shorts from Box 3 to Box 4.
boxes[3].remove('shorts')
boxes[4].append('shorts')

# Put the shampoo into Box 2.
boxes[2].append('shampoo')

# Remove the towel and the island from Box 1.
boxes[1].remove('towel')
boxes[1].remove('island')

# Put the car and the charger into Box 3.
boxes[3].append('car')
boxes[3].append('charger')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")