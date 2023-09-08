# Initial state of boxes
boxes = {
    0: ['lamp', 'jacket', 'towel', 'plane', 'toaster'],
    1: ['wallet', 'mountain', 'bag', 'phone'],
    2: ['bus', 'bowl', 'perfume', 'needle', 'desert'],
    3: [],
    4: ['motorcycle'],
    5: ['necklace', 'horse'],
    6: ['microscope', 'star', 'whistle', 'scissors'],
    7: ['shampoo', 'boat', 'headphone', 'bell'],
    8: [],
    9: ['pan'],
    10: ['cup', 'pants', 'crown', 'battery'],
    11: ['bear', 'coin']
}

# Put the horn into Box 5.
boxes[5].append('horn')

# Move the toaster and the plane and the towel from Box 0 to Box 2.
items_to_move = ['toaster', 'plane', 'towel']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[2].append(item)

# Replace the bag with the brush in Box 1.
boxes[1].remove('bag')
boxes[1].append('brush')

# Move the star and the whistle and the scissors from Box 6 to Box 0.
items_to_move = ['star', 'whistle', 'scissors']
for item in items_to_move:
    boxes[6].remove(item)
    boxes[0].append(item)

# Move the pan from Box 9 to Box 1.
boxes[9].remove('pan')
boxes[1].append('pan')

# Replace the wallet and the pan with the comet and the cloud in Box 1.
boxes[1].remove('wallet')
boxes[1].remove('pan')
boxes[1].append('comet')
boxes[1].append('cloud')

# Swap the cloud in Box 1 with the motorcycle in Box 4.
boxes[1].remove('cloud')
boxes[4].remove('motorcycle')
boxes[1].append('motorcycle')
boxes[4].append('cloud')

# Remove the jacket and the whistle from Box 0.
boxes[0].remove('jacket')
boxes[0].remove('whistle')

# Move the bear from Box 11 to Box 9.
boxes[11].remove('bear')
boxes[9].append('bear')

# Put the apple and the piano and the basket into Box 4.
items_to_move = ['apple', 'piano', 'basket']
for item in items_to_move:
    boxes[4].append(item)

# Move the lamp and the scissors and the star from Box 0 to Box 2.
items_to_move = ['lamp', 'scissors', 'star']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[2].append(item)

# Put the shampoo and the bus into Box 11.
boxes[7].remove('shampoo')
boxes[2].remove('bus')
boxes[11].extend(['shampoo', 'bus'])

# Move the crown from Box 10 to Box 0.
boxes[10].remove('crown')
boxes[0].append('crown')

# Move the motorcycle and the phone from Box 1 to Box 3.
boxes[1].remove('motorcycle')
boxes[1].remove('phone')
boxes[3].extend(['motorcycle', 'phone'])

# Remove the battery and the cup from Box 10.
boxes[10].remove('battery')
boxes[10].remove('cup')

# Remove the motorcycle from Box 3.
boxes[3].remove('motorcycle')

# Move the headphone from Box 7 to Box 1.
boxes[7].remove('headphone')
boxes[1].append('headphone')

# Replace the bear with the polish in Box 9.
boxes[9].remove('bear')
boxes[9].append('polish')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")