# Initial state of boxes
boxes = {
    0: [],
    1: ['spoon'],
    2: ['train', 'whistle', 'belt', 'button'],
    3: ['doll', 'pen'],
    4: ['jungle']
}

# Remove the train and the whistle from Box 2.
boxes[2].remove('train')
boxes[2].remove('whistle')

# Replace the doll with the camera in Box 3.
boxes[3].remove('doll')
boxes[3].append('camera')

# Remove the spoon from Box 1.
boxes[1].remove('spoon')

# Put the razor and the oven into Box 3.
boxes[3].append('razor')
boxes[3].append('oven')

# Remove the jungle from Box 4.
boxes[4].remove('jungle')

# Empty Box 3.
boxes[3] = []

# Replace the belt and the button with the dolphin and the seaweed in Box 2.
boxes[2].remove('belt')
boxes[2].remove('button')
boxes[2].append('dolphin')
boxes[2].append('seaweed')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")