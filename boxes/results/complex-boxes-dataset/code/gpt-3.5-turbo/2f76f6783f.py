# Initial state of boxes
boxes = {
    0: ['cat', 'rock', 'submarine', 'scissors', 'hat'],
    1: [],
    2: ['coin', 'shark', 'star', 'elephant', 'charger'],
    3: ['clock', 'button', 'table']
}

# Swap the coin in Box 2 with the submarine in Box 0.
boxes[0].remove('submarine')
boxes[2].remove('coin')
boxes[0].append('coin')
boxes[2].append('submarine')

# Put the helmet and the sock and the fork into Box 1.
items_to_put = ['helmet', 'sock', 'fork']
for item in items_to_put:
    boxes[1].append(item)

# Put the truck and the thunder into Box 2.
items_to_put = ['truck', 'thunder']
for item in items_to_put:
    boxes[2].append(item)

# Put the sun into Box 1.
boxes[1].append('sun')

# Swap the hat in Box 0 with the sock in Box 1.
boxes[0].remove('hat')
boxes[1].remove('sock')
boxes[0].append('sock')
boxes[1].append('hat')

# Remove the coin from Box 0.
boxes[0].remove('coin')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")