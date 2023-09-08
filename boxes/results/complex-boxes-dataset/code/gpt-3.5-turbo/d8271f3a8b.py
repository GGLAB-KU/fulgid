# Initial state of boxes
boxes = {
    0: ['cup', 'train'],
    1: ['comb', 'toothpaste', 'pen'],
    2: ['wig', 'necklace'],
    3: ['fridge'],
    4: ['puzzle', 'lock', 'sock', 'paint', 'ring'],
    5: ['needle', 'crown', 'cat'],
    6: ['elephant', 'camera', 'lamp', 'clock'],
    7: ['scissors', 'skirt'],
    8: ['blender', 'tiger', 'boat', 'helmet'],
    9: ['brush', 'headphone']
}

# Move the cat from Box 5 to Box 4.
boxes[5].remove('cat')
boxes[4].append('cat')

# Move the comb and the toothpaste and the pen from Box 1 to Box 5.
items_to_move = ['comb', 'toothpaste', 'pen']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[5].append(item)

# Swap the crown in Box 5 with the tiger in Box 8.
boxes[5].remove('crown')
boxes[8].remove('tiger')
boxes[5].append('tiger')
boxes[8].append('crown')

# Move the elephant and the camera and the clock from Box 6 to Box 7.
items_to_move = ['elephant', 'camera', 'clock']
for item in items_to_move:
    boxes[6].remove(item)
    boxes[7].append(item)

# Remove the cat and the lock and the paint from Box 4.
items_to_remove = ['cat', 'lock', 'paint']
for item in items_to_remove:
    boxes[4].remove(item)

# Move the scissors and the clock and the skirt from Box 7 to Box 6.
items_to_move = ['scissors', 'clock', 'skirt']
for item in items_to_move:
    boxes[7].remove(item)
    boxes[6].append(item)

# Put the jungle and the comet into Box 5.
boxes[5].extend(['jungle', 'comet'])

# Swap the fridge in Box 3 with the boat in Box 8.
boxes[3], boxes[8] = boxes[8], boxes[3]

# Remove the headphone and the brush from Box 9.
items_to_remove = ['headphone', 'brush']
for item in items_to_remove:
    boxes[9].remove(item)

# Swap the skirt in Box 6 with the wig in Box 2.
boxes[6].remove('skirt')
boxes[2].remove('wig')
boxes[6].append('wig')
boxes[2].append('skirt')

# Move the boat from Box 3 to Box 4.
boxes[3].remove('boat')
boxes[4].append('boat')

# Remove the helmet and the fridge and the blender from Box 8.
items_to_remove = ['helmet', 'fridge', 'blender']
for item in items_to_remove:
    boxes[8].remove(item)

# Replace the camera and the elephant with the island and the telescope in Box 7.
boxes[7].remove('camera')
boxes[7].remove('elephant')
boxes[7].append('island')
boxes[7].append('telescope')

# Swap the toothpaste in Box 5 with the telescope in Box 7.
boxes[5].remove('toothpaste')
boxes[7].remove('telescope')
boxes[5].append('telescope')
boxes[7].append('toothpaste')

# Empty Box 0.
boxes[0] = []

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")