# Initial state of boxes
boxes = {
    0: ['seaweed', 'motorcycle', 'sun', 'forest', 'glove'],
    1: ['needle'],
    2: ['dice', 'magnet', 'headphone', 'shelf'],
    3: ['pants', 'shirt', 'lamp'],
    4: [],
    5: ['grass', 'mirror', 'submarine', 'perfume', 'branch'],
    6: [],
    7: [],
    8: ['moon', 'swimsuit', 'sandals'],
    9: []
}

# Swap the sandals in Box 8 with the shirt in Box 3.
boxes[8].remove('sandals')
boxes[3].remove('shirt')
boxes[8].append('shirt')
boxes[3].append('sandals')

# Put the apple and the chair and the thread into Box 9.
items_to_put = ['apple', 'chair', 'thread']
for item in items_to_put:
    boxes[9].append(item)

# Put the dice into Box 8.
boxes[8].append('dice')

# Move the thread from Box 9 to Box 6.
boxes[9].remove('thread')
boxes[6].append('thread')

# Move the grass and the perfume from Box 5 to Box 0.
items_to_move = ['grass', 'perfume']
for item in items_to_move:
    boxes[5].remove(item)
    boxes[0].append(item)

# Empty Box 9.
boxes[9] = []

# Replace the perfume and the seaweed and the forest with the flute and the butterfly and the soap in Box 0.
boxes[0].remove('perfume')
boxes[0].remove('seaweed')
boxes[0].remove('forest')
boxes[0].append('flute')
boxes[0].append('butterfly')
boxes[0].append('soap')

# Swap the sandals in Box 3 with the thread in Box 6.
boxes[3].remove('sandals')
boxes[6].remove('thread')
boxes[3].append('thread')
boxes[6].append('sandals')

# Replace the branch with the forest in Box 5.
boxes[5].remove('branch')
boxes[5].append('forest')

# Replace the submarine and the mirror and the forest with the camera and the table and the dress in Box 5.
boxes[5].remove('submarine')
boxes[5].remove('mirror')
boxes[5].remove('forest')
boxes[5].append('camera')
boxes[5].append('table')
boxes[5].append('dress')

# Remove the needle from Box 1.
boxes[1].remove('needle')

# Put the dice and the boat into Box 2.
items_to_put = ['dice', 'boat']
for item in items_to_put:
    boxes[2].append(item)

# Swap the table in Box 5 with the shirt in Box 8.
boxes[5].remove('table')
boxes[8].remove('shirt')
boxes[5].append('shirt')
boxes[8].append('table')

# Move the headphone and the boat and the rain from Box 2 to Box 0.
items_to_move = ['headphone', 'boat', 'rain']
for item in items_to_move:
    boxes[2].remove(item)
    boxes[0].append(item)

# Put the leaf and the battery into Box 8.
items_to_put = ['leaf', 'battery']
for item in items_to_put:
    boxes[8].append(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")