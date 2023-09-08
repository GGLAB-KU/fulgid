# Initial state of boxes
boxes = {
    0: ['button', 'scissors', 'blender'],
    1: ['polish', 'cat'],
    2: ['horn', 'guitar'],
    3: ['shelf'],
    4: ['seaweed', 'leaf', 'necklace'],
    5: [],
    6: ['mountain'],
    7: ['coin', 'camera', 'cow', 'sun', 'fridge'],
    8: ['snow', 'branch', 'rain', 'wire', 'speaker'],
    9: ['gloves', 'ocean', 'pot'],
    10: ['storm', 'sandals']
}

# Swap the blender in Box 0 with the sandals in Box 10.
boxes[0].remove('blender')
boxes[10].remove('sandals')
boxes[0].append('sandals')
boxes[10].append('blender')

# Move the blender from Box 10 to Box 8.
boxes[10].remove('blender')
boxes[8].append('blender')

# Swap the cow in Box 7 with the mountain in Box 6.
boxes[7].remove('cow')
boxes[6].remove('mountain')
boxes[7].append('mountain')
boxes[6].append('cow')

# Put the dog and the butterfly and the grinder into Box 6.
items_to_move = ['dog', 'butterfly', 'grinder']
for item in items_to_move:
    boxes[6].append(item)

# Put the perfume into Box 2.
boxes[2].append('perfume')

# Put the fridge and the coral and the shorts into Box 5.
items_to_move = ['fridge', 'coral', 'shorts']
for item in items_to_move:
    boxes[5].append(item)

# Replace the blender and the wire and the speaker with the necklace and the coin and the starfish in Box 8.
boxes[8].remove('blender')
boxes[8].remove('wire')
boxes[8].remove('speaker')
boxes[8].append('necklace')
boxes[8].append('coin')
boxes[8].append('starfish')

# Swap the perfume in Box 2 with the fridge in Box 7.
boxes[2].remove('perfume')
boxes[7].remove('fridge')
boxes[2].append('fridge')
boxes[7].append('perfume')

# Replace the storm with the violin in Box 10.
boxes[10].remove('storm')
boxes[10].append('violin')

# Put the freezer into Box 9.
boxes[9].append('freezer')

# Remove the branch and the starfish and the necklace from Box 8.
items_to_remove = ['branch', 'starfish', 'necklace']
for item in items_to_remove:
    boxes[8].remove(item)

# Remove the polish and the cat from Box 1.
boxes[1].remove('polish')
boxes[1].remove('cat')

# Swap the gloves in Box 9 with the grinder in Box 6.
boxes[9].remove('gloves')
boxes[6].remove('grinder')
boxes[9].append('grinder')
boxes[6].append('gloves')

# Put the wallet into Box 4.
boxes[4].append('wallet')

# Put the wire and the moon into Box 5.
items_to_move = ['wire', 'moon']
for item in items_to_move:
    boxes[5].append(item)

# Empty Box 6.
boxes[6] = []

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")