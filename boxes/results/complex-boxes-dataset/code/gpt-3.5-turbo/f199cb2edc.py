# Initial state of boxes
boxes = {
    0: ['toy', 'keyboard', 'sock'],
    1: [],
    2: ['starfish', 'paint', 'pen'],
    3: ['apple', 'ship', 'submarine', 'belt'],
    4: ['oven', 'rock', 'whistle'],
    5: ['seaweed', 'shampoo', 'pillow'],
    6: ['usb', 'shoes'],
    7: ['shirt'],
    8: [],
    9: ['blanket', 'comet'],
    10: ['rain', 'soap'],
    11: ['planet', 'pants', 'grass', 'swimsuit']
}

# Move the comet and the blanket from Box 9 to Box 4.
boxes[9].remove('comet')
boxes[9].remove('blanket')
boxes[4].append('comet')
boxes[4].append('blanket')

# Remove the comet and the rock from Box 4.
boxes[4].remove('comet')
boxes[4].remove('rock')

# Move the apple and the belt from Box 3 to Box 9.
boxes[3].remove('apple')
boxes[3].remove('belt')
boxes[9].append('apple')
boxes[9].append('belt')

# Move the whistle and the oven from Box 4 to Box 5.
boxes[4].remove('whistle')
boxes[4].remove('oven')
boxes[5].append('whistle')
boxes[5].append('oven')

# Swap the shoes in Box 6 with the rain in Box 10.
boxes[6].remove('shoes')
boxes[10].remove('rain')
boxes[6].append('rain')
boxes[10].append('shoes')

# Replace the starfish and the pen with the toothbrush and the controller in Box 2.
boxes[2].remove('starfish')
boxes[2].remove('pen')
boxes[2].append('toothbrush')
boxes[2].append('controller')

# Replace the paint and the controller with the necklace and the river in Box 2.
boxes[2].remove('paint')
boxes[2].remove('controller')
boxes[2].append('necklace')
boxes[2].append('river')

# Move the submarine and the ship from Box 3 to Box 8.
boxes[3].remove('submarine')
boxes[3].remove('ship')
boxes[8].append('submarine')
boxes[8].append('ship')

# Put the shirt into Box 6.
boxes[6].append('shirt')

# Remove the shirt from Box 7.
boxes[7].remove('shirt')

# Remove the shoes and the soap from Box 10.
boxes[10].remove('shoes')
boxes[10].remove('soap')

# Move the grass from Box 11 to Box 9.
boxes[11].remove('grass')
boxes[9].append('grass')

# Put the scarf and the coat and the helmet into Box 11.
items_to_move = ['scarf', 'coat', 'helmet']
for item in items_to_move:
    boxes[11].append(item)

# Empty Box 8.
boxes[8] = []

# Move the blanket from Box 4 to Box 7.
boxes[4].remove('blanket')
boxes[7].append('blanket')

# Move the seaweed and the shampoo and the oven from Box 5 to Box 6.
items_to_move = ['seaweed', 'shampoo', 'oven']
for item in items_to_move:
    boxes[5].remove(item)
    boxes[6].append(item)

# Move the helmet from Box 11 to Box 0.
boxes[11].remove('helmet')
boxes[0].append('helmet')

# Move the swimsuit and the scarf from Box 11 to Box 1.
boxes[11].remove('swimsuit')
boxes[11].remove('scarf')
boxes[1].append('swimsuit')
boxes[1].append('scarf')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")