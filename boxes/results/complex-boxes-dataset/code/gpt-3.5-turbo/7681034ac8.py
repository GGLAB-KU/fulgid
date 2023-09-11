# Initial state of boxes
boxes = {
    0: ['rocket', 'tiger', 'tree'],
    1: ['boat', 'skirt', 'brush', 'grinder', 'battery'],
    2: ['blender', 'dolphin', 'laptop'],
    3: ['planet', 'train', 'book', 'paint', 'blanket'],
    4: ['moon', 'phone', 'mountain', 'speaker'],
    5: ['microscope', 'ocean', 'scarf', 'cup', 'bicycle'],
    6: ['freezer', 'glasses'],
    7: ['desert', 'rock', 'zipper'],
    8: ['cow'],
    9: ['sock'],
    10: ['coral', 'plate', 'charger', 'clock']
}

# Move the clock from Box 10 to Box 6.
boxes[10].remove('clock')
boxes[6].append('clock')

# Move the clock from Box 6 to Box 2.
boxes[6].remove('clock')
boxes[2].append('clock')

# Move the rock from Box 7 to Box 5.
boxes[7].remove('rock')
boxes[5].append('rock')

# Empty Box 4.
boxes[4] = []

# Remove the book and the paint and the train from Box 3.
items_to_remove = ['book', 'paint', 'train']
for item in items_to_remove:
    boxes[3].remove(item)

# Move the plate and the charger and the coral from Box 10 to Box 9.
items_to_move = ['plate', 'charger', 'coral']
for item in items_to_move:
    boxes[10].remove(item)
    boxes[9].append(item)

# Swap the tree in Box 0 with the zipper in Box 7.
boxes[0].remove('tree')
boxes[7].remove('zipper')
boxes[0].append('zipper')
boxes[7].append('tree')

# Move the planet from Box 3 to Box 7.
boxes[3].remove('planet')
boxes[7].append('planet')

# Move the clock and the blender from Box 2 to Box 7.
boxes[2].remove('clock')
boxes[2].remove('blender')
boxes[7].append('clock')
boxes[7].append('blender')

# Put the whistle and the mask and the cup into Box 5.
items_to_put = ['whistle', 'mask', 'cup']
for item in items_to_put:
    boxes[5].append(item)

# Move the freezer and the glasses from Box 6 to Box 0.
boxes[6].remove('freezer')
boxes[6].remove('glasses')
boxes[0].append('freezer')
boxes[0].append('glasses')

# Empty Box 0.
boxes[0] = []

# Replace the coral with the elephant in Box 9.
boxes[9].remove('coral')
boxes[9].append('elephant')

# Move the scarf and the mask from Box 5 to Box 2.
boxes[5].remove('scarf')
boxes[5].remove('mask')
boxes[2].append('scarf')
boxes[2].append('mask')

# Put the lion and the microwave and the bear into Box 10.
items_to_put = ['lion', 'microwave', 'bear']
for item in items_to_put:
    boxes[10].append(item)

# Swap the mask in Box 2 with the planet in Box 7.
boxes[2].remove('mask')
boxes[7].remove('planet')
boxes[2].append('planet')
boxes[7].append('mask')

# Replace the cup with the watch in Box 5.
boxes[5].remove('cup')
boxes[5].append('watch')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")