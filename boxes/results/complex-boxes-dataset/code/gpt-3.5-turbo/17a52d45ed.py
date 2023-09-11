# Initial state of boxes
boxes = {
    0: ['guitar', 'rock'],
    1: ['basket', 'vase', 'speaker', 'coral'],
    2: ['branch', 'scarf', 'freezer', 'rain', 'toothpaste'],
    3: []
}

# Move the freezer from Box 2 to Box 3.
boxes[2].remove('freezer')
boxes[3].append('freezer')

# Swap the freezer in Box 3 with the guitar in Box 0.
boxes[3].remove('freezer')
boxes[0].remove('guitar')
boxes[3].append('guitar')
boxes[0].append('freezer')

# Replace the speaker and the basket and the coral with the shirt and the wire and the bracelet in Box 1.
boxes[1].remove('speaker')
boxes[1].remove('basket')
boxes[1].remove('coral')
boxes[1].append('shirt')
boxes[1].append('wire')
boxes[1].append('bracelet')

# Put the harmonica and the sandals and the pan into Box 2.
items_to_add = ['harmonica', 'sandals', 'pan']
for item in items_to_add:
    boxes[2].append(item)

# Replace the freezer and the rock with the candle and the boot in Box 0.
boxes[0].remove('freezer')
boxes[0].remove('rock')
boxes[0].append('candle')
boxes[0].append('boot')

# Move the pan and the scarf and the branch from Box 2 to Box 0.
items_to_move = ['pan', 'scarf', 'branch']
for item in items_to_move:
    boxes[2].remove(item)
    boxes[0].append(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")