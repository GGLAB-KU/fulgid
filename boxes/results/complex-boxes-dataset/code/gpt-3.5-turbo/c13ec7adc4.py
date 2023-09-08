# Initial state of boxes
boxes = {
    0: ['polish', 'bracelet', 'dress'],
    1: ['candle', 'bag', 'shampoo', 'table'],
    2: ['lock', 'freezer', 'helmet', 'shoe'],
    3: ['mixer', 'paint', 'charger', 'scarf', 'umbrella'],
    4: ['zipper', 'glasses'],
    5: ['octopus', 'island', 'clock', 'comet'],
    6: ['cloud'],
    7: ['boat', 'fridge'],
    8: ['camera', 'bird', 'car', 'razor', 'note']
}

# Move the polish and the bracelet and the dress from Box 0 to Box 5.
items_to_move = ['polish', 'bracelet', 'dress']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[5].append(item)

# Put the drum into Box 0.
boxes[0].append('drum')

# Swap the scarf in Box 3 with the fridge in Box 7.
boxes[3].remove('scarf')
boxes[7].remove('fridge')
boxes[3].append('fridge')
boxes[7].append('scarf')

# Move the drum from Box 0 to Box 3.
boxes[0].remove('drum')
boxes[3].append('drum')

# Remove the fridge and the paint and the umbrella from Box 3.
items_to_remove = ['fridge', 'paint', 'umbrella']
for item in items_to_remove:
    boxes[3].remove(item)

# Replace the helmet and the freezer and the lock with the dice and the puzzle and the truck in Box 2.
boxes[2].remove('helmet')
boxes[2].remove('freezer')
boxes[2].remove('lock')
boxes[2].append('dice')
boxes[2].append('puzzle')
boxes[2].append('truck')

# Remove the cloud from Box 6.
boxes[6].remove('cloud')

# Remove the shampoo from Box 1.
boxes[1].remove('shampoo')

# Move the dice and the puzzle and the shoe from Box 2 to Box 6.
items_to_move = ['dice', 'puzzle', 'shoe']
for item in items_to_move:
    boxes[2].remove(item)
    boxes[6].append(item)

# Swap the dice in Box 6 with the scarf in Box 7.
boxes[6].remove('dice')
boxes[7].remove('scarf')
boxes[6].append('scarf')
boxes[7].append('dice')

# Empty Box 2.
boxes[2] = []

# Empty Box 8.
boxes[8] = []

# Remove the puzzle and the shoe from Box 6.
items_to_remove = ['puzzle', 'shoe']
for item in items_to_remove:
    boxes[6].remove(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")