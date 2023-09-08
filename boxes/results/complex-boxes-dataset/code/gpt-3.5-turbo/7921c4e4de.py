# Initial state of boxes
boxes = {
    0: [],
    1: ['dolphin', 'telescope', 'mixer'],
    2: ['pan', 'ring', 'blanket'],
    3: [],
    4: ['chair', 'camera'],
    5: ['moon', 'plate', 'key', 'bag'],
    6: ['earring', 'piano', 'toaster', 'tree', 'keyboard'],
    7: ['comb'],
    8: ['charger', 'bicycle', 'skirt', 'toothpaste'],
    9: ['planet', 'comet', 'coin'],
    10: ['forest', 'magnet'],
    11: [],
    12: ['wire', 'meteor', 'blender', 'flute', 'starfish']
}

# Move the bag and the moon from Box 5 to Box 9.
items_to_move = ['bag', 'moon']
for item in items_to_move:
    boxes[5].remove(item)
    boxes[9].append(item)

# Put the chair and the harmonica into Box 10.
items_to_move = ['chair', 'harmonica']
for item in items_to_move:
    boxes[4].remove(item)
    boxes[10].append(item)

# Move the bicycle and the charger from Box 8 to Box 7.
items_to_move = ['bicycle', 'charger']
for item in items_to_move:
    boxes[8].remove(item)
    boxes[7].append(item)

# Swap the flute in Box 12 with the chair in Box 4.
boxes[12].remove('flute')
boxes[4].remove('chair')
boxes[12].append('chair')
boxes[4].append('flute')

# Move the pan from Box 2 to Box 7.
boxes[2].remove('pan')
boxes[7].append('pan')

# Move the blender and the wire and the meteor from Box 12 to Box 6.
items_to_move = ['blender', 'wire', 'meteor']
for item in items_to_move:
    boxes[12].remove(item)
    boxes[6].append(item)

# Remove the starfish and the chair from Box 12.
items_to_remove = ['starfish', 'chair']
for item in items_to_remove:
    boxes[12].remove(item)

# Move the keyboard and the meteor and the piano from Box 6 to Box 8.
items_to_move = ['keyboard', 'meteor', 'piano']
for item in items_to_move:
    boxes[6].remove(item)
    boxes[8].append(item)

# Remove the comb and the pan from Box 7.
items_to_remove = ['comb', 'pan']
for item in items_to_remove:
    boxes[7].remove(item)

# Put the cup and the butterfly and the mask into Box 7.
items_to_move = ['cup', 'butterfly', 'mask']
for item in items_to_move:
    boxes[7].append(item)

# Move the bicycle from Box 7 to Box 6.
boxes[7].remove('bicycle')
boxes[6].append('bicycle')

# Remove the chair and the magnet from Box 10.
items_to_remove = ['chair', 'magnet']
for item in items_to_remove:
    boxes[10].remove(item)

# Put the coin and the glasses into Box 7.
items_to_move = ['coin', 'glasses']
for item in items_to_move:
    boxes[7].append(item)

# Swap the planet in Box 9 with the flute in Box 4.
boxes[9].remove('planet')
boxes[4].remove('flute')
boxes[9].append('flute')
boxes[4].append('planet')

# Empty Box 9.
boxes[9] = []

# Remove the ring and the blanket from Box 2.
items_to_remove = ['ring', 'blanket']
for item in items_to_remove:
    boxes[2].remove(item)

# Move the piano from Box 8 to Box 11.
boxes[8].remove('piano')
boxes[11].append('piano')

# Replace the plate with the river in Box 5.
boxes[5].remove('plate')
boxes[5].append('river')

# Empty Box 4.
boxes[4] = []

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")