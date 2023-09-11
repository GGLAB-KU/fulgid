# Initial state of boxes
boxes = {
    0: [],
    1: ['paint', 'pan', 'basket'],
    2: ['beach', 'card', 'thunder'],
    3: ['harmonica', 'dress', 'freezer', 'dice'],
    4: ['grass', 'car']
}

# Put the mixer into Box 2.
boxes[2].append('mixer')

# Remove the dice and the freezer and the harmonica from Box 3.
items_to_remove = ['dice', 'freezer', 'harmonica']
for item in items_to_remove:
    boxes[3].remove(item)

# Empty Box 2.
boxes[2] = []

# Put the moon and the cup and the star into Box 1.
items_to_add = ['moon', 'cup', 'star']
for item in items_to_add:
    boxes[1].append(item)

# Put the crown into Box 0.
boxes[0].append('crown')

# Put the bag into Box 4.
boxes[4].append('bag')

# Replace the grass and the car with the doll and the phone in Box 4.
boxes[4].remove('grass')
boxes[4].remove('car')
boxes[4].append('doll')
boxes[4].append('phone')

# Remove the doll and the bag and the phone from Box 4.
items_to_remove = ['doll', 'bag', 'phone']
for item in items_to_remove:
    boxes[4].remove(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")