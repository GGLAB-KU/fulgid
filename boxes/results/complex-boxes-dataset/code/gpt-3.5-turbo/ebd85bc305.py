# Initial state of boxes
boxes = {
    0: ['bird', 'button', 'microscope', 'thunder', 'horse'],
    1: ['console', 'toothbrush', 'controller', 'storm'],
    2: ['belt', 'snow', 'leaf', 'hat'],
    3: ['river', 'guitar', 'magnet', 'perfume', 'cow'],
    4: ['watch'],
    5: ['mirror', 'key', 'pants', 'grinder', 'car'],
    6: [],
    7: [],
    8: ['desert', 'planet', 'whistle']
}

# Move the toothbrush and the storm from Box 1 to Box 4.
boxes[1].remove('toothbrush')
boxes[1].remove('storm')
boxes[4].append('toothbrush')
boxes[4].append('storm')

# Remove the button and the bird and the thunder from Box 0.
items_to_remove = ['button', 'bird', 'thunder']
for item in items_to_remove:
    boxes[0].remove(item)

# Replace the controller and the console with the ship and the thread in Box 1.
boxes[1].remove('controller')
boxes[1].remove('console')
boxes[1].append('ship')
boxes[1].append('thread')

# Remove the ship and the thread from Box 1.
boxes[1].remove('ship')
boxes[1].remove('thread')

# Put the cow and the cloud into Box 7.
boxes[7].append('cow')
boxes[7].append('cloud')

# Swap the key in Box 5 with the cloud in Box 7.
boxes[5].remove('key')
boxes[7].remove('cloud')
boxes[5].append('cloud')
boxes[7].append('key')

# Replace the leaf and the snow and the belt with the pot and the freezer and the key in Box 2.
boxes[2].remove('leaf')
boxes[2].remove('snow')
boxes[2].remove('belt')
boxes[2].append('pot')
boxes[2].append('freezer')
boxes[2].append('key')

# Put the motorcycle into Box 5.
boxes[5].append('motorcycle')

# Remove the key and the cow from Box 7.
boxes[7].remove('key')
boxes[7].remove('cow')

# Remove the whistle and the desert and the planet from Box 8.
items_to_remove = ['whistle', 'desert', 'planet']
for item in items_to_remove:
    boxes[8].remove(item)

# Put the truck and the bag into Box 2.
boxes[2].append('truck')
boxes[2].append('bag')

# Move the watch and the storm from Box 4 to Box 7.
boxes[4].remove('watch')
boxes[4].remove('storm')
boxes[7].append('watch')
boxes[7].append('storm')

# Move the toothbrush from Box 4 to Box 6.
boxes[4].remove('toothbrush')
boxes[6].append('toothbrush')

# Move the freezer and the pot and the hat from Box 2 to Box 5.
items_to_move = ['freezer', 'pot', 'hat']
for item in items_to_move:
    boxes[2].remove(item)
    boxes[5].append(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")