# Initial state of boxes
boxes = {
    0: ['helmet'],
    1: ['puzzle', 'cat'],
    2: [],
    3: ['tie', 'needle'],
    4: ['dress', 'horn', 'bicycle', 'coin'],
    5: ['card', 'blanket', 'octopus', 'key'],
    6: ['mask', 'toaster'],
    7: ['submarine'],
    8: [],
    9: ['branch', 'perfume'],
    10: ['sun', 'violin', 'rocket', 'wire', 'scissors'],
    11: ['book'],
    12: ['flute', 'fridge', 'skirt', 'wallet'],
    13: ['shelf']
}

# Swap the horn in Box 4 with the skirt in Box 12.
boxes[4].remove('horn')
boxes[12].remove('skirt')
boxes[4].append('skirt')
boxes[12].append('horn')

# Swap the wallet in Box 12 with the wire in Box 10.
boxes[12].remove('wallet')
boxes[10].remove('wire')
boxes[12].append('wire')
boxes[10].append('wallet')

# Put the toothpaste and the lamp and the mountain into Box 2.
items_to_put = ['toothpaste', 'lamp', 'mountain']
for item in items_to_put:
    boxes[2].append(item)

# Put the island into Box 11.
boxes[11].append('island')

# Remove the wire from Box 12.
boxes[12].remove('wire')

# Move the submarine from Box 7 to Box 6.
boxes[7].remove('submarine')
boxes[6].append('submarine')

# Move the helmet from Box 0 to Box 7.
boxes[0].remove('helmet')
boxes[7].append('helmet')

# Replace the puzzle and the cat with the keyboard and the guitar in Box 1.
boxes[1].remove('puzzle')
boxes[1].remove('cat')
boxes[1].append('keyboard')
boxes[1].append('guitar')

# Replace the octopus and the blanket and the key with the towel and the sandals and the rain in Box 5.
boxes[5].remove('octopus')
boxes[5].remove('blanket')
boxes[5].remove('key')
boxes[5].append('towel')
boxes[5].append('sandals')
boxes[5].append('rain')

# Move the perfume and the branch from Box 9 to Box 6.
boxes[9].remove('perfume')
boxes[9].remove('branch')
boxes[6].append('perfume')
boxes[6].append('branch')

# Put the shampoo and the tiger into Box 5.
boxes[5].append('shampoo')
boxes[5].append('tiger')

# Remove the rocket and the sun and the violin from Box 10.
boxes[10].remove('rocket')
boxes[10].remove('sun')
boxes[10].remove('violin')

# Swap the keyboard in Box 1 with the tiger in Box 5.
boxes[1].remove('keyboard')
boxes[5].remove('tiger')
boxes[1].append('tiger')
boxes[5].append('keyboard')

# Remove the coin and the skirt and the dress from Box 4.
boxes[4].remove('coin')
boxes[4].remove('skirt')
boxes[4].remove('dress')

# Swap the branch in Box 6 with the book in Box 11.
boxes[6].remove('branch')
boxes[11].remove('book')
boxes[6].append('book')
boxes[11].append('branch')

# Swap the wallet in Box 10 with the submarine in Box 6.
boxes[10].remove('wallet')
boxes[6].remove('submarine')
boxes[10].append('submarine')
boxes[6].append('wallet')

# Swap the bicycle in Box 4 with the shelf in Box 13.
boxes[4].remove('bicycle')
boxes[13].remove('shelf')
boxes[4].append('shelf')
boxes[13].append('bicycle')

# Put the bear and the planet into Box 0.
boxes[0].append('bear')
boxes[0].append('planet')

# Remove the mountain and the lamp and the toothpaste from Box 2.
boxes[2].remove('mountain')
boxes[2].remove('lamp')
boxes[2].remove('toothpaste')

# Remove the branch and the island from Box 11.
boxes[11].remove('branch')
boxes[11].remove('island')

# Remove the toaster and the wallet from Box 6.
boxes[6].remove('toaster')
boxes[6].remove('wallet')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")