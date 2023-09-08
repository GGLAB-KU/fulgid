# Initial state of boxes
boxes = {
    0: [],
    1: ['battery', 'perfume', 'basket'],
    2: ['clock', 'rain', 'shorts', 'vase', 'boat'],
    3: ['butterfly'],
    4: ['dog', 'bag', 'mountain'],
    5: ['elephant', 'zipper', 'scissors', 'bird', 'shirt'],
    6: ['mirror'],
    7: ['makeup', 'sun', 'dolphin'],
    8: ['blender', 'piano', 'thunder'],
    9: ['freezer', 'card', 'tiger']
}

# Swap the butterfly in Box 3 with the basket in Box 1.
boxes[3].remove('butterfly')
boxes[1].remove('basket')
boxes[3].append('basket')
boxes[1].append('butterfly')

# Remove the freezer and the tiger and the card from Box 9.
items_to_remove = ['freezer', 'tiger', 'card']
for item in items_to_remove:
    boxes[9].remove(item)

# Replace the battery and the perfume and the butterfly with the apple and the fork and the glasses in Box 1.
boxes[1].remove('battery')
boxes[1].remove('perfume')
boxes[1].remove('butterfly')
boxes[1].append('apple')
boxes[1].append('fork')
boxes[1].append('glasses')

# Remove the blender and the piano and the thunder from Box 8.
items_to_remove = ['blender', 'piano', 'thunder']
for item in items_to_remove:
    boxes[8].remove(item)

# Put the pillow and the ship and the flute into Box 2.
items_to_add = ['pillow', 'ship', 'flute']
for item in items_to_add:
    boxes[2].append(item)

# Replace the mirror with the phone in Box 6.
boxes[6].remove('mirror')
boxes[6].append('phone')

# Remove the bird from Box 5.
boxes[5].remove('bird')

# Move the flute from Box 2 to Box 8.
boxes[2].remove('flute')
boxes[8].append('flute')

# Replace the flute with the scarf in Box 8.
boxes[8].remove('flute')
boxes[8].append('scarf')

# Remove the dolphin and the sun and the makeup from Box 7.
items_to_remove = ['dolphin', 'sun', 'makeup']
for item in items_to_remove:
    boxes[7].remove(item)

# Remove the scarf from Box 8.
boxes[8].remove('scarf')

# Put the plate into Box 8.
boxes[8].append('plate')

# Remove the ship and the shorts from Box 2.
items_to_remove = ['ship', 'shorts']
for item in items_to_remove:
    boxes[2].remove(item)

# Empty Box 2.
boxes[2] = []

# Put the charger and the book and the storm into Box 3.
items_to_add = ['charger', 'book', 'storm']
for item in items_to_add:
    boxes[3].append(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")