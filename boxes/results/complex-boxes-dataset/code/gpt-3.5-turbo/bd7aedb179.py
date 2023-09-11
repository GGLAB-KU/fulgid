# Initial state of boxes
boxes = {
    0: ['apple', 'umbrella', 'shoe', 'wig'],
    1: ['polish'],
    2: ['wire', 'dice', 'ship'],
    3: ['puzzle', 'coat', 'necklace', 'whistle'],
    4: [],
    5: ['beach', 'plate', 'meteor', 'thunder', 'blanket'],
    6: ['sandals'],
    7: ['grinder', 'branch', 'storm'],
    8: ['octopus', 'motorcycle'],
    9: ['gloves', 'fish', 'pot', 'tiger'],
    10: [],
    11: ['sun', 'chair'],
    12: ['plane', 'keyboard', 'paint', 'shoes']
}

# Swap the storm in Box 7 with the necklace in Box 3.
boxes[7].remove('storm')
boxes[3].remove('necklace')
boxes[7].append('necklace')
boxes[3].append('storm')

# Remove the dice from Box 2.
boxes[2].remove('dice')

# Replace the sandals with the microwave in Box 6.
boxes[6].remove('sandals')
boxes[6].append('microwave')

# Remove the branch from Box 7.
boxes[7].remove('branch')

# Remove the fish and the gloves and the pot from Box 9.
items_to_remove = ['fish', 'gloves', 'pot']
for item in items_to_remove:
    boxes[9].remove(item)

# Put the usb and the wire into Box 11.
boxes[11].append('usb')
boxes[11].append('wire')

# Move the microwave from Box 6 to Box 7.
boxes[6].remove('microwave')
boxes[7].append('microwave')

# Move the necklace from Box 7 to Box 8.
boxes[7].remove('necklace')
boxes[8].append('necklace')

# Put the apple and the scissors and the shoe into Box 3.
items_to_put = ['apple', 'scissors', 'shoe']
for item in items_to_put:
    boxes[0].remove(item)
    boxes[3].append(item)

# Remove the microwave from Box 7.
boxes[7].remove('microwave')

# Remove the grinder from Box 7.
boxes[7].remove('grinder')

# Move the motorcycle from Box 8 to Box 6.
boxes[8].remove('motorcycle')
boxes[6].append('motorcycle')

# Move the tiger from Box 9 to Box 6.
boxes[9].remove('tiger')
boxes[6].append('tiger')

# Remove the polish from Box 1.
boxes[1].remove('polish')

# Swap the octopus in Box 8 with the whistle in Box 3.
boxes[8].remove('octopus')
boxes[3].remove('whistle')
boxes[8].append('whistle')
boxes[3].append('octopus')

# Remove the plane from Box 12.
boxes[12].remove('plane')

# Move the usb and the wire from Box 11 to Box 3.
boxes[11].remove('usb')
boxes[11].remove('wire')
boxes[3].append('usb')
boxes[3].append('wire')

# Move the wig and the apple and the shoe from Box 0 to Box 3.
items_to_move = ['wig', 'apple', 'shoe']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[3].append(item)

# Put the cloud and the bear into Box 5.
boxes[5].append('cloud')
boxes[5].append('bear')

# Move the storm and the wire and the apple from Box 3 to Box 11.
items_to_move = ['storm', 'wire', 'apple']
for item in items_to_move:
    boxes[3].remove(item)
    boxes[11].append(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")