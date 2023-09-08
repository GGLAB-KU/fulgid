# Initial state of boxes
boxes = {
    0: ['storm', 'train', 'magnet', 'ring', 'bracelet'],
    1: [],
    2: ['plate', 'razor', 'pen', 'flower', 'shelf'],
    3: ['game', 'lipstick'],
    4: [],
    5: [],
    6: ['jungle', 'grinder', 'frame', 'table'],
    7: ['piano'],
    8: ['harmonica', 'blender', 'shoe', 'dog'],
    9: ['whistle', 'thunder'],
    10: [],
    11: ['camera', 'bell', 'speaker', 'pants', 'rain']
}

# Remove the shoe from Box 8.
boxes[8].remove('shoe')

# Remove the dog and the harmonica and the blender from Box 8.
items_to_remove = ['dog', 'harmonica', 'blender']
for item in items_to_remove:
    boxes[8].remove(item)

# Swap the plate in Box 2 with the table in Box 6.
boxes[2].remove('plate')
boxes[6].remove('table')
boxes[2].append('table')
boxes[6].append('plate')

# Remove the rain from Box 11.
boxes[11].remove('rain')

# Swap the piano in Box 7 with the razor in Box 2.
boxes[7].remove('piano')
boxes[2].remove('razor')
boxes[7].append('razor')
boxes[2].append('piano')

# Replace the ring and the bracelet and the magnet with the branch and the blanket and the boot in Box 0.
boxes[0].remove('ring')
boxes[0].remove('bracelet')
boxes[0].remove('magnet')
boxes[0].append('branch')
boxes[0].append('blanket')
boxes[0].append('boot')

# Swap the game in Box 3 with the pen in Box 2.
boxes[3].remove('game')
boxes[2].remove('pen')
boxes[3].append('pen')
boxes[2].append('game')

# Move the lipstick and the pen from Box 3 to Box 9.
boxes[3].remove('lipstick')
boxes[3].remove('pen')
boxes[9].append('lipstick')
boxes[9].append('pen')

# Move the jungle from Box 6 to Box 7.
boxes[6].remove('jungle')
boxes[7].append('jungle')

# Move the plate and the grinder and the frame from Box 6 to Box 10.
items_to_move = ['plate', 'grinder', 'frame']
for item in items_to_move:
    boxes[6].remove(item)
    boxes[10].append(item)

# Move the jungle and the razor from Box 7 to Box 9.
boxes[7].remove('jungle')
boxes[2].remove('razor')
boxes[9].append('jungle')
boxes[9].append('razor')

# Put the train into Box 3.
boxes[0].remove('train')
boxes[3].append('train')

# Put the guitar and the phone and the desert into Box 10.
items_to_put = ['guitar', 'phone', 'desert']
for item in items_to_put:
    boxes[10].append(item)

# Put the console and the frame and the bowl into Box 8.
items_to_put = ['console', 'frame', 'bowl']
for item in items_to_put:
    boxes[8].append(item)

# Remove the pants and the camera from Box 11.
items_to_remove = ['pants', 'camera']
for item in items_to_remove:
    boxes[11].remove(item)

# Put the coral and the lipstick and the grass into Box 0.
items_to_put = ['coral', 'lipstick', 'grass']
for item in items_to_put:
    boxes[0].append(item)

# Remove the pen and the lipstick from Box 9.
items_to_remove = ['pen', 'lipstick']
for item in items_to_remove:
    boxes[9].remove(item)

# Replace the whistle and the razor and the thunder with the controller and the pants and the crown in Box 9.
boxes[9].remove('whistle')
boxes[9].remove('razor')
boxes[9].remove('thunder')
boxes[9].append('controller')
boxes[9].append('pants')
boxes[9].append('crown')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")