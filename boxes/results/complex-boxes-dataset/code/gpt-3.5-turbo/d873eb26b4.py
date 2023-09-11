# Initial state of boxes
boxes = {
    0: ['seaweed', 'oven', 'scarf'],
    1: [],
    2: ['coin', 'tape', 'glove', 'thread', 'moon'],
    3: ['motorcycle', 'wallet', 'storm', 'rock', 'mixer']
}

# Swap the moon in Box 2 with the rock in Box 3.
boxes[2].remove('moon')
boxes[3].remove('rock')
boxes[2].append('rock')
boxes[3].append('moon')

# Put the truck and the coral and the whistle into Box 3.
items_to_add = ['truck', 'coral', 'whistle']
for item in items_to_add:
    boxes[3].append(item)

# Remove the glove from Box 2.
boxes[2].remove('glove')

# Remove the mixer from Box 3.
boxes[3].remove('mixer')

# Move the seaweed and the scarf and the oven from Box 0 to Box 1.
items_to_move = ['seaweed', 'scarf', 'oven']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[1].append(item)

# Move the oven from Box 1 to Box 0.
boxes[1].remove('oven')
boxes[0].append('oven')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")