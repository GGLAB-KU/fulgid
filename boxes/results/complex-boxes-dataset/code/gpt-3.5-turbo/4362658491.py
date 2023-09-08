# Initial state of boxes
boxes = {
    0: ['wire', 'submarine', 'ship'],
    1: ['forest', 'dress'],
    2: ['comb', 'bowl', 'octopus'],
    3: ['coat', 'ocean', 'candle', 'bracelet'],
    4: ['shoe', 'boat', 'clock', 'toothbrush'],
    5: ['microwave', 'polish', 'needle', 'razor', 'bag']
}

# Replace the ocean and the bracelet and the coat with the grinder and the cat and the paint in Box 3.
boxes[3].remove('ocean')
boxes[3].remove('bracelet')
boxes[3].remove('coat')
boxes[3].append('grinder')
boxes[3].append('cat')
boxes[3].append('paint')

# Swap the toothbrush in Box 4 with the bowl in Box 2.
boxes[4].remove('toothbrush')
boxes[2].remove('bowl')
boxes[4].append('bowl')
boxes[2].append('toothbrush')

# Remove the comb and the octopus and the toothbrush from Box 2.
items_to_remove = ['comb', 'octopus', 'toothbrush']
for item in items_to_remove:
    boxes[2].remove(item)

# Put the octopus and the bell and the vase into Box 5.
items_to_put = ['octopus', 'bell', 'vase']
for item in items_to_put:
    boxes[5].append(item)

# Put the forest and the card into Box 4.
items_to_put = ['forest', 'card']
for item in items_to_put:
    boxes[4].append(item)

# Swap the razor in Box 5 with the cat in Box 3.
boxes[5].remove('razor')
boxes[3].remove('cat')
boxes[5].append('cat')
boxes[3].append('razor')

# Replace the wire with the scissors in Box 0.
boxes[0].remove('wire')
boxes[0].append('scissors')

# Put the comb into Box 0.
boxes[0].append('comb')

# Move the cat from Box 5 to Box 3.
boxes[5].remove('cat')
boxes[3].append('cat')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")