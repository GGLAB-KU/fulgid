# Initial state of boxes
boxes = {
    0: ['microwave'],
    1: [],
    2: ['ring', 'soap', 'glove', 'piano', 'wallet'],
    3: [],
    4: [],
    5: ['cow', 'bear', 'console', 'towel'],
    6: ['rock', 'shoes', 'sun', 'makeup', 'bird']
}

# Put the freezer and the zipper and the sock into Box 3.
boxes[3].extend(['freezer', 'zipper', 'sock'])

# Remove the zipper and the freezer and the sock from Box 3.
items_to_remove = ['zipper', 'freezer', 'sock']
for item in items_to_remove:
    boxes[3].remove(item)

# Put the swimsuit into Box 0.
boxes[0].append('swimsuit')

# Put the bus into Box 1.
boxes[1].append('bus')

# Replace the bus with the planet in Box 1.
boxes[1].remove('bus')
boxes[1].append('planet')

# Swap the microwave in Box 0 with the sun in Box 6.
boxes[0].remove('microwave')
boxes[6].remove('sun')
boxes[0].append('sun')
boxes[6].append('microwave')

# Move the swimsuit from Box 0 to Box 2.
boxes[0].remove('swimsuit')
boxes[2].append('swimsuit')

# Put the boot into Box 5.
boxes[5].append('boot')

# Move the planet from Box 1 to Box 2.
boxes[1].remove('planet')
boxes[2].append('planet')

# Replace the sun with the controller in Box 0.
boxes[0].remove('sun')
boxes[0].append('controller')

# Put the cup into Box 6.
boxes[6].append('cup')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")