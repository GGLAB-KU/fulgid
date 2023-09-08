# Initial state of boxes
boxes = {
    0: ['scarf', 'desert', 'dolphin', 'apple', 'spoon'],
    1: ['doll', 'star', 'razor'],
    2: ['glasses', 'rocket'],
    3: ['glove', 'pan', 'telescope', 'sculpture', 'puzzle'],
    4: [],
    5: ['mountain'],
    6: ['charger', 'shoe', 'makeup', 'battery']
}

# Put the scarf and the shorts and the fork into Box 6.
items_to_move = ['scarf', 'shorts', 'fork']
for item in items_to_move:
    boxes[6].append(item)

# Swap the makeup in Box 6 with the glove in Box 3.
boxes[6].remove('makeup')
boxes[3].remove('glove')
boxes[6].append('glove')
boxes[3].append('makeup')

# Remove the charger and the fork and the scarf from Box 6.
items_to_remove = ['charger', 'fork', 'scarf']
for item in items_to_remove:
    boxes[6].remove(item)

# Remove the spoon and the scarf and the dolphin from Box 0.
items_to_remove = ['spoon', 'scarf', 'dolphin']
for item in items_to_remove:
    boxes[0].remove(item)

# Remove the rocket from Box 2.
boxes[2].remove('rocket')

# Replace the doll with the toothbrush in Box 1.
boxes[1].remove('doll')
boxes[1].append('toothbrush')

# Remove the desert and the apple from Box 0.
items_to_remove = ['desert', 'apple']
for item in items_to_remove:
    boxes[0].remove(item)

# Swap the toothbrush in Box 1 with the mountain in Box 5.
boxes[1].remove('toothbrush')
boxes[5].remove('mountain')
boxes[1].append('mountain')
boxes[5].append('toothbrush')

# Replace the razor and the star with the helmet and the oven in Box 1.
boxes[1].remove('razor')
boxes[1].remove('star')
boxes[1].append('helmet')
boxes[1].append('oven')

# Remove the toothbrush from Box 5.
boxes[5].remove('toothbrush')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")