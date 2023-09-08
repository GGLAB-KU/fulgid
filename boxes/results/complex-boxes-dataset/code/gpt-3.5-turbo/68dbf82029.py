# Initial state of boxes
boxes = {
    0: ['table', 'shark'],
    1: ['shampoo', 'pillow'],
    2: ['cat'],
    3: ['desert', 'belt', 'soap', 'violin', 'cup'],
    4: ['bracelet', 'comb', 'skirt'],
    5: ['vase', 'glove', 'camera'],
    6: ['cloud'],
    7: ['toy', 'horn', 'battery', 'planet'],
    8: ['towel'],
    9: ['car', 'ring', 'tiger', 'octopus', 'spoon'],
    10: ['fish', 'clock', 'toothbrush', 'wig'],
    11: ['zipper', 'microwave', 'necklace', 'drum', 'shirt'],
    12: ['freezer'],
    13: [],
    14: []
}

# Remove the towel from Box 8.
boxes[8].remove('towel')

# Put the makeup and the tree and the harmonica into Box 9.
items_to_put = ['makeup', 'tree', 'harmonica']
for item in items_to_put:
    boxes[9].append(item)

# Empty Box 4.
boxes[4] = []

# Replace the planet and the battery and the horn with the candle and the starfish and the glasses in Box 7.
boxes[7].remove('planet')
boxes[7].remove('battery')
boxes[7].remove('horn')
boxes[7].append('candle')
boxes[7].append('starfish')
boxes[7].append('glasses')

# Remove the cloud from Box 6.
boxes[6].remove('cloud')

# Move the glove and the camera from Box 5 to Box 4.
items_to_move = ['glove', 'camera']
for item in items_to_move:
    boxes[5].remove(item)
    boxes[4].append(item)

# Move the clock and the wig from Box 10 to Box 3.
items_to_move = ['clock', 'wig']
for item in items_to_move:
    boxes[10].remove(item)
    boxes[3].append(item)

# Put the toothbrush and the elephant and the train into Box 3.
items_to_put = ['toothbrush', 'elephant', 'train']
for item in items_to_put:
    boxes[3].append(item)

# Move the camera from Box 4 to Box 0.
boxes[4].remove('camera')
boxes[0].append('camera')

# Remove the train and the belt and the elephant from Box 3.
items_to_remove = ['train', 'belt', 'elephant']
for item in items_to_remove:
    boxes[3].remove(item)

# Replace the freezer with the lock in Box 12.
boxes[12].remove('freezer')
boxes[12].append('lock')

# Remove the glove from Box 4.
boxes[4].remove('glove')

# Remove the soap and the toothbrush from Box 3.
items_to_remove = ['soap', 'toothbrush']
for item in items_to_remove:
    boxes[3].remove(item)

# Put the hat and the phone and the shelf into Box 0.
items_to_put = ['hat', 'phone', 'shelf']
for item in items_to_put:
    boxes[0].append(item)

# Put the jungle and the necklace into Box 14.
items_to_put = ['jungle', 'necklace']
for item in items_to_put:
    boxes[14].append(item)

# Put the drum and the submarine into Box 13.
items_to_put = ['drum', 'submarine']
for item in items_to_put:
    boxes[13].append(item)

# Put the shoe and the polish and the rain into Box 5.
items_to_put = ['shoe', 'polish', 'rain']
for item in items_to_put:
    boxes[5].append(item)

# Remove the toothbrush and the fish from Box 10.
items_to_remove = ['toothbrush', 'fish']
for item in items_to_remove:
    boxes[10].remove(item)

# Remove the necklace and the jungle from Box 14.
items_to_remove = ['necklace', 'jungle']
for item in items_to_remove:
    boxes[14].remove(item)

# Put the vase into Box 12.
boxes[5].remove('vase')
boxes[12].append('vase')

# Swap the drum in Box 13 with the shampoo in Box 1.
boxes[13].remove('drum')
boxes[1].remove('shampoo')
boxes[13].append('shampoo')
boxes[1].append('drum')

# Remove the vase and the shoe and the rain from Box 5.
items_to_remove = ['vase', 'shoe', 'rain']
for item in items_to_remove:
    boxes[5].remove(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")