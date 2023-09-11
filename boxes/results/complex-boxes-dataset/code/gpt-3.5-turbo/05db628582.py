# Initial state of boxes
boxes = {
    0: ['comb', 'console', 'lion', 'submarine'],
    1: ['speaker'],
    2: ['river', 'controller'],
    3: ['flute', 'needle', 'shirt', 'cat', 'lipstick'],
    4: [],
    5: ['violin', 'ship', 'fork'],
    6: ['truck', 'coin', 'gloves', 'piano']
}

# Swap the speaker in Box 1 with the river in Box 2.
boxes[1].remove('speaker')
boxes[2].remove('river')
boxes[1].append('river')
boxes[2].append('speaker')

# Swap the cat in Box 3 with the piano in Box 6.
boxes[3].remove('cat')
boxes[6].remove('piano')
boxes[3].append('piano')
boxes[6].append('cat')

# Put the necklace and the toaster and the cup into Box 6.
items_to_put = ['necklace', 'toaster', 'cup']
for item in items_to_put:
    boxes[6].append(item)

# Remove the ship and the violin and the fork from Box 5.
items_to_remove = ['ship', 'violin', 'fork']
for item in items_to_remove:
    boxes[5].remove(item)

# Move the comb and the submarine from Box 0 to Box 1.
items_to_move = ['comb', 'submarine']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[1].append(item)

# Put the island into Box 0.
boxes[0].append('island')

# Move the comb and the river and the submarine from Box 1 to Box 2.
items_to_move = ['comb', 'river', 'submarine']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[2].append(item)

# Swap the truck in Box 6 with the island in Box 0.
boxes[6].remove('truck')
boxes[0].remove('island')
boxes[6].append('island')
boxes[0].append('truck')

# Remove the gloves and the coin from Box 6.
boxes[6].remove('gloves')
boxes[6].remove('coin')

# Put the toaster and the speaker and the river into Box 5.
items_to_put = ['toaster', 'speaker', 'river']
for item in items_to_put:
    boxes[5].append(item)

# Swap the speaker in Box 5 with the needle in Box 3.
boxes[5].remove('speaker')
boxes[3].remove('needle')
boxes[5].append('needle')
boxes[3].append('speaker')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")