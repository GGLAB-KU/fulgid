box = {
    0: ['table', 'plate'],
    1: [],
    2: ['coin', 'laptop', 'ring', 'button', 'zipper'],
    3: ['comb'],
    4: ['puzzle', 'basket', 'drum', 'pants', 'rocket'],
    5: [],
    6: ['ocean', 'flute'],
    7: ['toy'],
    8: [],
    9: ['hat', 'toothpaste', 'harmonica', 'speaker', 'umbrella'],
    10: [],
    11: ['island', 'battery']
}

# Replace the ocean and the flute with the tape and the storm in Box 6
box[6] = ['tape', 'storm']

# Replace the tape and the storm with the necklace and the magnet in Box 6
box[6] = ['necklace', 'magnet']

# Put the pillow and the bag and the submarine into Box 6
box[6].extend(['pillow', 'bag', 'submarine'])

# Move the table and the plate from Box 0 to Box 5
box[5].extend(box[0])
box[0] = []

# Empty Box 11
box[11] = []

# Remove the coin from Box 2
box[2].remove('coin')

# Empty Box 4
box[4] = []

# Put the battery and the paint and the boat into Box 11
box[11].extend(['battery', 'paint', 'boat'])

# Move the button from Box 2 to Box 7
box[7].append(box[2].pop(box[2].index('button')))

# Move the speaker from Box 9 to Box 2
box[2].append(box[9].pop(box[9].index('speaker')))

# Remove the magnet and the pillow from Box 6
box[6].remove('magnet')
box[6].remove('pillow')

# Move the umbrella from Box 9 to Box 11
box[11].append(box[9].pop(box[9].index('umbrella')))

# Replace the necklace with the guitar in Box 6
box[6].remove('necklace')
box[6].append('guitar')

# Move the toy and the button from Box 7 to Box 8
box[8].extend([box[7].pop(box[7].index('toy')), box[7].pop(box[7].index('button'))])

# Remove the ring from Box 2
box[2].remove('ring')

# Move the speaker and the zipper from Box 2 to Box 0
box[0].extend([box[2].pop(box[2].index('speaker')), box[2].pop(box[2].index('zipper'))])

# Move the laptop from Box 2 to Box 8
box[8].append(box[2].pop(box[2].index('laptop')))

# Move the plate and the table from Box 5 to Box 0
box[0].extend(box[5])
box[5] = []

# Print the contents of each box
for i in range(12):
    print(f"Box {i}: {box[i]}")