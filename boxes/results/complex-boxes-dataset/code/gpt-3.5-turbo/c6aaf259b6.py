# Initial state of boxes
boxes = {
    0: ['mountain', 'gloves', 'necklace', 'shirt'],
    1: ['rocket', 'tie', 'phone', 'grinder', 'chair'],
    2: ['harmonica', 'sock'],
    3: ['jacket', 'game', 'magnet', 'tiger', 'crown'],
    4: [],
    5: ['wig', 'cow', 'wallet'],
    6: ['note', 'microwave'],
    7: [],
    8: ['ring', 'dice', 'pants', 'button'],
    9: ['piano', 'earring', 'thunder', 'perfume', 'ship'],
    10: ['pan', 'wire']
}

# Remove the mountain and the gloves and the shirt from Box 0.
items_to_remove = ['mountain', 'gloves', 'shirt']
for item in items_to_remove:
    boxes[0].remove(item)

# Put the plate and the tape and the lock into Box 2.
items_to_add = ['plate', 'tape', 'lock']
for item in items_to_add:
    boxes[2].append(item)

# Remove the magnet and the jacket and the game from Box 3.
items_to_remove = ['magnet', 'jacket', 'game']
for item in items_to_remove:
    boxes[3].remove(item)

# Swap the lock in Box 2 with the crown in Box 3.
boxes[2].remove('lock')
boxes[3].remove('crown')
boxes[2].append('crown')
boxes[3].append('lock')

# Put the gloves and the toy and the plane into Box 6.
items_to_add = ['gloves', 'toy', 'plane']
for item in items_to_add:
    boxes[6].append(item)

# Swap the ship in Box 9 with the necklace in Box 0.
boxes[0].remove('necklace')
boxes[9].remove('ship')
boxes[0].append('ship')
boxes[9].append('necklace')

# Empty Box 8.
boxes[8] = []

# Move the lock and the tiger from Box 3 to Box 7.
items_to_move = ['lock', 'tiger']
for item in items_to_move:
    boxes[3].remove(item)
    boxes[7].append(item)

# Replace the plate and the tape with the octopus and the shark in Box 2.
boxes[2].remove('plate')
boxes[2].remove('tape')
boxes[2].append('octopus')
boxes[2].append('shark')

# Swap the shark in Box 2 with the lock in Box 7.
boxes[2].remove('shark')
boxes[7].remove('lock')
boxes[2].append('lock')
boxes[7].append('shark')

# Move the gloves from Box 6 to Box 2.
boxes[6].remove('gloves')
boxes[2].append('gloves')

# Remove the microwave and the plane and the toy from Box 6.
items_to_remove = ['microwave', 'plane', 'toy']
for item in items_to_remove:
    boxes[6].remove(item)

# Empty Box 1.
boxes[1] = []

# Remove the wallet from Box 5.
boxes[5].remove('wallet')

# Move the note from Box 6 to Box 5.
boxes[6].remove('note')
boxes[5].append('note')

# Put the brush and the star and the whistle into Box 6.
items_to_add = ['brush', 'star', 'whistle']
for item in items_to_add:
    boxes[6].append(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")