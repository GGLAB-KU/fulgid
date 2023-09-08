# Initial state of boxes
boxes = {
    0: ['planet', 'console'],
    1: ['lipstick', 'glove', 'river', 'key'],
    2: ['umbrella'],
    3: ['battery', 'paint'],
    4: [],
    5: ['dice', 'ship', 'table'],
    6: ['coral', 'shampoo', 'shoe', 'sock', 'ring'],
    7: ['lock', 'fridge', 'horn'],
    8: ['blanket', 'moon', 'necklace'],
    9: ['phone', 'toothpaste', 'flower', 'skirt'],
    10: ['boat', 'bell'],
    11: ['lightning'],
    12: ['game', 'brush', 'telescope', 'cloud', 'puzzle'],
    13: [],
    14: []
}

# Remove the moon and the necklace and the blanket from Box 8.
items_to_remove = ['moon', 'necklace', 'blanket']
for item in items_to_remove:
    boxes[8].remove(item)

# Remove the shoe and the shampoo from Box 6.
items_to_remove = ['shoe', 'shampoo']
for item in items_to_remove:
    boxes[6].remove(item)

# Remove the dice and the table from Box 5.
items_to_remove = ['dice', 'table']
for item in items_to_remove:
    boxes[5].remove(item)

# Put the usb into Box 7.
boxes[7].append('usb')

# Swap the battery in Box 3 with the key in Box 1.
boxes[3].remove('battery')
boxes[1].remove('key')
boxes[3].append('key')
boxes[1].append('battery')

# Swap the console in Box 0 with the ship in Box 5.
boxes[0].remove('console')
boxes[5].remove('ship')
boxes[0].append('ship')
boxes[5].append('console')

# Swap the console in Box 5 with the boat in Box 10.
boxes[5].remove('console')
boxes[10].remove('boat')
boxes[5].append('boat')
boxes[10].append('console')

# Move the key and the paint from Box 3 to Box 11.
boxes[3].remove('key')
boxes[3].remove('paint')
boxes[11].append('key')
boxes[11].append('paint')

# Move the fridge and the usb and the horn from Box 7 to Box 14.
items_to_move = ['fridge', 'usb', 'horn']
for item in items_to_move:
    boxes[7].remove(item)
    boxes[14].append(item)

# Swap the boat in Box 5 with the ship in Box 0.
boxes[5].remove('boat')
boxes[0].remove('ship')
boxes[5].append('ship')
boxes[0].append('boat')

# Replace the boat and the planet with the scissors and the console in Box 0.
boxes[0].remove('boat')
boxes[0].remove('planet')
boxes[0].append('scissors')
boxes[0].append('console')

# Move the ship from Box 5 to Box 8.
boxes[5].remove('ship')
boxes[8].append('ship')

# Replace the console and the scissors with the snow and the flower in Box 0.
boxes[0].remove('console')
boxes[0].remove('scissors')
boxes[0].append('snow')
boxes[0].append('flower')

# Replace the battery and the lipstick with the comb and the seaweed in Box 1.
boxes[1].remove('battery')
boxes[1].remove('lipstick')
boxes[1].append('comb')
boxes[1].append('seaweed')

# Move the ring and the coral from Box 6 to Box 1.
boxes[6].remove('ring')
boxes[6].remove('coral')
boxes[1].append('ring')
boxes[1].append('coral')

# Move the paint and the key from Box 11 to Box 7.
boxes[11].remove('paint')
boxes[11].remove('key')
boxes[7].append('paint')
boxes[7].append('key')

# Remove the cloud and the game and the puzzle from Box 12.
items_to_remove = ['cloud', 'game', 'puzzle']
for item in items_to_remove:
    boxes[12].remove(item)

# Swap the telescope in Box 12 with the lightning in Box 11.
boxes[12].remove('telescope')
boxes[11].remove('lightning')
boxes[12].append('lightning')
boxes[11].append('telescope')

# Put the beach and the pants into Box 1.
boxes[1].append('beach')
boxes[1].append('pants')

# Swap the lightning in Box 12 with the telescope in Box 11.
boxes[12].remove('lightning')
boxes[11].remove('telescope')
boxes[12].append('telescope')
boxes[11].append('lightning')

# Swap the console in Box 10 with the ship in Box 8.
boxes[10].remove('console')
boxes[8].remove('ship')
boxes[10].append('ship')
boxes[8].append('console')

# Put the fork and the tree into Box 10.
boxes[10].append('fork')
boxes[10].append('tree')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")