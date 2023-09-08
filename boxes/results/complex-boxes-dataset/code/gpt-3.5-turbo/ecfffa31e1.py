# Initial state of boxes
boxes = {
    0: ['mask', 'cat'],
    1: ['coat', 'lion', 'violin', 'moon'],
    2: [],
    3: ['watch', 'book', 'harmonica', 'soap', 'brush'],
    4: ['tie', 'chair', 'doll', 'freezer'],
    5: ['earring', 'thread', 'dice'],
    6: [],
    7: ['storm'],
    8: ['wig'],
    9: ['necklace'],
    10: ['ring', 'forest', 'bear', 'jacket'],
    11: ['shorts', 'planet'],
    12: ['oven'],
    13: ['magnet', 'hat', 'grinder', 'toy', 'paint']
}

# Put the guitar and the drum and the pants into Box 10.
items_to_put = ['guitar', 'drum', 'pants']
for item in items_to_put:
    boxes[10].append(item)

# Put the magnet and the sun into Box 1.
items_to_put = ['magnet', 'sun']
for item in items_to_put:
    boxes[1].append(item)

# Put the tie and the storm and the umbrella into Box 2.
items_to_put = ['tie', 'storm', 'umbrella']
for item in items_to_put:
    boxes[2].append(item)

# Move the brush from Box 3 to Box 10.
boxes[3].remove('brush')
boxes[10].append('brush')

# Replace the umbrella and the tie with the camera and the usb in Box 2.
boxes[2].remove('umbrella')
boxes[2].remove('tie')
boxes[2].append('camera')
boxes[2].append('usb')

# Replace the cat with the wig in Box 0.
boxes[0].remove('cat')
boxes[0].append('wig')

# Swap the brush in Box 10 with the doll in Box 4.
boxes[10].remove('brush')
boxes[4].remove('doll')
boxes[10].append('doll')
boxes[4].append('brush')

# Put the chair and the keyboard into Box 8.
items_to_put = ['chair', 'keyboard']
for item in items_to_put:
    boxes[8].append(item)

# Move the guitar from Box 10 to Box 8.
boxes[10].remove('guitar')
boxes[8].append('guitar')

# Move the chair from Box 8 to Box 1.
boxes[8].remove('chair')
boxes[1].append('chair')

# Swap the tie in Box 4 with the camera in Box 2.
boxes[4].remove('tie')
boxes[2].remove('camera')
boxes[4].append('camera')
boxes[2].append('tie')

# Move the necklace from Box 9 to Box 10.
boxes[9].remove('necklace')
boxes[10].append('necklace')

# Remove the tie and the usb from Box 2.
boxes[2].remove('tie')
boxes[2].remove('usb')

# Move the violin and the moon and the coat from Box 1 to Box 5.
items_to_move = ['violin', 'moon', 'coat']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[5].append(item)

# Replace the oven with the cow in Box 12.
boxes[12].remove('oven')
boxes[12].append('cow')

# Swap the soap in Box 3 with the cow in Box 12.
boxes[3].remove('soap')
boxes[12].remove('cow')
boxes[3].append('cow')
boxes[12].append('soap')

# Move the magnet and the toy and the grinder from Box 13 to Box 7.
items_to_move = ['magnet', 'toy', 'grinder']
for item in items_to_move:
    boxes[13].remove(item)
    boxes[7].append(item)

# Remove the shorts and the planet from Box 11.
boxes[11].remove('shorts')
boxes[11].remove('planet')

# Swap the brush in Box 4 with the grinder in Box 7.
boxes[4].remove('brush')
boxes[7].remove('grinder')
boxes[4].append('grinder')
boxes[7].append('brush')

# Swap the dice in Box 5 with the mask in Box 0.
boxes[5].remove('dice')
boxes[0].remove('mask')
boxes[5].append('mask')
boxes[0].append('dice')

# Remove the guitar and the wig from Box 8.
boxes[8].remove('guitar')
boxes[8].remove('wig')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")