# Initial state of boxes
boxes = {
    0: ['lock', 'laptop', 'bus'],
    1: ['beach', 'sock'],
    2: ['boot', 'telescope'],
    3: ['card', 'gloves', 'charger'],
    4: ['rock', 'flower', 'speaker'],
    5: ['truck'],
    6: ['scarf'],
    7: ['wire', 'chair', 'plate', 'microwave'],
    8: ['apple', 'bear', 'puzzle', 'flute', 'tape'],
    9: ['basket', 'toothbrush', 'cloud', 'lamp'],
    10: ['microscope', 'zipper', 'cat', 'shark']
}

# Move the boot and the telescope from Box 2 to Box 6.
boxes[2].remove('boot')
boxes[2].remove('telescope')
boxes[6].append('boot')
boxes[6].append('telescope')

# Swap the toothbrush in Box 9 with the lock in Box 0.
boxes[0].remove('lock')
boxes[9].remove('toothbrush')
boxes[0].append('toothbrush')
boxes[9].append('lock')

# Remove the speaker and the rock and the flower from Box 4.
items_to_remove = ['speaker', 'rock', 'flower']
for item in items_to_remove:
    boxes[4].remove(item)

# Swap the telescope in Box 6 with the truck in Box 5.
boxes[5].remove('truck')
boxes[6].remove('telescope')
boxes[5].append('telescope')
boxes[6].append('truck')

# Remove the truck and the scarf and the boot from Box 6.
items_to_remove = ['truck', 'scarf', 'boot']
for item in items_to_remove:
    boxes[6].remove(item)

# Remove the beach from Box 1.
boxes[1].remove('beach')

# Remove the microscope and the shark and the cat from Box 10.
items_to_remove = ['microscope', 'shark', 'cat']
for item in items_to_remove:
    boxes[10].remove(item)

# Put the rock and the game and the piano into Box 9.
items_to_move = ['rock', 'game', 'piano']
for item in items_to_move:
    boxes[4].remove(item)
    boxes[9].append(item)

# Empty Box 1.
boxes[1] = []

# Remove the telescope from Box 5.
boxes[5].remove('telescope')

# Put the bird into Box 10.
boxes[10].append('bird')

# Swap the toothbrush in Box 0 with the game in Box 9.
boxes[0].remove('toothbrush')
boxes[9].remove('game')
boxes[0].append('game')
boxes[9].append('toothbrush')

# Move the lock and the lamp from Box 9 to Box 4.
boxes[9].remove('lock')
boxes[9].remove('lamp')
boxes[4].append('lock')
boxes[4].append('lamp')

# Move the bear and the apple and the tape from Box 8 to Box 0.
items_to_move = ['bear', 'apple', 'tape']
for item in items_to_move:
    boxes[8].remove(item)
    boxes[0].append(item)

# Remove the charger and the card from Box 3.
items_to_remove = ['charger', 'card']
for item in items_to_remove:
    boxes[3].remove(item)

# Move the basket and the piano and the cloud from Box 9 to Box 3.
items_to_move = ['basket', 'piano', 'cloud']
for item in items_to_move:
    boxes[9].remove(item)
    boxes[3].append(item)

# Move the plate and the microwave and the wire from Box 7 to Box 4.
items_to_move = ['plate', 'microwave', 'wire']
for item in items_to_move:
    boxes[7].remove(item)
    boxes[4].append(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")