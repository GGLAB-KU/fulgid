# Initial state of boxes
boxes = {
    0: ['helmet', 'elephant', 'skirt'],
    1: ['laptop', 'perfume', 'leaf'],
    2: ['storm', 'bicycle', 'hat', 'earring'],
    3: ['star'],
    4: [],
    5: [],
    6: ['lamp']
}

# Swap the lamp in Box 6 with the leaf in Box 1.
boxes[6].remove('lamp')
boxes[1].remove('leaf')
boxes[6].append('leaf')
boxes[1].append('lamp')

# Swap the leaf in Box 6 with the perfume in Box 1.
boxes[6].remove('leaf')
boxes[1].remove('perfume')
boxes[6].append('perfume')
boxes[1].append('leaf')

# Move the perfume from Box 6 to Box 2.
boxes[6].remove('perfume')
boxes[2].append('perfume')

# Swap the lamp in Box 1 with the skirt in Box 0.
boxes[1].remove('lamp')
boxes[0].remove('skirt')
boxes[1].append('skirt')
boxes[0].append('lamp')

# Put the blanket and the plane and the forest into Box 3.
items_to_move = ['blanket', 'plane', 'forest']
for item in items_to_move:
    boxes[3].append(item)

# Put the flute and the mask and the card into Box 6.
items_to_move = ['flute', 'mask', 'card']
for item in items_to_move:
    boxes[6].append(item)

# Move the flute and the card from Box 6 to Box 1.
items_to_move = ['flute', 'card']
for item in items_to_move:
    boxes[6].remove(item)
    boxes[1].append(item)

# Put the river into Box 4.
boxes[4].append('river')

# Swap the lamp in Box 0 with the perfume in Box 2.
boxes[0].remove('lamp')
boxes[2].remove('perfume')
boxes[0].append('perfume')
boxes[2].append('lamp')

# Swap the earring in Box 2 with the plane in Box 3.
boxes[2].remove('earring')
boxes[3].remove('plane')
boxes[2].append('plane')
boxes[3].append('earring')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")