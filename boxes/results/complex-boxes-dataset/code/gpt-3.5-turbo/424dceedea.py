# Initial state of boxes
boxes = {
    0: ['mask', 'branch', 'desert'],
    1: ['shorts', 'comb', 'submarine', 'dolphin'],
    2: ['cat'],
    3: ['seaweed', 'camera', 'note', 'elephant'],
    4: ['plate', 'skirt', 'phone', 'blender'],
    5: ['lightning', 'fish', 'razor'],
    6: ['moon'],
    7: ['bus', 'card', 'boat', 'magnet']
}

# Remove the desert and the mask from Box 0.
boxes[0].remove('desert')
boxes[0].remove('mask')

# Swap the note in Box 3 with the cat in Box 2.
boxes[3].remove('note')
boxes[2].remove('cat')
boxes[3].append('cat')
boxes[2].append('note')

# Put the scissors and the spoon and the tiger into Box 7.
items_to_put = ['scissors', 'spoon', 'tiger']
for item in items_to_put:
    boxes[7].append(item)

# Put the rocket and the seaweed into Box 3.
items_to_put = ['rocket', 'seaweed']
for item in items_to_put:
    boxes[3].append(item)

# Remove the blender and the phone from Box 4.
boxes[4].remove('blender')
boxes[4].remove('phone')

# Put the scarf and the bell and the vase into Box 6.
items_to_put = ['scarf', 'bell', 'vase']
for item in items_to_put:
    boxes[6].append(item)

# Swap the submarine in Box 1 with the skirt in Box 4.
boxes[1].remove('submarine')
boxes[4].remove('skirt')
boxes[1].append('skirt')
boxes[4].append('submarine')

# Put the guitar and the river and the button into Box 5.
items_to_put = ['guitar', 'river', 'button']
for item in items_to_put:
    boxes[5].append(item)

# Move the shorts from Box 1 to Box 7.
boxes[1].remove('shorts')
boxes[7].append('shorts')

# Replace the comb and the dolphin with the basket and the oven in Box 1.
boxes[1].remove('comb')
boxes[1].remove('dolphin')
boxes[1].append('basket')
boxes[1].append('oven')

# Remove the branch from Box 0.
boxes[0].remove('branch')

# Empty Box 1.
boxes[1] = []

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")