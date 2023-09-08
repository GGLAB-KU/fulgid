# Initial state of boxes
boxes = {
    0: ['lock', 'dog'],
    1: [],
    2: ['oven', 'shoe'],
    3: ['magnet', 'frame', 'horse', 'spoon', 'jacket'],
    4: ['camera'],
    5: ['train'],
    6: []
}

# Swap the train in Box 5 with the magnet in Box 3.
boxes[5], boxes[3] = boxes[3], boxes[5]

# Swap the magnet in Box 5 with the train in Box 3.
boxes[5], boxes[3] = boxes[3], boxes[5]

# Remove the train from Box 5.
boxes[5].remove('train')

# Move the camera from Box 4 to Box 0.
boxes[4].remove('camera')
boxes[0].append('camera')

# Move the camera and the dog from Box 0 to Box 2.
boxes[0].remove('camera')
boxes[0].remove('dog')
boxes[2].extend(['camera', 'dog'])

# Remove the dog and the shoe and the oven from Box 2.
boxes[2].remove('dog')
boxes[2].remove('shoe')
boxes[2].remove('oven')

# Put the gloves into Box 5.
boxes[5].append('gloves')

# Move the frame and the jacket and the magnet from Box 3 to Box 0.
items_to_move = ['frame', 'jacket', 'magnet']
for item in items_to_move:
    boxes[3].remove(item)
    boxes[0].append(item)

# Replace the magnet and the jacket with the coin and the microwave in Box 0.
boxes[0].remove('magnet')
boxes[0].remove('jacket')
boxes[0].append('coin')
boxes[0].append('microwave')

# Swap the coin in Box 0 with the spoon in Box 3.
boxes[0], boxes[3] = boxes[3], boxes[0]

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")