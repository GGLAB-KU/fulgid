# Initial state of boxes
boxes = {
    0: ['doll', 'candle'],
    1: ['scarf', 'thunder', 'beach', 'toy'],
    2: ['charger', 'microwave', 'bird', 'cat'],
    3: ['hat'],
    4: ['towel'],
    5: ['cup', 'desert', 'cloud', 'butterfly', 'ship'],
    6: [],
    7: ['grinder', 'river', 'bag']
}

# Remove the toy and the beach and the scarf from Box 1.
items_to_remove = ['toy', 'beach', 'scarf']
for item in items_to_remove:
    boxes[1].remove(item)

# Replace the towel with the octopus in Box 4.
boxes[4].remove('towel')
boxes[4].append('octopus')

# Put the fridge and the soap and the wig into Box 7.
items_to_add = ['fridge', 'soap', 'wig']
for item in items_to_add:
    boxes[7].append(item)

# Move the bag from Box 7 to Box 6.
boxes[6].append(boxes[7].pop(boxes[7].index('bag')))

# Swap the octopus in Box 4 with the candle in Box 0.
boxes[0].remove('candle')
boxes[4].remove('octopus')
boxes[0].append('octopus')
boxes[4].append('candle')

# Replace the grinder and the fridge with the gloves and the magnet in Box 7.
boxes[7].remove('grinder')
boxes[7].remove('fridge')
boxes[7].append('gloves')
boxes[7].append('magnet')

# Put the tiger into Box 6.
boxes[6].append('tiger')

# Move the hat from Box 3 to Box 0.
boxes[0].append(boxes[3].pop(boxes[3].index('hat')))

# Remove the river and the magnet and the soap from Box 7.
items_to_remove = ['river', 'magnet', 'soap']
for item in items_to_remove:
    boxes[7].remove(item)

# Remove the bag from Box 6.
boxes[6].remove('bag')

# Empty Box 7.
boxes[7] = []

# Replace the candle with the bell in Box 4.
boxes[4].remove('candle')
boxes[4].append('bell')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")