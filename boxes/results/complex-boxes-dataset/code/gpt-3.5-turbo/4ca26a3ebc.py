# Initial state of boxes
boxes = {
    0: ['vase'],
    1: ['car', 'fork'],
    2: ['button', 'toothpaste', 'rain'],
    3: ['butterfly', 'boat', 'crown'],
    4: ['branch', 'storm', 'rock', 'wig', 'tiger'],
    5: ['charger', 'shirt', 'towel', 'table', 'desert'],
    6: ['perfume', 'glasses', 'lock', 'battery', 'pillow']
}

# Move the rock and the storm and the wig from Box 4 to Box 0.
items_to_move = ['rock', 'storm', 'wig']
for item in items_to_move:
    boxes[4].remove(item)
    boxes[0].append(item)

# Put the cow and the hat into Box 0.
boxes[0].append('cow')
boxes[0].append('hat')

# Replace the perfume with the comet in Box 6.
boxes[6].remove('perfume')
boxes[6].append('comet')

# Remove the hat and the storm from Box 0.
boxes[0].remove('hat')
boxes[0].remove('storm')

# Move the wig from Box 0 to Box 4.
boxes[0].remove('wig')
boxes[4].append('wig')

# Move the towel and the charger from Box 5 to Box 4.
items_to_move = ['towel', 'charger']
for item in items_to_move:
    boxes[5].remove(item)
    boxes[4].append(item)

# Move the glasses and the comet from Box 6 to Box 4.
items_to_move = ['glasses', 'comet']
for item in items_to_move:
    boxes[6].remove(item)
    boxes[4].append(item)

# Move the rock and the cow and the vase from Box 0 to Box 4.
items_to_move = ['rock', 'cow', 'vase']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[4].append(item)

# Replace the crown and the boat with the hat and the spoon in Box 3.
boxes[3].remove('crown')
boxes[3].remove('boat')
boxes[3].append('hat')
boxes[3].append('spoon')

# Move the fork from Box 1 to Box 2.
boxes[1].remove('fork')
boxes[2].append('fork')

# Swap the towel in Box 4 with the rain in Box 2.
boxes[4].remove('towel')
boxes[2].remove('rain')
boxes[4].append('rain')
boxes[2].append('towel')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")