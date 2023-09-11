# Initial state of boxes
boxes = {
    0: ['note', 'glasses', 'wallet', 'butterfly'],
    1: ['bird', 'island', 'frame'],
    2: ['helmet', 'jacket', 'necklace', 'pants', 'pen'],
    3: ['sun', 'snow', 'pillow', 'zipper'],
    4: ['shorts'],
    5: ['jungle', 'star', 'hat', 'starfish'],
    6: ['shark', 'lion', 'pot', 'magnet', 'bracelet'],
    7: ['umbrella', 'lamp', 'sculpture'],
    8: ['microscope', 'vase', 'puzzle']
}

# Move the jacket and the pen and the necklace from Box 2 to Box 1.
items_to_move = ['jacket', 'pen', 'necklace']
for item in items_to_move:
    boxes[2].remove(item)
    boxes[1].append(item)

# Swap the note in Box 0 with the shorts in Box 4.
boxes[0].remove('note')
boxes[4].remove('shorts')
boxes[0].append('shorts')
boxes[4].append('note')

# Remove the star and the hat and the starfish from Box 5.
items_to_remove = ['star', 'hat', 'starfish']
for item in items_to_remove:
    boxes[5].remove(item)

# Swap the sun in Box 3 with the wallet in Box 0.
boxes[3].remove('sun')
boxes[0].remove('wallet')
boxes[3].append('wallet')
boxes[0].append('sun')

# Move the vase from Box 8 to Box 2.
boxes[8].remove('vase')
boxes[2].append('vase')

# Replace the microscope with the shoe in Box 8.
boxes[8].remove('microscope')
boxes[8].append('shoe')

# Swap the snow in Box 3 with the jungle in Box 5.
boxes[3].remove('snow')
boxes[5].remove('jungle')
boxes[3].append('jungle')
boxes[5].append('snow')

# Move the shorts and the glasses and the sun from Box 0 to Box 6.
items_to_move = ['shorts', 'glasses', 'sun']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[6].append(item)

# Move the puzzle and the shoe from Box 8 to Box 7.
boxes[8].remove('puzzle')
boxes[8].remove('shoe')
boxes[7].append('puzzle')
boxes[7].append('shoe')

# Move the butterfly from Box 0 to Box 3.
boxes[0].remove('butterfly')
boxes[3].append('butterfly')

# Replace the shoe with the mirror in Box 7.
boxes[7].remove('shoe')
boxes[7].append('mirror')

# Put the blender and the key and the train into Box 3.
items_to_put = ['blender', 'key', 'train']
for item in items_to_put:
    boxes[3].append(item)

# Move the sun and the shark and the lion from Box 6 to Box 8.
items_to_move = ['sun', 'shark', 'lion']
for item in items_to_move:
    boxes[6].remove(item)
    boxes[8].append(item)

# Replace the bracelet with the toy in Box 6.
boxes[6].remove('bracelet')
boxes[6].append('toy')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")