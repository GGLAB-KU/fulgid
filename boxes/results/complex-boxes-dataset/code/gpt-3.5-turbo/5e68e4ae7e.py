# Initial state of boxes
boxes = {
    0: [],
    1: ['star', 'toothpaste', 'speaker'],
    2: ['mirror'],
    3: ['toy', 'sock', 'swimsuit', 'ring', 'rocket'],
    4: ['scissors', 'tie', 'grinder', 'car', 'island'],
    5: ['tree', 'boot'],
    6: ['blanket', 'lion', 'horse'],
    7: ['horn', 'soap'],
    8: ['shorts', 'telescope']
}

# Replace the boot and the tree with the battery and the bag in Box 5.
boxes[5].remove('boot')
boxes[5].remove('tree')
boxes[5].append('battery')
boxes[5].append('bag')

# Replace the tie and the island with the car and the phone in Box 4.
boxes[4].remove('tie')
boxes[4].remove('island')
boxes[4].append('car')
boxes[4].append('phone')

# Move the sock from Box 3 to Box 0.
boxes[3].remove('sock')
boxes[0].append('sock')

# Replace the mirror with the oven in Box 2.
boxes[2].remove('mirror')
boxes[2].append('oven')

# Replace the rocket and the toy with the magnet and the shelf in Box 3.
boxes[3].remove('rocket')
boxes[3].remove('toy')
boxes[3].append('magnet')
boxes[3].append('shelf')

# Move the soap from Box 7 to Box 6.
boxes[7].remove('soap')
boxes[6].append('soap')

# Put the cat and the sun and the river into Box 4.
items_to_add = ['cat', 'sun', 'river']
for item in items_to_add:
    boxes[4].append(item)

# Swap the speaker in Box 1 with the bag in Box 5.
boxes[1].remove('speaker')
boxes[5].remove('bag')
boxes[1].append('bag')
boxes[5].append('speaker')

# Swap the oven in Box 2 with the grinder in Box 4.
boxes[2].remove('oven')
boxes[4].remove('grinder')
boxes[2].append('grinder')
boxes[4].append('oven')

# Swap the bag in Box 1 with the shorts in Box 8.
boxes[1].remove('bag')
boxes[8].remove('shorts')
boxes[1].append('shorts')
boxes[8].append('bag')

# Swap the ring in Box 3 with the shorts in Box 1.
boxes[3].remove('ring')
boxes[1].remove('shorts')
boxes[3].append('shorts')
boxes[1].append('ring')

# Swap the shorts in Box 3 with the horn in Box 7.
boxes[3].remove('shorts')
boxes[7].remove('horn')
boxes[3].append('horn')
boxes[7].append('shorts')

# Move the speaker from Box 5 to Box 0.
boxes[5].remove('speaker')
boxes[0].append('speaker')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")