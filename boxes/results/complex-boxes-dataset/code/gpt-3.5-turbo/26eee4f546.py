# Initial state of boxes
boxes = {
    0: ['butterfly', 'tie', 'rock', 'crown', 'bicycle'],
    1: ['zipper', 'battery', 'needle'],
    2: ['perfume', 'bell', 'octopus'],
    3: ['mountain', 'watch', 'shoes'],
    4: ['guitar', 'grinder', 'speaker', 'blender'],
    5: ['fork', 'grass', 'makeup', 'chair'],
    6: []
}

# Put the beach into Box 2.
boxes[2].append('beach')

# Replace the tie with the umbrella in Box 0.
boxes[0].remove('tie')
boxes[0].append('umbrella')

# Swap the battery in Box 1 with the grass in Box 5.
boxes[1].remove('battery')
boxes[5].remove('grass')
boxes[1].append('grass')
boxes[5].append('battery')

# Move the battery from Box 5 to Box 1.
boxes[5].remove('battery')
boxes[1].append('battery')

# Move the umbrella and the bicycle and the butterfly from Box 0 to Box 6.
items_to_move = ['umbrella', 'bicycle', 'butterfly']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[6].append(item)

# Swap the blender in Box 4 with the needle in Box 1.
boxes[4].remove('blender')
boxes[1].remove('needle')
boxes[4].append('needle')
boxes[1].append('blender')

# Replace the crown with the shirt in Box 0.
boxes[0].remove('crown')
boxes[0].append('shirt')

# Put the guitar and the glove and the book into Box 3.
items_to_put = ['guitar', 'glove', 'book']
for item in items_to_put:
    boxes[3].append(item)

# Put the lion into Box 6.
boxes[6].append('lion')

# Remove the rock and the shirt from Box 0.
boxes[0].remove('rock')
boxes[0].remove('shirt')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")