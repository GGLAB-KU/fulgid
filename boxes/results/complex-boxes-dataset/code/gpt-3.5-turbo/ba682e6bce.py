# Initial state of boxes
boxes = {
    0: ['lock', 'crown'],
    1: ['shark'],
    2: [],
    3: [],
    4: ['keyboard', 'pan', 'skirt', 'apple'],
    5: ['car', 'blanket', 'plane', 'bowl'],
    6: ['moon', 'hat', 'fridge', 'sun', 'console'],
    7: ['gloves', 'mountain', 'cat', 'cup', 'phone'],
    8: ['wig', 'mask', 'meteor', 'soap'],
    9: ['flower', 'octopus', 'rain', 'chair'],
    10: ['bear']
}

# Remove the shark from Box 1.
boxes[1].remove('shark')

# Remove the flower from Box 9.
boxes[9].remove('flower')

# Move the fridge and the moon from Box 6 to Box 10.
boxes[6].remove('fridge')
boxes[6].remove('moon')
boxes[10].append('fridge')
boxes[10].append('moon')

# Move the crown and the lock from Box 0 to Box 5.
boxes[0].remove('crown')
boxes[0].remove('lock')
boxes[5].append('crown')
boxes[5].append('lock')

# Move the fridge from Box 10 to Box 0.
boxes[10].remove('fridge')
boxes[0].append('fridge')

# Move the fridge from Box 0 to Box 2.
boxes[0].remove('fridge')
boxes[2].append('fridge')

# Empty Box 5.
boxes[5] = []

# Put the bell and the sun and the earring into Box 3.
boxes[3].append('bell')
boxes[3].append('sun')
boxes[3].append('earring')

# Put the bracelet and the bird into Box 6.
boxes[6].append('bracelet')
boxes[6].append('bird')

# Put the toy into Box 6.
boxes[6].append('toy')

# Move the mask and the meteor and the soap from Box 8 to Box 1.
boxes[8].remove('mask')
boxes[8].remove('meteor')
boxes[8].remove('soap')
boxes[1].append('mask')
boxes[1].append('meteor')
boxes[1].append('soap')

# Replace the bell and the earring with the bus and the comb in Box 3.
boxes[3].remove('bell')
boxes[3].remove('earring')
boxes[3].append('bus')
boxes[3].append('comb')

# Put the fridge and the flute into Box 8.
boxes[8].append('fridge')
boxes[8].append('flute')

# Remove the pan from Box 4.
boxes[4].remove('pan')

# Put the gloves and the flute into Box 7.
boxes[7].append('gloves')
boxes[7].append('flute')

# Remove the chair and the octopus and the rain from Box 9.
boxes[9].remove('chair')
boxes[9].remove('octopus')
boxes[9].remove('rain')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")