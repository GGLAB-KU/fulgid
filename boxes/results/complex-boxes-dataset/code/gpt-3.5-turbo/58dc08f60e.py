# Initial state of boxes
boxes = {
    0: ['makeup', 'fish'],
    1: ['microwave'],
    2: ['seaweed', 'book', 'cloud', 'controller'],
    3: ['pants', 'meteor', 'submarine', 'coral'],
    4: ['hat', 'desert', 'blender', 'dress'],
    5: ['key', 'phone', 'drum', 'fork', 'comet'],
    6: ['grass', 'guitar', 'charger', 'river', 'branch'],
    7: [],
    8: [],
    9: []
}

# Remove the microwave from Box 1.
boxes[1].remove('microwave')

# Put the perfume into Box 8.
boxes[8].append('perfume')

# Swap the submarine in Box 3 with the makeup in Box 0.
boxes[3].remove('submarine')
boxes[0].remove('makeup')
boxes[3].append('makeup')
boxes[0].append('submarine')

# Remove the key from Box 5.
boxes[5].remove('key')

# Remove the branch from Box 6.
boxes[6].remove('branch')

# Remove the charger and the guitar from Box 6.
boxes[6].remove('charger')
boxes[6].remove('guitar')

# Swap the perfume in Box 8 with the coral in Box 3.
boxes[8].remove('perfume')
boxes[3].remove('coral')
boxes[8].append('coral')
boxes[3].append('perfume')

# Remove the cloud and the controller and the book from Box 2.
items_to_remove = ['cloud', 'controller', 'book']
for item in items_to_remove:
    boxes[2].remove(item)

# Swap the river in Box 6 with the coral in Box 8.
boxes[6].remove('river')
boxes[8].remove('coral')
boxes[6].append('coral')
boxes[8].append('river')

# Empty Box 8.
boxes[8] = []

# Swap the pants in Box 3 with the desert in Box 4.
boxes[3].remove('pants')
boxes[4].remove('desert')
boxes[3].append('desert')
boxes[4].append('pants')

# Remove the grass and the coral from Box 6.
boxes[6].remove('grass')
boxes[6].remove('coral')

# Move the seaweed from Box 2 to Box 0.
boxes[2].remove('seaweed')
boxes[0].append('seaweed')

# Move the makeup from Box 3 to Box 7.
boxes[3].remove('makeup')
boxes[7].append('makeup')

# Remove the makeup from Box 7.
boxes[7].remove('makeup')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")