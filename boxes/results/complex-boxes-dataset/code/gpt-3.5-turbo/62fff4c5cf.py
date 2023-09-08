# Initial state of boxes
boxes = {
    0: ['toothbrush', 'brush', 'ring'],
    1: ['keyboard', 'clock', 'toaster', 'flute', 'pot'],
    2: ['mountain', 'thunder'],
    3: ['paint', 'umbrella', 'toothpaste'],
    4: ['train', 'plate', 'jungle', 'battery'],
    5: ['shoes', 'dice', 'sculpture', 'forest', 'glove'],
    6: ['headphone', 'rain', 'tree', 'horse'],
    7: ['card', 'cup', 'storm', 'toy'],
    8: ['shampoo', 'wig'],
    9: ['snow'],
    10: ['note', 'basket', 'speaker', 'car'],
    11: ['ship', 'tie', 'vase', 'grinder', 'bear'],
    12: ['belt']
}

# Put the fish and the blanket and the forest into Box 6.
items_to_move = ['fish', 'blanket', 'forest']
for item in items_to_move:
    boxes[6].append(item)

# Swap the ship in Box 11 with the belt in Box 12.
boxes[11].remove('ship')
boxes[12].remove('belt')
boxes[11].append('belt')
boxes[12].append('ship')

# Remove the card and the storm from Box 7.
boxes[7].remove('card')
boxes[7].remove('storm')

# Move the snow from Box 9 to Box 8.
boxes[9].remove('snow')
boxes[8].append('snow')

# Move the toaster and the pot and the flute from Box 1 to Box 3.
items_to_move = ['toaster', 'pot', 'flute']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[3].append(item)

# Replace the fish and the horse with the umbrella and the microscope in Box 6.
boxes[6].remove('fish')
boxes[6].remove('horse')
boxes[6].append('umbrella')
boxes[6].append('microscope')

# Move the blanket and the microscope and the forest from Box 6 to Box 12.
items_to_move = ['blanket', 'microscope', 'forest']
for item in items_to_move:
    boxes[6].remove(item)
    boxes[12].append(item)

# Replace the microscope and the blanket with the swimsuit and the gloves in Box 12.
boxes[12].remove('microscope')
boxes[12].remove('blanket')
boxes[12].append('swimsuit')
boxes[12].append('gloves')

# Empty Box 5.
boxes[5] = []

# Swap the tie in Box 11 with the ship in Box 12.
boxes[11].remove('tie')
boxes[12].remove('ship')
boxes[11].append('ship')
boxes[12].append('tie')

# Put the laptop into Box 12.
boxes[12].append('laptop')

# Put the hat and the coral into Box 10.
items_to_move = ['hat', 'coral']
for item in items_to_move:
    boxes[10].append(item)

# Remove the belt from Box 11.
boxes[11].remove('belt')

# Put the grinder and the drum into Box 11.
items_to_move = ['grinder', 'drum']
for item in items_to_move:
    boxes[11].append(item)

# Remove the wig from Box 8.
boxes[8].remove('wig')

# Remove the brush and the ring and the toothbrush from Box 0.
items_to_remove = ['brush', 'ring', 'toothbrush']
for item in items_to_remove:
    boxes[0].remove(item)

# Put the lamp into Box 5.
boxes[5].append('lamp')

# Put the microscope and the desert into Box 6.
items_to_move = ['microscope', 'desert']
for item in items_to_move:
    boxes[6].append(item)

# Remove the laptop and the forest from Box 12.
boxes[12].remove('laptop')
boxes[12].remove('forest')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")