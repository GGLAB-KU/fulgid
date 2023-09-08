# Initial state of boxes
boxes = {
    0: ['shirt', 'seaweed'],
    1: ['truck', 'dolphin', 'headphone'],
    2: ['star', 'chair', 'flower'],
    3: ['brush', 'wallet'],
    4: ['umbrella', 'usb', 'plate', 'ship', 'moon'],
    5: ['makeup'],
    6: [],
    7: ['towel', 'tie', 'glove', 'mask'],
    8: [],
    9: ['wire', 'shoes', 'thunder', 'meteor', 'earring'],
    10: [],
    11: ['coin', 'bell'],
    12: ['boot', 'sculpture', 'thread', 'grass'],
    13: []
}

# Put the shampoo into Box 10.
boxes[10].append('shampoo')

# Swap the coin in Box 11 with the wallet in Box 3.
boxes[11].remove('coin')
boxes[3].remove('wallet')
boxes[11].append('wallet')
boxes[3].append('coin')

# Move the grass from Box 12 to Box 10.
boxes[12].remove('grass')
boxes[10].append('grass')

# Put the violin and the spoon and the submarine into Box 4.
items_to_move = ['violin', 'spoon', 'submarine']
for item in items_to_move:
    boxes[4].append(item)

# Remove the wire and the meteor and the shoes from Box 9.
items_to_remove = ['wire', 'meteor', 'shoes']
for item in items_to_remove:
    boxes[9].remove(item)

# Put the shoe and the seaweed into Box 5.
items_to_move = ['shoe', 'seaweed']
for item in items_to_move:
    boxes[5].append(item)

# Put the umbrella into Box 10.
boxes[10].append('umbrella')

# Move the thunder from Box 9 to Box 11.
boxes[9].remove('thunder')
boxes[11].append('thunder')

# Move the flower and the star from Box 2 to Box 9.
items_to_move = ['flower', 'star']
for item in items_to_move:
    boxes[2].remove(item)
    boxes[9].append(item)

# Replace the bell with the cup in Box 11.
boxes[11].remove('bell')
boxes[11].append('cup')

# Replace the coin with the lion in Box 3.
boxes[3].remove('coin')
boxes[3].append('lion')

# Move the brush and the lion from Box 3 to Box 5.
items_to_move = ['brush', 'lion']
for item in items_to_move:
    boxes[3].remove(item)
    boxes[5].append(item)

# Remove the shirt and the seaweed from Box 0.
items_to_remove = ['shirt', 'seaweed']
for item in items_to_remove:
    boxes[0].remove(item)

# Remove the star and the flower and the earring from Box 9.
items_to_remove = ['star', 'flower', 'earring']
for item in items_to_remove:
    boxes[9].remove(item)

# Put the rocket and the harmonica into Box 10.
items_to_move = ['rocket', 'harmonica']
for item in items_to_move:
    boxes[10].append(item)

# Move the chair from Box 2 to Box 7.
boxes[2].remove('chair')
boxes[7].append('chair')

# Swap the rocket in Box 10 with the cup in Box 11.
boxes[10].remove('rocket')
boxes[11].remove('cup')
boxes[10].append('cup')
boxes[11].append('rocket')

# Swap the moon in Box 4 with the sculpture in Box 12.
boxes[4].remove('moon')
boxes[12].remove('sculpture')
boxes[4].append('sculpture')
boxes[12].append('moon')

# Move the moon and the boot from Box 12 to Box 7.
items_to_move = ['moon', 'boot']
for item in items_to_move:
    boxes[12].remove(item)
    boxes[7].append(item)

# Put the battery and the microwave into Box 5.
items_to_move = ['battery', 'microwave']
for item in items_to_move:
    boxes[5].append(item)

# Replace the harmonica and the grass and the umbrella with the magnet and the forest and the swimsuit in Box 10.
items_to_remove = ['harmonica', 'grass', 'umbrella']
items_to_add = ['magnet', 'forest', 'swimsuit']
for item in items_to_remove:
    boxes[10].remove(item)
for item in items_to_add:
    boxes[10].append(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")