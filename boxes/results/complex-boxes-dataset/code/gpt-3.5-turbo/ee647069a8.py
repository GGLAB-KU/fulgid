# Initial state of boxes
boxes = {
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

# Replace the ocean and the flute with the tape and the storm in Box 6.
boxes[6].remove('ocean')
boxes[6].remove('flute')
boxes[6].append('tape')
boxes[6].append('storm')

# Replace the tape and the storm with the necklace and the magnet in Box 6.
boxes[6].remove('tape')
boxes[6].remove('storm')
boxes[6].append('necklace')
boxes[6].append('magnet')

# Put the pillow and the bag and the submarine into Box 6.
boxes[6].extend(['pillow', 'bag', 'submarine'])

# Move the table and the plate from Box 0 to Box 5.
items_to_move = ['table', 'plate']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[5].append(item)

# Empty Box 11.
boxes[11] = []

# Remove the coin from Box 2.
boxes[2].remove('coin')

# Empty Box 4.
boxes[4] = []

# Put the battery and the paint and the boat into Box 11.
boxes[11].extend(['battery', 'paint', 'boat'])

# Move the button from Box 2 to Box 7.
boxes[2].remove('button')
boxes[7].append('button')

# Move the speaker from Box 9 to Box 2.
boxes[9].remove('speaker')
boxes[2].append('speaker')

# Remove the magnet and the pillow from Box 6.
boxes[6].remove('magnet')
boxes[6].remove('pillow')

# Move the umbrella from Box 9 to Box 11.
boxes[9].remove('umbrella')
boxes[11].append('umbrella')

# Replace the necklace with the guitar in Box 6.
boxes[6].remove('necklace')
boxes[6].append('guitar')

# Move the toy and the button from Box 7 to Box 8.
boxes[7].remove('toy')
boxes[7].remove('button')
boxes[8].extend(['toy', 'button'])

# Remove the ring from Box 2.
boxes[2].remove('ring')

# Move the speaker and the zipper from Box 2 to Box 0.
boxes[2].remove('speaker')
boxes[2].remove('zipper')
boxes[0].extend(['speaker', 'zipper'])

# Move the laptop from Box 2 to Box 8.
boxes[2].remove('laptop')
boxes[8].append('laptop')

# Move the plate and the table from Box 5 to Box 0.
boxes[5].remove('plate')
boxes[5].remove('table')
boxes[0].extend(['plate', 'table'])

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")