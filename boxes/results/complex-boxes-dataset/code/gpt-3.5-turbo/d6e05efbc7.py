# Initial state of boxes
boxes = {
    0: ['keyboard', 'mountain', 'hat'],
    1: ['beach', 'oven', 'makeup'],
    2: ['shoes', 'river', 'lion', 'whistle'],
    3: ['harmonica', 'boot'],
    4: ['glasses', 'sun', 'sculpture']
}

# Replace the keyboard with the helmet in Box 0.
boxes[0].remove('keyboard')
boxes[0].append('helmet')

# Move the glasses from Box 4 to Box 2.
boxes[4].remove('glasses')
boxes[2].append('glasses')

# Put the harmonica and the drum and the microwave into Box 1.
items_to_move = ['harmonica', 'drum', 'microwave']
for item in items_to_move:
    boxes[1].append(item)

# Remove the mountain and the helmet from Box 0.
boxes[0].remove('mountain')
boxes[0].remove('helmet')

# Put the needle into Box 1.
boxes[1].append('needle')

# Empty Box 0.
boxes[0] = []

# Put the skirt and the soap and the pants into Box 0.
items_to_move = ['skirt', 'soap', 'pants']
for item in items_to_move:
    boxes[0].append(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")