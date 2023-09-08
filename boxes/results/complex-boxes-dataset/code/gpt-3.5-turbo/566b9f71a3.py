# Initial state of boxes
boxes = {
    0: ['mountain', 'shark'],
    1: [],
    2: ['comb', 'mirror', 'train', 'coral', 'horse'],
    3: ['blender', 'pen', 'planet', 'tape'],
    4: ['belt', 'flute'],
    5: []
}

# Replace the planet and the blender with the drum and the chair in Box 3.
boxes[3].remove('planet')
boxes[3].remove('blender')
boxes[3].append('drum')
boxes[3].append('chair')

# Replace the horse with the train in Box 2.
boxes[2].remove('horse')
boxes[2].append('train')

# Swap the belt in Box 4 with the train in Box 2.
boxes[4].remove('belt')
boxes[2].remove('train')
boxes[4].append('train')
boxes[2].append('belt')

# Replace the belt with the glasses in Box 2.
boxes[2].remove('belt')
boxes[2].append('glasses')

# Move the tape and the pen from Box 3 to Box 5.
items_to_move = ['tape', 'pen']
for item in items_to_move:
    boxes[3].remove(item)
    boxes[5].append(item)

# Remove the chair from Box 3.
boxes[3].remove('chair')

# Swap the train in Box 4 with the mountain in Box 0.
boxes[4].remove('train')
boxes[0].remove('mountain')
boxes[4].append('mountain')
boxes[0].append('train')

# Put the tree and the moon into Box 5.
items_to_move = ['tree', 'moon']
for item in items_to_move:
    boxes[5].append(item)

# Put the jacket and the doll and the beach into Box 0.
items_to_move = ['jacket', 'doll', 'beach']
for item in items_to_move:
    boxes[0].append(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")