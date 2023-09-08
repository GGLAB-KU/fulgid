# Initial state of boxes
boxes = {
    0: ['toothbrush', 'helmet', 'lion'],
    1: ['shelf'],
    2: ['charger', 'rocket', 'frame', 'toothpaste', 'clock'],
    3: ['submarine', 'cloud'],
    4: ['tiger', 'coin', 'rain', 'boot', 'telescope'],
    5: [],
    6: ['river'],
    7: ['belt', 'dress', 'star'],
    8: ['wig', 'starfish', 'mixer', 'microscope', 'mask'],
    9: ['swimsuit', 'flower', 'lock', 'shorts', 'speaker'],
    10: ['umbrella', 'camera', 'fish'],
    11: ['glove', 'beach', 'shark'],
    12: ['cup']
}

# Move the star and the dress and the belt from Box 7 to Box 4.
items_to_move = ['star', 'dress', 'belt']
for item in items_to_move:
    boxes[7].remove(item)
    boxes[4].append(item)

# Remove the river from Box 6.
boxes[6].remove('river')

# Remove the camera and the umbrella from Box 10.
boxes[10].remove('camera')
boxes[10].remove('umbrella')

# Put the shorts and the note and the tie into Box 7.
items_to_put = ['shorts', 'note', 'tie']
for item in items_to_put:
    boxes[7].append(item)

# Put the coral into Box 7.
boxes[7].append('coral')

# Swap the boot in Box 4 with the fish in Box 10.
boxes[4].remove('boot')
boxes[10].remove('fish')
boxes[4].append('fish')
boxes[10].append('boot')

# Remove the coral and the note and the shorts from Box 7.
items_to_remove = ['coral', 'note', 'shorts']
for item in items_to_remove:
    boxes[7].remove(item)

# Remove the wig and the microscope from Box 8.
boxes[8].remove('wig')
boxes[8].remove('microscope')

# Swap the cup in Box 12 with the glove in Box 11.
boxes[12].remove('cup')
boxes[11].remove('glove')
boxes[12].append('glove')
boxes[11].append('cup')

# Move the toothbrush and the helmet from Box 0 to Box 12.
items_to_move = ['toothbrush', 'helmet']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[12].append(item)

# Remove the rain and the telescope from Box 4.
boxes[4].remove('rain')
boxes[4].remove('telescope')

# Put the brush and the paint and the razor into Box 0.
items_to_put = ['brush', 'paint', 'razor']
for item in items_to_put:
    boxes[0].append(item)

# Put the shark and the shelf into Box 4.
boxes[11].remove('shark')
boxes[1].remove('shelf')
boxes[4].append('shark')
boxes[4].append('shelf')

# Move the shelf from Box 1 to Box 11.
boxes[1].remove('shelf')
boxes[11].append('shelf')

# Replace the tie with the tree in Box 7.
boxes[7].remove('tie')
boxes[7].append('tree')

# Move the beach and the shelf from Box 11 to Box 8.
boxes[11].remove('beach')
boxes[11].remove('shelf')
boxes[8].append('beach')
boxes[8].append('shelf')

# Move the lion and the paint and the brush from Box 0 to Box 11.
items_to_move = ['lion', 'paint', 'brush']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[11].append(item)

# Put the laptop into Box 10.
boxes[10].append('laptop')

# Swap the flower in Box 9 with the tiger in Box 4.
boxes[9].remove('flower')
boxes[4].remove('tiger')
boxes[9].append('tiger')
boxes[4].append('flower')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")