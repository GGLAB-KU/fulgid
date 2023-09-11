# Initial state of boxes
boxes = {
    0: ['sun', 'moon', 'plane', 'submarine'],
    1: ['shoes', 'cloud', 'whistle', 'car', 'drum'],
    2: [],
    3: ['thunder']
}

# Put the dice and the bell into Box 1.
boxes[1].append('dice')
boxes[1].append('bell')

# Move the sun and the submarine and the plane from Box 0 to Box 1.
items_to_move = ['sun', 'submarine', 'plane']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[1].append(item)

# Replace the thunder with the blanket in Box 3.
boxes[3].remove('thunder')
boxes[3].append('blanket')

# Replace the moon with the plate in Box 0.
boxes[0].remove('moon')
boxes[0].append('plate')

# Put the flower and the sock into Box 3.
boxes[3].append('flower')
boxes[3].append('sock')

# Remove the plate from Box 0.
boxes[0].remove('plate')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")