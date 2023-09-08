# Initial state of boxes
boxes = {
    0: ['shorts'],
    1: ['grass'],
    2: ['sculpture'],
    3: [],
    4: ['tie'],
    5: [],
    6: ['table', 'meteor', 'basket', 'button', 'guitar'],
    7: ['pot', 'elephant', 'lipstick', 'camera'],
    8: ['pants', 'dress', 'shelf', 'microscope'],
    9: []
}

# Swap the guitar in Box 6 with the lipstick in Box 7.
boxes[6].remove('guitar')
boxes[7].remove('lipstick')
boxes[6].append('lipstick')
boxes[7].append('guitar')

# Move the tie from Box 4 to Box 7.
boxes[4].remove('tie')
boxes[7].append('tie')

# Swap the sculpture in Box 2 with the lipstick in Box 6.
boxes[2].remove('sculpture')
boxes[6].remove('lipstick')
boxes[2].append('lipstick')
boxes[6].append('sculpture')

# Swap the meteor in Box 6 with the shorts in Box 0.
boxes[6].remove('meteor')
boxes[0].remove('shorts')
boxes[6].append('shorts')
boxes[0].append('meteor')

# Remove the guitar and the elephant from Box 7.
boxes[7].remove('guitar')
boxes[7].remove('elephant')

# Move the lipstick from Box 2 to Box 1.
boxes[2].remove('lipstick')
boxes[1].append('lipstick')

# Move the shorts and the button and the sculpture from Box 6 to Box 8.
items_to_move = ['shorts', 'button', 'sculpture']
for item in items_to_move:
    boxes[6].remove(item)
    boxes[8].append(item)

# Move the tie and the pot and the camera from Box 7 to Box 0.
items_to_move = ['tie', 'pot', 'camera']
for item in items_to_move:
    boxes[7].remove(item)
    boxes[0].append(item)

# Remove the shelf from Box 8.
boxes[8].remove('shelf')

# Move the grass from Box 1 to Box 3.
boxes[1].remove('grass')
boxes[3].append('grass')

# Move the camera from Box 0 to Box 9.
boxes[0].remove('camera')
boxes[9].append('camera')

# Remove the basket and the table from Box 6.
boxes[6].remove('basket')
boxes[6].remove('table')

# Move the grass from Box 3 to Box 9.
boxes[3].remove('grass')
boxes[9].append('grass')

# Replace the camera and the grass with the makeup and the boot in Box 9.
boxes[9].remove('camera')
boxes[9].remove('grass')
boxes[9].append('makeup')
boxes[9].append('boot')

# Remove the dress and the sculpture and the shorts from Box 8.
items_to_remove = ['dress', 'sculpture', 'shorts']
for item in items_to_remove:
    boxes[8].remove(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")