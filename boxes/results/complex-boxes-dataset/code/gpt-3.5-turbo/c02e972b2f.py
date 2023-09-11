# Initial state of boxes
boxes = {
    0: ['crown', 'phone', 'frame'],
    1: ['watch', 'needle', 'polish'],
    2: ['pants', 'shelf'],
    3: ['ocean'],
    4: ['comet'],
    5: [],
    6: ['scissors'],
    7: ['belt', 'note', 'sun', 'spoon', 'fork'],
    8: ['pot', 'butterfly', 'fridge', 'chair', 'motorcycle']
}

# Swap the needle in Box 1 with the crown in Box 0.
boxes[0].remove('crown')
boxes[1].remove('needle')
boxes[0].append('needle')
boxes[1].append('crown')

# Put the skirt and the jacket and the microwave into Box 2.
items_to_put = ['skirt', 'jacket', 'microwave']
for item in items_to_put:
    boxes[2].append(item)

# Move the ocean from Box 3 to Box 6.
boxes[3].remove('ocean')
boxes[6].append('ocean')

# Put the pen and the guitar into Box 1.
items_to_put = ['pen', 'guitar']
for item in items_to_put:
    boxes[1].append(item)

# Remove the belt and the fork and the spoon from Box 7.
items_to_remove = ['belt', 'fork', 'spoon']
for item in items_to_remove:
    boxes[7].remove(item)

# Put the paint and the violin and the boat into Box 3.
items_to_put = ['paint', 'violin', 'boat']
for item in items_to_put:
    boxes[3].append(item)

# Move the violin and the paint from Box 3 to Box 4.
boxes[3].remove('violin')
boxes[3].remove('paint')
boxes[4].append('violin')
boxes[4].append('paint')

# Remove the guitar and the watch and the pen from Box 1.
items_to_remove = ['guitar', 'watch', 'pen']
for item in items_to_remove:
    boxes[1].remove(item)

# Replace the crown and the polish with the perfume and the violin in Box 1.
boxes[1].remove('crown')
boxes[1].remove('polish')
boxes[1].append('perfume')
boxes[1].append('violin')

# Remove the violin and the perfume from Box 1.
boxes[1].remove('violin')
boxes[1].remove('perfume')

# Replace the microwave and the jacket and the pants with the glasses and the snow and the pillow in Box 2.
boxes[2].remove('microwave')
boxes[2].remove('jacket')
boxes[2].remove('pants')
boxes[2].append('glasses')
boxes[2].append('snow')
boxes[2].append('pillow')

# Put the necklace and the beach and the card into Box 7.
items_to_put = ['necklace', 'beach', 'card']
for item in items_to_put:
    boxes[7].append(item)

# Remove the violin and the comet and the paint from Box 4.
items_to_remove = ['violin', 'comet', 'paint']
for item in items_to_remove:
    boxes[4].remove(item)

# Move the pillow and the snow and the glasses from Box 2 to Box 3.
items_to_move = ['pillow', 'snow', 'glasses']
for item in items_to_move:
    boxes[2].remove(item)
    boxes[3].append(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")