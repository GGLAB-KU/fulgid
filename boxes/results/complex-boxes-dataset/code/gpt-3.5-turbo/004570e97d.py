# Initial state of boxes
boxes = {
    0: ['flute', 'speaker', 'blanket', 'butterfly', 'paint'],
    1: ['sun', 'lion', 'shoes', 'submarine', 'oven'],
    2: ['swimsuit', 'pan', 'whistle', 'thread', 'vase'],
    3: ['bowl', 'clock', 'pot', 'dolphin'],
    4: ['makeup', 'leaf'],
    5: ['perfume', 'puzzle', 'soap', 'glasses'],
    6: ['moon'],
    7: ['console', 'glove', 'shirt', 'snow', 'bell'],
    8: ['comb', 'sock'],
    9: ['toothpaste'],
    10: ['doll', 'shark'],
    11: ['charger']
}

# Put the shampoo and the bag and the shorts into Box 11.
boxes[11].extend(['shampoo', 'bag', 'shorts'])

# Swap the leaf in Box 4 with the vase in Box 2.
boxes[4].remove('leaf')
boxes[2].remove('vase')
boxes[4].append('vase')
boxes[2].append('leaf')

# Swap the toothpaste in Box 9 with the moon in Box 6.
boxes[9].remove('toothpaste')
boxes[6].remove('moon')
boxes[9].append('moon')
boxes[6].append('toothpaste')

# Move the bag from Box 11 to Box 2.
boxes[11].remove('bag')
boxes[2].append('bag')

# Empty Box 6.
boxes[6] = []

# Remove the charger and the shampoo and the shorts from Box 11.
items_to_remove = ['charger', 'shampoo', 'shorts']
for item in items_to_remove:
    boxes[11].remove(item)

# Empty Box 3.
boxes[3] = []

# Move the moon from Box 9 to Box 5.
boxes[9].remove('moon')
boxes[5].append('moon')

# Move the whistle from Box 2 to Box 6.
boxes[2].remove('whistle')
boxes[6].append('whistle')

# Put the sandals into Box 5.
boxes[5].append('sandals')

# Replace the glasses and the perfume with the keyboard and the car in Box 5.
boxes[5].remove('glasses')
boxes[5].remove('perfume')
boxes[5].append('keyboard')
boxes[5].append('car')

# Put the keyboard and the beach and the flute into Box 4.
boxes[4].extend(['keyboard', 'beach', 'flute'])

# Move the flute from Box 0 to Box 6.
boxes[0].remove('flute')
boxes[6].append('flute')

# Replace the butterfly with the tiger in Box 0.
boxes[0].remove('butterfly')
boxes[0].append('tiger')

# Put the sandals and the perfume and the snow into Box 2.
boxes[2].extend(['sandals', 'perfume', 'snow'])

# Put the flower and the microscope into Box 6.
boxes[6].extend(['flower', 'microscope'])

# Replace the tiger and the blanket with the truck and the zipper in Box 0.
boxes[0].remove('tiger')
boxes[0].remove('blanket')
boxes[0].append('truck')
boxes[0].append('zipper')

# Put the puzzle and the bowl into Box 5.
boxes[5].extend(['puzzle', 'bowl'])

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")