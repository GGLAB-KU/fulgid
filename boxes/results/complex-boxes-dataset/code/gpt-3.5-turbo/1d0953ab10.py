# Initial state of boxes
boxes = {
    0: [],
    1: ['guitar', 'note', 'toothpaste', 'tie'],
    2: ['wire', 'train', 'pillow', 'desert'],
    3: ['lock', 'grass', 'plate', 'bag'],
    4: ['starfish', 'motorcycle', 'blanket', 'beach', 'sandals'],
    5: [],
    6: ['jungle', 'clock'],
    7: ['soap', 'book', 'card'],
    8: ['river', 'sculpture', 'rain', 'skirt', 'mountain'],
    9: ['necklace', 'pants', 'dice', 'rocket', 'helmet']
}

# Empty Box 1.
boxes[1] = []

# Replace the desert and the train with the magnet and the usb in Box 2.
boxes[2].remove('desert')
boxes[2].remove('train')
boxes[2].append('magnet')
boxes[2].append('usb')

# Replace the pants and the helmet with the skirt and the lightning in Box 9.
boxes[9].remove('pants')
boxes[9].remove('helmet')
boxes[9].append('skirt')
boxes[9].append('lightning')

# Replace the clock with the leaf in Box 6.
boxes[6].remove('clock')
boxes[6].append('leaf')

# Move the magnet and the pillow from Box 2 to Box 8.
items_to_move = ['magnet', 'pillow']
for item in items_to_move:
    boxes[2].remove(item)
    boxes[8].append(item)

# Put the headphone and the glasses into Box 8.
boxes[8].append('headphone')
boxes[8].append('glasses')

# Empty Box 2.
boxes[2] = []

# Move the leaf from Box 6 to Box 9.
boxes[6].remove('leaf')
boxes[9].append('leaf')

# Put the ocean and the comb into Box 6.
boxes[6].append('ocean')
boxes[6].append('comb')

# Replace the comb and the ocean and the jungle with the cloud and the note and the makeup in Box 6.
boxes[6].remove('comb')
boxes[6].remove('ocean')
boxes[6].remove('jungle')
boxes[6].append('cloud')
boxes[6].append('note')
boxes[6].append('makeup')

# Move the dice from Box 9 to Box 8.
boxes[9].remove('dice')
boxes[8].append('dice')

# Remove the note and the cloud and the makeup from Box 6.
boxes[6].remove('note')
boxes[6].remove('cloud')
boxes[6].remove('makeup')

# Put the guitar and the helmet and the bracelet into Box 6.
boxes[6].append('guitar')
boxes[6].append('helmet')
boxes[6].append('bracelet')

# Move the bracelet and the helmet and the guitar from Box 6 to Box 2.
items_to_move = ['bracelet', 'helmet', 'guitar']
for item in items_to_move:
    boxes[6].remove(item)
    boxes[2].append(item)

# Empty Box 8.
boxes[8] = []

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")