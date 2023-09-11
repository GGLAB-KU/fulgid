# Initial state of boxes
boxes = {
    0: ['mountain', 'elephant'],
    1: ['swimsuit', 'microwave', 'lipstick', 'tree'],
    2: ['river', 'microscope'],
    3: ['dress', 'lion', 'clock'],
    4: [],
    5: ['table', 'umbrella', 'headphone', 'console'],
    6: []
}

# Remove the headphone from Box 5.
boxes[5].remove('headphone')

# Move the clock and the lion and the dress from Box 3 to Box 2.
items_to_move = ['clock', 'lion', 'dress']
for item in items_to_move:
    boxes[3].remove(item)
    boxes[2].append(item)

# Remove the mountain and the elephant from Box 0.
boxes[0].remove('mountain')
boxes[0].remove('elephant')

# Replace the tree and the swimsuit and the microwave with the shelf and the shoe and the puzzle in Box 1.
boxes[1].remove('tree')
boxes[1].remove('swimsuit')
boxes[1].remove('microwave')
boxes[1].append('shelf')
boxes[1].append('shoe')
boxes[1].append('puzzle')

# Remove the console from Box 5.
boxes[5].remove('console')

# Replace the dress and the microscope with the ocean and the desert in Box 2.
boxes[2].remove('dress')
boxes[2].remove('microscope')
boxes[2].append('ocean')
boxes[2].append('desert')

# Swap the lion in Box 2 with the shoe in Box 1.
boxes[2].remove('lion')
boxes[1].remove('shoe')
boxes[2].append('shoe')
boxes[1].append('lion')

# Put the controller and the polish and the tie into Box 4.
items_to_put = ['controller', 'polish', 'tie']
for item in items_to_put:
    boxes[4].append(item)

# Put the book and the microscope and the mask into Box 0.
items_to_put = ['book', 'microscope', 'mask']
for item in items_to_put:
    boxes[0].append(item)

# Remove the controller from Box 4.
boxes[4].remove('controller')

# Replace the book and the microscope with the river and the dog in Box 0.
boxes[0].remove('book')
boxes[0].remove('microscope')
boxes[0].append('river')
boxes[0].append('dog')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")