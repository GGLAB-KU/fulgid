box = {
    0: [],
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

def print_box_contents():
    for index, items in box.items():
        print(f"Box {index}: {items}")

# Put the lion and the shoe into Box 9
box[9] = ['lion', 'shoe']

# Swap the comb in Box 12 with the star in Box 0
box[0], box[12] = box[12], box[0]

# Put the star and the seaweed into Box 2
box[2] = ['star', 'seaweed']

# Replace the lion and the shoe with the necklace and the starfish in Box 9
box[9] = ['necklace', 'starfish']

# Put the violin and the leaf and the harmonica into Box 12
box[12] += ['violin', 'leaf', 'harmonica']

# Remove the polish and the forest and the hat from Box 5
box[5] = []

# Put the butterfly and the forest and the tree into Box 0
box[0] = ['butterfly', 'forest', 'tree']

# Put the glasses into Box 0
box[0].append('glasses')

# Remove the bell from Box 4
box[4] = []

# Empty Box 4
box[4] = []

# Replace the star with the belt in Box 2
box[2] = ['belt']

# Replace the pan and the freezer with the submarine and the forest in Box 8
box[8] = ['submarine', 'forest']

# Empty Box 3
box[3] = []

# Swap the shirt in Box 7 with the butterfly in Box 0
box[0], box[7] = box[7], box[0]

# Swap the tree in Box 9 with the rain in Box 5
box[5], box[9] = box[9], box[5]

# Put the skirt and the pen and the battery into Box 2
box[2] += ['skirt', 'pen', 'battery']

# Swap the seaweed in Box 2 with the submarine in Box 8
box[2], box[8] = box[8], box[2]

# Replace the submarine and the skirt with the plate and the shorts in Box 2
box[2] = ['plate', 'shorts']

# Replace the thunder with the sculpture in Box 5
box[5] = ['sculpture']

print_box_contents()