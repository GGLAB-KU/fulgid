# Initial state of boxes
boxes = {
    0: ['needle', 'scissors', 'glasses', 'laptop', 'train'],
    1: ['shirt', 'dolphin', 'scarf', 'toy', 'cat'],
    2: [],
    3: ['umbrella', 'bag', 'cow', 'mirror'],
    4: ['lightning', 'towel'],
    5: ['horse'],
    6: ['sock', 'controller', 'skirt', 'lipstick', 'mask'],
    7: ['blender', 'keyboard', 'rock', 'boot'],
    8: ['razor'],
    9: ['beach', 'fish']
}

# Replace the beach with the whistle in Box 9.
boxes[9].remove('beach')
boxes[9].append('whistle')

# Move the controller and the mask from Box 6 to Box 7.
items_to_move = ['controller', 'mask']
for item in items_to_move:
    boxes[6].remove(item)
    boxes[7].append(item)

# Move the glasses and the train from Box 0 to Box 8.
items_to_move = ['glasses', 'train']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[8].append(item)

# Swap the horse in Box 5 with the skirt in Box 6.
boxes[5], boxes[6] = boxes[6], boxes[5]

# Remove the lightning from Box 4.
boxes[4].remove('lightning')

# Put the shirt and the necklace and the clock into Box 8.
items_to_put = ['shirt', 'necklace', 'clock']
for item in items_to_put:
    boxes[8].append(item)

# Put the cow and the toy into Box 0.
items_to_put = ['cow', 'toy']
for item in items_to_put:
    boxes[0].append(item)

# Move the towel from Box 4 to Box 1.
boxes[4].remove('towel')
boxes[1].append('towel')

# Swap the shirt in Box 8 with the skirt in Box 5.
boxes[8], boxes[5] = boxes[5], boxes[8]

# Swap the toy in Box 1 with the fish in Box 9.
boxes[1], boxes[9] = boxes[9], boxes[1]

# Remove the laptop from Box 0.
boxes[0].remove('laptop')

# Swap the toy in Box 9 with the lipstick in Box 6.
boxes[9], boxes[6] = boxes[6], boxes[9]

# Remove the sock and the toy from Box 6.
items_to_remove = ['sock', 'toy']
for item in items_to_remove:
    boxes[6].remove(item)

# Put the microscope and the grass into Box 6.
items_to_put = ['microscope', 'grass']
for item in items_to_put:
    boxes[6].append(item)

# Put the soap and the microwave into Box 5.
items_to_put = ['soap', 'microwave']
for item in items_to_put:
    boxes[5].append(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")