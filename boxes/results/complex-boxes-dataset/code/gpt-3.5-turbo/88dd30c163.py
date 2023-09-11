# Initial state of boxes
boxes = {
    0: ['oven'],
    1: ['speaker', 'soap', 'bracelet'],
    2: ['tape', 'forest', 'basket', 'elephant', 'butterfly'],
    3: ['note', 'cloud', 'comet', 'fish'],
    4: []
}

# Replace the fish with the branch in Box 3.
boxes[3].remove('fish')
boxes[3].append('branch')

# Move the oven from Box 0 to Box 3.
boxes[0].remove('oven')
boxes[3].append('oven')

# Empty Box 3.
boxes[3] = []

# Replace the basket and the forest with the helmet and the pants in Box 2.
boxes[2].remove('basket')
boxes[2].remove('forest')
boxes[2].append('helmet')
boxes[2].append('pants')

# Move the soap and the bracelet and the speaker from Box 1 to Box 4.
items_to_move = ['soap', 'bracelet', 'speaker']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[4].append(item)

# Move the pants and the helmet and the elephant from Box 2 to Box 3.
items_to_move = ['pants', 'helmet', 'elephant']
for item in items_to_move:
    boxes[2].remove(item)
    boxes[3].append(item)

# Move the pants and the helmet from Box 3 to Box 2.
items_to_move = ['pants', 'helmet']
for item in items_to_move:
    boxes[3].remove(item)
    boxes[2].append(item)

# Put the shoes and the blender into Box 3.
items_to_add = ['shoes', 'blender']
for item in items_to_add:
    boxes[3].append(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")