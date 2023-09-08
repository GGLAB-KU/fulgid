# Initial state of boxes
boxes = {
    0: ['crown', 'cup', 'lion'],
    1: ['scissors', 'cloud', 'rocket'],
    2: ['moon', 'speaker'],
    3: ['lightning', 'planet', 'razor', 'star'],
    4: ['shorts', 'shoes'],
    5: ['dog'],
    6: ['grass', 'table'],
    7: ['violin', 'soap', 'plane'],
    8: ['pillow', 'mirror', 'meteor'],
    9: ['button'],
    10: ['lipstick'],
    11: []
}

# Empty Box 6.
boxes[6] = []

# Put the swimsuit and the toaster and the button into Box 2.
items_to_move = ['swimsuit', 'toaster', 'button']
for item in items_to_move:
    boxes[2].append(item)

# Put the spoon and the wig into Box 1.
items_to_move = ['spoon', 'wig']
for item in items_to_move:
    boxes[1].append(item)

# Empty Box 0.
boxes[0] = []

# Replace the pillow and the meteor and the mirror with the coin and the storm and the magnet in Box 8.
boxes[8].remove('pillow')
boxes[8].remove('meteor')
boxes[8].remove('mirror')
boxes[8].append('coin')
boxes[8].append('storm')
boxes[8].append('magnet')

# Replace the lipstick with the swimsuit in Box 10.
boxes[10].remove('lipstick')
boxes[10].append('swimsuit')

# Move the button from Box 2 to Box 4.
boxes[2].remove('button')
boxes[4].append('button')

# Swap the moon in Box 2 with the dog in Box 5.
boxes[2].remove('moon')
boxes[5].remove('dog')
boxes[2].append('dog')
boxes[5].append('moon')

# Move the moon from Box 5 to Box 6.
boxes[5].remove('moon')
boxes[6].append('moon')

# Swap the swimsuit in Box 10 with the button in Box 9.
boxes[10].remove('swimsuit')
boxes[9].remove('button')
boxes[10].append('button')
boxes[9].append('swimsuit')

# Replace the star and the lightning and the razor with the tape and the fridge and the apple in Box 3.
boxes[3].remove('star')
boxes[3].remove('lightning')
boxes[3].remove('razor')
boxes[3].append('tape')
boxes[3].append('fridge')
boxes[3].append('apple')

# Swap the planet in Box 3 with the button in Box 10.
boxes[3].remove('planet')
boxes[10].remove('button')
boxes[3].append('button')
boxes[10].append('planet')

# Move the plane and the soap and the violin from Box 7 to Box 11.
items_to_move = ['plane', 'soap', 'violin']
for item in items_to_move:
    boxes[7].remove(item)
    boxes[11].append(item)

# Swap the planet in Box 10 with the violin in Box 11.
boxes[10].remove('planet')
boxes[11].remove('violin')
boxes[10].append('violin')
boxes[11].append('planet')

# Replace the rocket with the earring in Box 1.
boxes[1].remove('rocket')
boxes[1].append('earring')

# Replace the violin with the rocket in Box 10.
boxes[10].remove('violin')
boxes[10].append('rocket')

# Empty Box 3.
boxes[3] = []

# Remove the magnet and the coin and the storm from Box 8.
boxes[8].remove('magnet')
boxes[8].remove('coin')
boxes[8].remove('storm')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")