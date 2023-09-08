# Initial state of boxes
boxes = {
    0: ['star'],
    1: [],
    2: [],
    3: ['horse', 'shoes', 'ship', 'wallet'],
    4: ['bell', 'zipper'],
    5: ['forest', 'rain', 'polish', 'thunder', 'hat'],
    6: ['harmonica', 'pen', 'oven', 'clock'],
    7: ['violin', 'puzzle', 'fridge', 'shirt', 'bag'],
    8: ['pan', 'towel', 'tiger', 'freezer'],
    9: ['tree', 'makeup', 'gloves'],
    10: [],
    11: ['thread', 'dress', 'cloud'],
    12: ['game', 'comb', 'magnet']
}

# Put the lion and the shoe into Box 9.
boxes[9].append('lion')
boxes[9].append('shoe')

# Swap the comb in Box 12 with the star in Box 0.
boxes[0].remove('star')
boxes[12].remove('comb')
boxes[0].append('comb')
boxes[12].append('star')

# Put the star and the seaweed into Box 2.
boxes[2].append('star')
boxes[2].append('seaweed')

# Replace the lion and the shoe with the necklace and the starfish in Box 9.
boxes[9].remove('lion')
boxes[9].remove('shoe')
boxes[9].append('necklace')
boxes[9].append('starfish')

# Put the violin and the leaf and the harmonica into Box 12.
boxes[12].append('violin')
boxes[12].append('leaf')
boxes[12].append('harmonica')

# Remove the polish and the forest and the hat from Box 5.
boxes[5].remove('polish')
boxes[5].remove('forest')
boxes[5].remove('hat')

# Put the butterfly and the forest and the tree into Box 0.
boxes[0].append('butterfly')
boxes[0].append('forest')
boxes[0].append('tree')

# Put the glasses into Box 0.
boxes[0].append('glasses')

# Remove the bell from Box 4.
boxes[4].remove('bell')

# Empty Box 4.
boxes[4] = []

# Replace the star with the belt in Box 2.
boxes[2].remove('star')
boxes[2].append('belt')

# Replace the pan and the freezer with the submarine and the forest in Box 8.
boxes[8].remove('pan')
boxes[8].remove('freezer')
boxes[8].append('submarine')
boxes[8].append('forest')

# Empty Box 3.
boxes[3] = []

# Swap the shirt in Box 7 with the butterfly in Box 0.
boxes[0].remove('butterfly')
boxes[7].remove('shirt')
boxes[0].append('shirt')
boxes[7].append('butterfly')

# Swap the tree in Box 9 with the rain in Box 5.
boxes[5].remove('rain')
boxes[9].remove('tree')
boxes[5].append('tree')
boxes[9].append('rain')

# Put the skirt and the pen and the battery into Box 2.
boxes[2].append('skirt')
boxes[2].append('pen')
boxes[2].append('battery')

# Swap the seaweed in Box 2 with the submarine in Box 8.
boxes[2].remove('seaweed')
boxes[8].remove('submarine')
boxes[2].append('submarine')
boxes[8].append('seaweed')

# Replace the submarine and the skirt with the plate and the shorts in Box 2.
boxes[2].remove('submarine')
boxes[2].remove('skirt')
boxes[2].append('plate')
boxes[2].append('shorts')

# Replace the thunder with the sculpture in Box 5.
boxes[5].remove('thunder')
boxes[5].append('sculpture')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")