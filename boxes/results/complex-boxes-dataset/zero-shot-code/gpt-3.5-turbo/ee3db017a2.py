box = {
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

# Swap the horn in Box 4 with the skirt in Box 12
box[4].remove('horn')
box[12].remove('skirt')
box[4].append('skirt')
box[12].append('horn')

# Swap the wallet in Box 12 with the wire in Box 10
box[12].remove('wallet')
box[10].remove('wire')
box[12].append('wire')
box[10].append('wallet')

# Put the toothpaste and the lamp and the mountain into Box 2
box[2].extend(['toothpaste', 'lamp', 'mountain'])

# Put the island into Box 11
box[11].append('island')

# Remove the wire from Box 12
box[12].remove('wire')

# Move the submarine from Box 7 to Box 6
box[7].remove('submarine')
box[6].append('submarine')

# Move the helmet from Box 0 to Box 7
box[0].remove('helmet')
box[7].append('helmet')

# Replace the puzzle and the cat with the keyboard and the guitar in Box 1
box[1].remove('puzzle')
box[1].remove('cat')
box[1].extend(['keyboard', 'guitar'])

# Replace the octopus and the blanket and the key with the towel and the sandals and the rain in Box 5
box[5].remove('octopus')
box[5].remove('blanket')
box[5].remove('key')
box[5].extend(['towel', 'sandals', 'rain'])

# Move the perfume and the branch from Box 9 to Box 6
box[9].remove('perfume')
box[9].remove('branch')
box[6].extend(['perfume', 'branch'])

# Put the shampoo and the tiger into Box 5
box[5].extend(['shampoo', 'tiger'])

# Remove the rocket and the sun and the violin from Box 10
box[10].remove('rocket')
box[10].remove('sun')
box[10].remove('violin')

# Swap the keyboard in Box 1 with the tiger in Box 5
box[1].remove('keyboard')
box[5].remove('tiger')
box[1].append('tiger')
box[5].append('keyboard')

# Remove the coin and the skirt and the dress from Box 4
box[4].remove('coin')
box[4].remove('skirt')
box[4].remove('dress')

# Swap the branch in Box 6 with the book in Box 11
box[6].remove('branch')
box[11].remove('book')
box[6].append('book')
box[11].append('branch')

# Swap the wallet in Box 10 with the submarine in Box 6
box[10].remove('wallet')
box[6].remove('submarine')
box[10].append('submarine')
box[6].append('wallet')

# Swap the bicycle in Box 4 with the shelf in Box 13
box[4].remove('bicycle')
box[13].remove('shelf')
box[4].append('shelf')
box[13].append('bicycle')

# Put the bear and the planet into Box 0
box[0].extend(['bear', 'planet'])

# Remove the mountain and the lamp and the toothpaste from Box 2
box[2].remove('mountain')
box[2].remove('lamp')
box[2].remove('toothpaste')

# Remove the branch and the island from Box 11
box[11].remove('branch')
box[11].remove('island')

# Remove the toaster and the wallet from Box 6
box[6].remove('toaster')
box[6].remove('wallet')

# Print the contents of each box
for i in range(14):
    print(f"Box {i}: {box[i]}")