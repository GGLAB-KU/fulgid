# Initial state of boxes
boxes = {
    0: ['note', 'mirror', 'belt'],
    1: ['grass'],
    2: ['scarf', 'usb', 'sculpture'],
    3: ['fish', 'microwave', 'wallet', 'needle'],
    4: [],
    5: ['shirt', 'swimsuit', 'bicycle'],
    6: ['mixer', 'flute'],
    7: ['sandals', 'grinder'],
    8: ['rocket', 'pot'],
    9: [],
    10: ['pan', 'shorts', 'telescope', 'glasses', 'laptop'],
    11: ['branch', 'charger'],
    12: []
}

# Move the charger from Box 11 to Box 8.
boxes[11].remove('charger')
boxes[8].append('charger')

# Remove the rocket and the charger and the pot from Box 8.
items_to_remove = ['rocket', 'charger', 'pot']
for item in items_to_remove:
    boxes[8].remove(item)

# Put the lock into Box 1.
boxes[1].append('lock')

# Swap the grass in Box 1 with the branch in Box 11.
boxes[1].remove('grass')
boxes[11].remove('branch')
boxes[1].append('branch')
boxes[11].append('grass')

# Remove the flute and the mixer from Box 6.
items_to_remove = ['flute', 'mixer']
for item in items_to_remove:
    boxes[6].remove(item)

# Swap the grass in Box 11 with the wallet in Box 3.
boxes[11].remove('grass')
boxes[3].remove('wallet')
boxes[11].append('wallet')
boxes[3].append('grass')

# Replace the note and the belt and the mirror with the plane and the sandals and the thunder in Box 0.
boxes[0].remove('note')
boxes[0].remove('belt')
boxes[0].remove('mirror')
boxes[0].append('plane')
boxes[0].append('sandals')
boxes[0].append('thunder')

# Put the sandals into Box 5.
boxes[5].append('sandals')

# Swap the glasses in Box 10 with the scarf in Box 2.
boxes[10].remove('glasses')
boxes[2].remove('scarf')
boxes[10].append('scarf')
boxes[2].append('glasses')

# Put the flute and the camera and the note into Box 0.
items_to_move = ['flute', 'camera', 'note']
for item in items_to_move:
    boxes[6].remove(item)
    boxes[0].append(item)

# Remove the laptop and the telescope from Box 10.
items_to_remove = ['laptop', 'telescope']
for item in items_to_remove:
    boxes[10].remove(item)

# Replace the wallet with the coat in Box 11.
boxes[11].remove('wallet')
boxes[11].append('coat')

# Move the grinder and the sandals from Box 7 to Box 4.
items_to_move = ['grinder', 'sandals']
for item in items_to_move:
    boxes[7].remove(item)
    boxes[4].append(item)

# Move the shirt and the bicycle from Box 5 to Box 7.
items_to_move = ['shirt', 'bicycle']
for item in items_to_move:
    boxes[5].remove(item)
    boxes[7].append(item)

# Remove the sandals and the grinder from Box 4.
items_to_remove = ['sandals', 'grinder']
for item in items_to_remove:
    boxes[4].remove(item)

# Swap the needle in Box 3 with the shirt in Box 7.
boxes[3].remove('needle')
boxes[7].remove('shirt')
boxes[3].append('shirt')
boxes[7].append('needle')

# Remove the shirt and the microwave from Box 3.
items_to_remove = ['shirt', 'microwave']
for item in items_to_remove:
    boxes[3].remove(item)

# Remove the fish from Box 3.
boxes[3].remove('fish')

# Remove the plane from Box 0.
boxes[0].remove('plane')

# Remove the bicycle and the needle from Box 7.
items_to_remove = ['bicycle', 'needle']
for item in items_to_remove:
    boxes[7].remove(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")