# Initial state of boxes
boxes = {
    0: ['tree'],
    1: ['thunder', 'microwave', 'headphone', 'controller'],
    2: ['hat', 'spoon', 'polish', 'coin', 'harmonica'],
    3: ['brush'],
    4: ['seaweed', 'leaf', 'freezer', 'dice'],
    5: ['desert', 'planet', 'bus'],
    6: [],
    7: ['paint', 'rain'],
    8: [],
    9: ['grass'],
    10: ['comet', 'oven', 'sun', 'glove'],
    11: ['thread', 'shorts', 'gloves'],
    12: ['piano', 'laptop'],
    13: ['keyboard', 'bracelet', 'tape'],
    14: ['blender', 'magnet', 'blanket', 'soap']
}

# Swap the tree in Box 0 with the rain in Box 7.
boxes[0].remove('tree')
boxes[7].remove('rain')
boxes[0].append('rain')
boxes[7].append('tree')

# Empty Box 5.
boxes[5] = []

# Swap the brush in Box 3 with the bracelet in Box 13.
boxes[3].remove('brush')
boxes[13].remove('bracelet')
boxes[3].append('bracelet')
boxes[13].append('brush')

# Put the shampoo and the octopus and the desert into Box 14.
items_to_move = ['shampoo', 'octopus', 'desert']
for item in items_to_move:
    boxes[14].append(item)

# Move the brush and the tape and the keyboard from Box 13 to Box 2.
items_to_move = ['brush', 'tape', 'keyboard']
for item in items_to_move:
    boxes[13].remove(item)
    boxes[2].append(item)

# Remove the tape and the spoon and the keyboard from Box 2.
items_to_remove = ['tape', 'spoon', 'keyboard']
for item in items_to_remove:
    boxes[2].remove(item)

# Empty Box 2.
boxes[2] = []

# Put the mirror into Box 5.
boxes[5].append('mirror')

# Put the apple and the toaster and the game into Box 3.
items_to_move = ['apple', 'toaster', 'game']
for item in items_to_move:
    boxes[3].append(item)

# Empty Box 0.
boxes[0] = []

# Remove the thread from Box 11.
boxes[11].remove('thread')

# Swap the freezer in Box 4 with the comet in Box 10.
boxes[4].remove('freezer')
boxes[10].remove('comet')
boxes[4].append('comet')
boxes[10].append('freezer')

# Remove the desert and the magnet from Box 14.
items_to_remove = ['desert', 'magnet']
for item in items_to_remove:
    boxes[14].remove(item)

# Swap the paint in Box 7 with the oven in Box 10.
boxes[7].remove('paint')
boxes[10].remove('oven')
boxes[7].append('oven')
boxes[10].append('paint')

# Remove the bracelet and the game and the apple from Box 3.
items_to_remove = ['bracelet', 'game', 'apple']
for item in items_to_remove:
    boxes[3].remove(item)

# Move the tree and the oven from Box 7 to Box 11.
items_to_move = ['tree', 'oven']
for item in items_to_move:
    boxes[7].remove(item)
    boxes[11].append(item)

# Put the controller and the tape into Box 6.
items_to_move = ['controller', 'tape']
for item in items_to_move:
    boxes[6].append(item)

# Remove the paint and the freezer from Box 10.
items_to_remove = ['paint', 'freezer']
for item in items_to_remove:
    boxes[10].remove(item)

# Put the candle into Box 9.
boxes[9].append('candle')

# Remove the toaster from Box 3.
boxes[3].remove('toaster')

# Move the laptop from Box 12 to Box 7.
boxes[12].remove('laptop')
boxes[7].append('laptop')

# Replace the laptop with the flower in Box 7.
boxes[7].remove('laptop')
boxes[7].append('flower')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")