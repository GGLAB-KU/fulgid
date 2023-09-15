box = {
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

def print_box_contents():
    for index, items in box.items():
        print(f"Box {index}: {items}")

def move_item(source_box, item, destination_box):
    if item in box[source_box]:
        box[source_box].remove(item)
        box[destination_box].append(item)

def swap_items(box1, item1, box2, item2):
    if item1 in box[box1] and item2 in box[box2]:
        box[box1].remove(item1)
        box[box2].remove(item2)
        box[box1].append(item2)
        box[box2].append(item1)

# Put the shampoo into Box 10
box[10].append('shampoo')

# Swap the coin in Box 11 with the wallet in Box 3
swap_items(11, 'coin', 3, 'wallet')

# Move the grass from Box 12 to Box 10
move_item(12, 'grass', 10)

# Put the violin and the spoon and the submarine into Box 4
box[4].extend(['violin', 'spoon', 'submarine'])

# Remove the wire and the meteor and the shoes from Box 9
box[9].remove('wire')
box[9].remove('meteor')
box[9].remove('shoes')

# Put the shoe and the seaweed into Box 5
box[5].extend(['shoe', 'seaweed'])

# Put the umbrella into Box 10
box[10].append('umbrella')

# Move the thunder from Box 9 to Box 11
move_item(9, 'thunder', 11)

# Move the flower and the star from Box 2 to Box 9
move_item(2, 'flower', 9)
move_item(2, 'star', 9)

# Replace the bell with the cup in Box 11
swap_items(11, 'bell', 11, 'cup')

# Replace the coin with the lion in Box 3
swap_items(3, 'coin', 3, 'lion')

# Move the brush and the lion from Box 3 to Box 5
move_item(3, 'brush', 5)
move_item(3, 'lion', 5)

# Remove the shirt and the seaweed from Box 0
box[0].remove('shirt')
box[0].remove('seaweed')

# Remove the star and the flower and the earring from Box 9
box[9].remove('star')
box[9].remove('flower')
box[9].remove('earring')

# Put the rocket and the harmonica into Box 10
box[10].extend(['rocket', 'harmonica'])

# Move the chair from Box 2 to Box 7
move_item(2, 'chair', 7)

# Swap the rocket in Box 10 with the cup in Box 11
swap_items(10, 'rocket', 11, 'cup')

# Swap the moon in Box 4 with the sculpture in Box 12
swap_items(4, 'moon', 12, 'sculpture')

# Move the moon and the boot from Box 12 to Box 7
move_item(12, 'moon', 7)
move_item(12, 'boot', 7)

# Put the battery and the microwave into Box 5
box[5].extend(['battery', 'microwave'])

# Replace the harmonica and the grass and the umbrella with the magnet and the forest and the swimsuit in Box 10
box[10].remove('harmonica')
box[10].remove('grass')
box[10].remove('umbrella')
box[10].extend(['magnet', 'forest', 'swimsuit'])

# Print the contents of each box
print_box_contents()