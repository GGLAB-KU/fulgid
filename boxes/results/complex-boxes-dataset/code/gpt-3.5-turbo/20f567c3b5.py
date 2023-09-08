# Initial state of boxes
boxes = {
    0: ['train', 'bus', 'pan', 'bell'],
    1: ['doll', 'umbrella', 'meteor'],
    2: [],
    3: ['island'],
    4: [],
    5: ['basket', 'harmonica', 'pot', 'glove']
}

# Put the bear into Box 2.
boxes[2].append('bear')

# Move the harmonica and the basket and the glove from Box 5 to Box 0.
items_to_move = ['harmonica', 'basket', 'glove']
for item in items_to_move:
    boxes[5].remove(item)
    boxes[0].append(item)

# Put the coin and the controller and the sock into Box 1.
items_to_put = ['coin', 'controller', 'sock']
for item in items_to_put:
    boxes[1].append(item)

# Move the bus and the pan and the train from Box 0 to Box 2.
items_to_move = ['bus', 'pan', 'train']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[2].append(item)

# Put the moon into Box 5.
boxes[5].append('moon')

# Empty Box 2.
boxes[2] = []

# Swap the pot in Box 5 with the bell in Box 0.
boxes[5].remove('pot')
boxes[0].remove('bell')
boxes[5].append('bell')
boxes[0].append('pot')

# Swap the bell in Box 5 with the meteor in Box 1.
boxes[5].remove('bell')
boxes[1].remove('meteor')
boxes[5].append('meteor')
boxes[1].append('bell')

# Swap the moon in Box 5 with the island in Box 3.
boxes[5].remove('moon')
boxes[3].remove('island')
boxes[5].append('island')
boxes[3].append('moon')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")