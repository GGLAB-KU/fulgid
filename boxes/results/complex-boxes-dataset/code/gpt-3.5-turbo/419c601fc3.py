# Initial state of boxes
boxes = {
    0: ['snow'],
    1: ['meteor', 'plate', 'glove', 'bear'],
    2: ['starfish', 'island', 'comet', 'paint', 'bracelet'],
    3: ['fork', 'bag', 'gloves', 'watch'],
    4: ['shirt', 'tie', 'earring', 'tree', 'wig'],
    5: [],
    6: ['star', 'car'],
    7: ['perfume'],
    8: ['bus', 'shampoo', 'submarine', 'chair'],
    9: ['coat'],
    10: [],
    11: ['vase', 'table'],
    12: ['pants', 'storm']
}

# Replace the tree and the earring and the shirt with the flower and the lipstick and the soap in Box 4.
boxes[4].remove('tree')
boxes[4].remove('earring')
boxes[4].remove('shirt')
boxes[4].append('flower')
boxes[4].append('lipstick')
boxes[4].append('soap')

# Swap the perfume in Box 7 with the table in Box 11.
boxes[7], boxes[11] = boxes[11], boxes[7]

# Swap the vase in Box 11 with the storm in Box 12.
boxes[11], boxes[12] = boxes[12], boxes[11]

# Empty Box 11.
boxes[11] = []

# Replace the vase and the pants with the whistle and the mixer in Box 12.
boxes[12].remove('vase')
boxes[12].remove('pants')
boxes[12].append('whistle')
boxes[12].append('mixer')

# Move the gloves from Box 3 to Box 5.
boxes[3].remove('gloves')
boxes[5].append('gloves')

# Move the bracelet and the starfish from Box 2 to Box 4.
boxes[2].remove('bracelet')
boxes[2].remove('starfish')
boxes[4].append('bracelet')
boxes[4].append('starfish')

# Put the rock and the paint and the freezer into Box 9.
boxes[9].extend(['rock', 'paint', 'freezer'])

# Remove the freezer and the rock and the paint from Box 9.
boxes[9].remove('freezer')
boxes[9].remove('rock')
boxes[9].remove('paint')

# Remove the starfish and the wig and the bracelet from Box 4.
boxes[4].remove('starfish')
boxes[4].remove('wig')
boxes[4].remove('bracelet')

# Put the wig and the pot and the mask into Box 10.
boxes[10].extend(['wig', 'pot', 'mask'])

# Move the table from Box 7 to Box 3.
boxes[7].remove('table')
boxes[3].append('table')

# Put the necklace and the camera and the bicycle into Box 0.
boxes[0].extend(['necklace', 'camera', 'bicycle'])

# Remove the whistle from Box 12.
boxes[12].remove('whistle')

# Move the meteor and the glove from Box 1 to Box 5.
boxes[1].remove('meteor')
boxes[1].remove('glove')
boxes[5].extend(['meteor', 'glove'])

# Remove the glove and the meteor and the gloves from Box 5.
boxes[5].remove('glove')
boxes[5].remove('meteor')
boxes[5].remove('gloves')

# Move the submarine and the chair from Box 8 to Box 5.
boxes[8].remove('submarine')
boxes[8].remove('chair')
boxes[5].extend(['submarine', 'chair'])

# Put the cat into Box 0.
boxes[0].append('cat')

# Empty Box 5.
boxes[5] = []

# Empty Box 0.
boxes[0] = []

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")