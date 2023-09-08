# Initial state of boxes
boxes = {
    0: ['boat', 'doll', 'crown', 'zipper'],
    1: ['lion', 'toothbrush', 'train'],
    2: ['truck', 'seaweed', 'phone', 'motorcycle', 'magnet'],
    3: ['whistle', 'brush', 'frame', 'makeup', 'paint'],
    4: ['perfume', 'flower'],
    5: ['blender'],
    6: ['button'],
    7: ['fish', 'bell', 'rain', 'car'],
    8: ['battery', 'tie', 'branch', 'bicycle'],
    9: ['rocket', 'speaker'],
    10: ['ship', 'lightning', 'piano', 'cat', 'bus'],
    11: ['tiger'],
    12: ['keyboard', 'shampoo']
}

# Move the bell and the rain from Box 7 to Box 8.
boxes[7].remove('bell')
boxes[7].remove('rain')
boxes[8].append('bell')
boxes[8].append('rain')

# Put the coat and the bear into Box 2.
boxes[2].append('coat')
boxes[2].append('bear')

# Move the fish from Box 7 to Box 6.
boxes[7].remove('fish')
boxes[6].append('fish')

# Replace the speaker and the rocket with the scarf and the elephant in Box 9.
boxes[9].remove('speaker')
boxes[9].remove('rocket')
boxes[9].append('scarf')
boxes[9].append('elephant')

# Move the elephant and the scarf from Box 9 to Box 11.
boxes[9].remove('elephant')
boxes[9].remove('scarf')
boxes[11].append('elephant')
boxes[11].append('scarf')

# Move the magnet and the phone and the coat from Box 2 to Box 6.
items_to_move = ['magnet', 'phone', 'coat']
for item in items_to_move:
    boxes[2].remove(item)
    boxes[6].append(item)

# Move the doll and the boat and the zipper from Box 0 to Box 11.
items_to_move = ['doll', 'boat', 'zipper']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[11].append(item)

# Empty Box 2.
boxes[2] = []

# Put the glove and the ring and the pants into Box 7.
items_to_put = ['glove', 'ring', 'pants']
for item in items_to_put:
    boxes[7].append(item)

# Remove the bell from Box 8.
boxes[8].remove('bell')

# Swap the lion in Box 1 with the pants in Box 7.
boxes[1].remove('lion')
boxes[7].remove('pants')
boxes[1].append('pants')
boxes[7].append('lion')

# Swap the lion in Box 7 with the rain in Box 8.
boxes[7].remove('lion')
boxes[8].remove('rain')
boxes[7].append('rain')
boxes[8].append('lion')

# Move the flower and the perfume from Box 4 to Box 8.
items_to_move = ['flower', 'perfume']
for item in items_to_move:
    boxes[4].remove(item)
    boxes[8].append(item)

# Empty Box 6.
boxes[6] = []

# Put the shoes and the cloud and the bag into Box 12.
items_to_put = ['shoes', 'cloud', 'bag']
for item in items_to_put:
    boxes[12].append(item)

# Remove the doll and the tiger and the zipper from Box 11.
items_to_remove = ['doll', 'tiger', 'zipper']
for item in items_to_remove:
    boxes[11].remove(item)

# Move the toothbrush and the pants and the train from Box 1 to Box 10.
items_to_move = ['toothbrush', 'pants', 'train']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[10].append(item)

# Remove the blender from Box 5.
boxes[5].remove('blender')

# Empty Box 12.
boxes[12] = []

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")