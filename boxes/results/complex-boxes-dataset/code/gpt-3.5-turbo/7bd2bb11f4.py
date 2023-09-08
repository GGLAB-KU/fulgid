# Initial state of boxes
boxes = {
    0: ['bag'],
    1: [],
    2: ['boot', 'comet', 'lightning'],
    3: [],
    4: ['belt', 'jacket'],
    5: ['controller', 'motorcycle', 'comb'],
    6: ['doll', 'guitar', 'brush'],
    7: ['horn', 'fish']
}

# Move the belt from Box 4 to Box 2.
boxes[4].remove('belt')
boxes[2].append('belt')

# Remove the fish from Box 7.
boxes[7].remove('fish')

# Swap the bag in Box 0 with the controller in Box 5.
boxes[0], boxes[5] = boxes[5], boxes[0]

# Swap the controller in Box 0 with the horn in Box 7.
boxes[0], boxes[7] = boxes[7], boxes[0]

# Remove the horn from Box 0.
boxes[0].remove('horn')

# Replace the jacket with the fish in Box 4.
boxes[4].remove('jacket')
boxes[4].append('fish')

# Move the comb and the motorcycle from Box 5 to Box 3.
items_to_move = ['comb', 'motorcycle']
for item in items_to_move:
    boxes[5].remove(item)
    boxes[3].append(item)

# Put the laptop and the tree and the glasses into Box 6.
items_to_put = ['laptop', 'tree', 'glasses']
for item in items_to_put:
    boxes[6].append(item)

# Remove the comb and the motorcycle from Box 3.
boxes[3].remove('comb')
boxes[3].remove('motorcycle')

# Swap the controller in Box 7 with the boot in Box 2.
boxes[7], boxes[2] = boxes[2], boxes[7]

# Put the cloud into Box 1.
boxes[1].append('cloud')

# Replace the cloud with the charger in Box 1.
boxes[1].remove('cloud')
boxes[1].append('charger')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")