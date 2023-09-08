# Initial state of boxes
boxes = {
    0: [],
    1: ['earring', 'sock', 'coin'],
    2: ['mixer', 'shoe', 'tape', 'thunder', 'bell'],
    3: ['horse'],
    4: ['bear', 'snow'],
    5: [],
    6: ['puzzle', 'helmet', 'desert'],
    7: ['fish', 'lipstick', 'dog', 'skirt'],
    8: ['book', 'scarf'],
    9: ['plane', 'basket', 'moon', 'flute']
}

# Put the telescope and the shorts and the submarine into Box 6.
boxes[6].append('telescope')
boxes[6].append('shorts')
boxes[6].append('submarine')

# Move the scarf and the book from Box 8 to Box 5.
boxes[8].remove('scarf')
boxes[8].remove('book')
boxes[5].append('scarf')
boxes[5].append('book')

# Replace the skirt and the lipstick with the ring and the branch in Box 7.
boxes[7].remove('skirt')
boxes[7].remove('lipstick')
boxes[7].append('ring')
boxes[7].append('branch')

# Move the mixer and the tape and the shoe from Box 2 to Box 5.
items_to_move = ['mixer', 'tape', 'shoe']
for item in items_to_move:
    boxes[2].remove(item)
    boxes[5].append(item)

# Remove the scarf and the shoe from Box 5.
boxes[5].remove('scarf')
boxes[5].remove('shoe')

# Move the sock and the coin and the earring from Box 1 to Box 7.
items_to_move = ['sock', 'coin', 'earring']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[7].append(item)

# Replace the snow and the bear with the doll and the toaster in Box 4.
boxes[4].remove('snow')
boxes[4].remove('bear')
boxes[4].append('doll')
boxes[4].append('toaster')

# Remove the toaster from Box 4.
boxes[4].remove('toaster')

# Put the console into Box 1.
boxes[1].append('console')

# Swap the moon in Box 9 with the horse in Box 3.
boxes[9].remove('moon')
boxes[3].remove('horse')
boxes[9].append('horse')
boxes[3].append('moon')

# Replace the console with the jungle in Box 1.
boxes[1].remove('console')
boxes[1].append('jungle')

# Move the jungle from Box 1 to Box 4.
boxes[1].remove('jungle')
boxes[4].append('jungle')

# Replace the puzzle and the helmet and the desert with the drum and the shoes and the sock in Box 6.
boxes[6].remove('puzzle')
boxes[6].remove('helmet')
boxes[6].remove('desert')
boxes[6].append('drum')
boxes[6].append('shoes')
boxes[6].append('sock')

# Move the doll from Box 4 to Box 6.
boxes[4].remove('doll')
boxes[6].append('doll')

# Replace the flute and the plane and the basket with the apple and the violin and the mixer in Box 9.
boxes[9].remove('flute')
boxes[9].remove('plane')
boxes[9].remove('basket')
boxes[9].append('apple')
boxes[9].append('violin')
boxes[9].append('mixer')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")