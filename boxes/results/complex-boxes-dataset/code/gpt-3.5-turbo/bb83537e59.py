# Initial state of boxes
boxes = {
    0: ['hat', 'pants', 'earring', 'necklace'],
    1: ['flower', 'grass', 'blanket'],
    2: [],
    3: ['vase', 'moon', 'bowl'],
    4: ['ring'],
    5: ['brush', 'tiger', 'cow'],
    6: ['desert'],
    7: ['dice', 'key', 'motorcycle', 'shampoo'],
    8: ['storm'],
    9: ['bracelet', 'train', 'lipstick', 'card'],
    10: ['glove', 'lamp', 'piano', 'star', 'shorts']
}

# Put the flower and the river and the lock into Box 10.
boxes[10].append('flower')
boxes[10].append('river')
boxes[10].append('lock')

# Replace the card and the bracelet with the cup and the makeup in Box 9.
boxes[9].remove('card')
boxes[9].remove('bracelet')
boxes[9].append('cup')
boxes[9].append('makeup')

# Remove the ring from Box 4.
boxes[4].remove('ring')

# Put the glasses into Box 5.
boxes[5].append('glasses')

# Replace the hat with the submarine in Box 0.
boxes[0].remove('hat')
boxes[0].append('submarine')

# Move the storm from Box 8 to Box 1.
boxes[8].remove('storm')
boxes[1].append('storm')

# Swap the submarine in Box 0 with the cow in Box 5.
boxes[0].remove('submarine')
boxes[5].remove('cow')
boxes[0].append('cow')
boxes[5].append('submarine')

# Remove the cow and the earring and the necklace from Box 0.
items_to_remove = ['cow', 'earring', 'necklace']
for item in items_to_remove:
    boxes[0].remove(item)

# Remove the dice and the key and the motorcycle from Box 7.
items_to_remove = ['dice', 'key', 'motorcycle']
for item in items_to_remove:
    boxes[7].remove(item)

# Put the piano into Box 3.
boxes[3].append('piano')

# Swap the bowl in Box 3 with the brush in Box 5.
boxes[3].remove('bowl')
boxes[5].remove('brush')
boxes[3].append('brush')
boxes[5].append('bowl')

# Remove the moon from Box 3.
boxes[3].remove('moon')

# Move the shampoo from Box 7 to Box 10.
boxes[7].remove('shampoo')
boxes[10].append('shampoo')

# Replace the lock and the shampoo and the flower with the tree and the frame and the book in Box 10.
boxes[10].remove('lock')
boxes[10].remove('shampoo')
boxes[10].remove('flower')
boxes[10].append('tree')
boxes[10].append('frame')
boxes[10].append('book')

# Move the bowl and the tiger and the glasses from Box 5 to Box 1.
items_to_move = ['bowl', 'tiger', 'glasses']
for item in items_to_move:
    boxes[5].remove(item)
    boxes[1].append(item)

# Put the elephant into Box 5.
boxes[5].append('elephant')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")