# Initial state of boxes
boxes = {
    0: [],
    1: ['camera', 'boat', 'jacket'],
    2: ['bowl', 'snow', 'plane', 'bag'],
    3: ['microscope']
}

# Put the rock and the tiger into Box 1.
boxes[1].append('rock')
boxes[1].append('tiger')

# Move the microscope from Box 3 to Box 1.
boxes[3].remove('microscope')
boxes[1].append('microscope')

# Put the glasses and the basket and the sock into Box 1.
items_to_put = ['glasses', 'basket', 'sock']
for item in items_to_put:
    boxes[1].append(item)

# Put the puzzle and the pan and the toy into Box 2.
items_to_put = ['puzzle', 'pan', 'toy']
for item in items_to_put:
    boxes[2].append(item)

# Swap the pan in Box 2 with the tiger in Box 1.
boxes[2].remove('pan')
boxes[1].remove('tiger')
boxes[2].append('tiger')
boxes[1].append('pan')

# Put the apple into Box 3.
boxes[3].append('apple')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")