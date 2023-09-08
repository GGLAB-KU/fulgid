# Initial state of boxes
boxes = {
    0: ['freezer', 'zipper', 'ring'],
    1: ['tree'],
    2: [],
    3: ['scarf', 'lock'],
    4: ['wallet', 'lion', 'umbrella'],
    5: ['plate', 'sandals', 'crown', 'starfish', 'dice'],
    6: ['grinder', 'sock', 'speaker'],
    7: ['rocket', 'keyboard', 'pot'],
    8: ['ocean', 'button', 'cow'],
    9: ['chair', 'lamp', 'sun', 'bracelet'],
    10: ['glove', 'controller', 'paint', 'pillow', 'forest'],
    11: [],
    12: ['horse', 'shampoo', 'dress']
}

# Remove the grinder and the speaker and the sock from Box 6.
boxes[6].remove('grinder')
boxes[6].remove('speaker')
boxes[6].remove('sock')

# Move the tree from Box 1 to Box 3.
boxes[1].remove('tree')
boxes[3].append('tree')

# Empty Box 4.
boxes[4] = []

# Swap the controller in Box 10 with the zipper in Box 0.
boxes[10].remove('controller')
boxes[0].remove('zipper')
boxes[10].append('zipper')
boxes[0].append('controller')

# Remove the tree and the scarf and the lock from Box 3.
items_to_remove = ['tree', 'scarf', 'lock']
for item in items_to_remove:
    boxes[3].remove(item)

# Swap the shampoo in Box 12 with the ring in Box 0.
boxes[12].remove('shampoo')
boxes[0].remove('ring')
boxes[12].append('ring')
boxes[0].append('shampoo')

# Remove the chair and the lamp and the bracelet from Box 9.
items_to_remove = ['chair', 'lamp', 'bracelet']
for item in items_to_remove:
    boxes[9].remove(item)

# Put the puzzle and the dolphin and the tree into Box 2.
items_to_move = ['puzzle', 'dolphin', 'tree']
for item in items_to_move:
    boxes[2].append(item)

# Swap the paint in Box 10 with the sun in Box 9.
boxes[10].remove('paint')
boxes[9].remove('sun')
boxes[10].append('sun')
boxes[9].append('paint')

# Swap the freezer in Box 0 with the sun in Box 10.
boxes[0].remove('freezer')
boxes[10].remove('sun')
boxes[0].append('sun')
boxes[10].append('freezer')

# Swap the dice in Box 5 with the pot in Box 7.
boxes[5].remove('dice')
boxes[7].remove('pot')
boxes[5].append('pot')
boxes[7].append('dice')

# Remove the dice and the rocket from Box 7.
boxes[7].remove('dice')
boxes[7].remove('rocket')

# Replace the puzzle with the game in Box 2.
boxes[2].remove('puzzle')
boxes[2].append('game')

# Move the shampoo and the sun from Box 0 to Box 3.
boxes[0].remove('shampoo')
boxes[0].remove('sun')
boxes[3].append('shampoo')
boxes[3].append('sun')

# Put the boot and the rain and the lamp into Box 5.
items_to_move = ['boot', 'rain', 'lamp']
for item in items_to_move:
    boxes[5].append(item)

# Put the crown and the ring into Box 4.
items_to_move = ['crown', 'ring']
for item in items_to_move:
    boxes[4].append(item)

# Move the keyboard from Box 7 to Box 8.
boxes[7].remove('keyboard')
boxes[8].append('keyboard')

# Remove the paint from Box 9.
boxes[9].remove('paint')

# Replace the shampoo and the sun with the razor and the dog in Box 3.
boxes[3].remove('shampoo')
boxes[3].remove('sun')
boxes[3].append('razor')
boxes[3].append('dog')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")