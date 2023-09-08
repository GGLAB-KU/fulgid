# Initial state of boxes
boxes = {
    0: ['paint', 'guitar', 'frame'],
    1: ['polish', 'basket', 'book', 'elephant', 'snow'],
    2: [],
    3: ['apple', 'rain'],
    4: ['blanket', 'cow', 'controller', 'toaster'],
    5: ['rocket']
}

# Replace the blanket and the controller with the belt and the plate in Box 4.
boxes[4].remove('blanket')
boxes[4].remove('controller')
boxes[4].append('belt')
boxes[4].append('plate')

# Replace the guitar and the paint with the towel and the coat in Box 0.
boxes[0].remove('guitar')
boxes[0].remove('paint')
boxes[0].append('towel')
boxes[0].append('coat')

# Empty Box 3.
boxes[3] = []

# Remove the plate and the belt and the toaster from Box 4.
items_to_remove = ['plate', 'belt', 'toaster']
for item in items_to_remove:
    boxes[4].remove(item)

# Move the rocket from Box 5 to Box 1.
boxes[5].remove('rocket')
boxes[1].append('rocket')

# Move the rocket from Box 1 to Box 2.
boxes[1].remove('rocket')
boxes[2].append('rocket')

# Replace the rocket with the razor in Box 2.
boxes[2].remove('rocket')
boxes[2].append('razor')

# Swap the towel in Box 0 with the snow in Box 1.
boxes[0].remove('towel')
boxes[1].remove('snow')
boxes[0].append('snow')
boxes[1].append('towel')

# Put the leaf and the chair and the toaster into Box 2.
items_to_move = ['leaf', 'chair', 'toaster']
for item in items_to_move:
    boxes[2].append(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")