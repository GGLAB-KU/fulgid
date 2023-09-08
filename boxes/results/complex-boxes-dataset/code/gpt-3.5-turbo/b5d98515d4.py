# Initial state of boxes
boxes = {
    0: ['star'],
    1: ['glasses', 'island', 'camera', 'spoon', 'beach'],
    2: ['shirt', 'drum', 'zipper', 'candle', 'dolphin'],
    3: ['tree', 'toaster', 'shorts', 'tiger'],
    4: ['microwave', 'tape', 'mirror', 'usb'],
    5: [],
    6: ['toy', 'brush']
}

# Empty Box 4
boxes[4] = []

# Empty Box 0
boxes[0] = []

# Replace the beach with the dress in Box 1
boxes[1].remove('beach')
boxes[1].append('dress')

# Move the toaster and the tree and the tiger from Box 3 to Box 0
items_to_move = ['toaster', 'tree', 'tiger']
for item in items_to_move:
    boxes[3].remove(item)
    boxes[0].append(item)

# Replace the toy and the brush with the fork and the necklace in Box 6
boxes[6].remove('toy')
boxes[6].remove('brush')
boxes[6].append('fork')
boxes[6].append('necklace')

# Put the swimsuit and the zipper and the lipstick into Box 2
items_to_put = ['swimsuit', 'zipper', 'lipstick']
for item in items_to_put:
    boxes[2].append(item)

# Put the jungle into Box 1
boxes[1].append('jungle')

# Move the dress and the camera from Box 1 to Box 5
items_to_move = ['dress', 'camera']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[5].append(item)

# Remove the shirt and the lipstick from Box 2
boxes[2].remove('shirt')
boxes[2].remove('lipstick')

# Remove the camera and the dress from Box 5
boxes[5].remove('camera')
boxes[5].remove('dress')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")