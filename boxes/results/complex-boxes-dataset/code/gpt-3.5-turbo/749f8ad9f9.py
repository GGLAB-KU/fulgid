# Initial state of boxes
boxes = {
    0: [],
    1: ['cat', 'shorts', 'submarine', 'headphone', 'bell'],
    2: ['shampoo', 'sun', 'zipper', 'bird'],
    3: ['star', 'desert', 'blanket', 'dress', 'basket'],
    4: ['bracelet', 'spoon', 'lamp', 'charger'],
    5: ['comb', 'toothbrush'],
    6: ['fridge', 'fish', 'rocket', 'book', 'swimsuit'],
    7: ['shelf', 'shoe', 'console', 'keyboard'],
    8: ['leaf', 'pillow', 'freezer'],
    9: [],
    10: ['coin', 'paint'],
    11: ['snow', 'phone', 'helmet']
}

# Remove the lamp and the charger and the spoon from Box 4.
items_to_remove = ['lamp', 'charger', 'spoon']
for item in items_to_remove:
    boxes[4].remove(item)

# Put the controller and the paint into Box 2.
items_to_put = ['controller', 'paint']
for item in items_to_put:
    boxes[2].append(item)

# Put the forest into Box 0.
boxes[0].append('forest')

# Swap the bell in Box 1 with the bracelet in Box 4.
boxes[1].remove('bell')
boxes[4].remove('bracelet')
boxes[1].append('bracelet')
boxes[4].append('bell')

# Swap the zipper in Box 2 with the desert in Box 3.
boxes[2].remove('zipper')
boxes[3].remove('desert')
boxes[2].append('desert')
boxes[3].append('zipper')

# Remove the pillow and the leaf and the freezer from Box 8.
items_to_remove = ['pillow', 'leaf', 'freezer']
for item in items_to_remove:
    boxes[8].remove(item)

# Move the shoe and the console and the shelf from Box 7 to Box 1.
items_to_move = ['shoe', 'console', 'shelf']
for item in items_to_move:
    boxes[7].remove(item)
    boxes[1].append(item)

# Swap the bird in Box 2 with the bell in Box 4.
boxes[2].remove('bird')
boxes[4].remove('bell')
boxes[2].append('bell')
boxes[4].append('bird')

# Move the keyboard from Box 7 to Box 9.
boxes[7].remove('keyboard')
boxes[9].append('keyboard')

# Put the tiger into Box 9.
boxes[9].append('tiger')

# Move the blanket from Box 3 to Box 6.
boxes[3].remove('blanket')
boxes[6].append('blanket')

# Move the bird from Box 4 to Box 3.
boxes[4].remove('bird')
boxes[3].append('bird')

# Remove the helmet from Box 11.
boxes[11].remove('helmet')

# Replace the star with the mixer in Box 3.
boxes[3].remove('star')
boxes[3].append('mixer')

# Put the ocean and the tree into Box 4.
items_to_put = ['ocean', 'tree']
for item in items_to_put:
    boxes[4].append(item)

# Swap the forest in Box 0 with the paint in Box 2.
boxes[0].remove('forest')
boxes[2].remove('paint')
boxes[0].append('paint')
boxes[2].append('forest')

# Move the ocean and the tree from Box 4 to Box 6.
items_to_move = ['ocean', 'tree']
for item in items_to_move:
    boxes[4].remove(item)
    boxes[6].append(item)

# Remove the comb from Box 5.
boxes[5].remove('comb')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")