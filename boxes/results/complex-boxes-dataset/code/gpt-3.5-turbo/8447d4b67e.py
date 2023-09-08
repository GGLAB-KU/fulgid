# Initial state of boxes
boxes = {
    0: ['button', 'bird', 'island', 'pillow'],
    1: ['lock', 'belt', 'usb', 'puzzle', 'microscope'],
    2: [],
    3: ['cloud', 'coin', 'ocean', 'key'],
    4: ['starfish', 'controller', 'clock'],
    5: ['bag'],
    6: ['dog', 'sock', 'fork', 'watch', 'towel'],
    7: ['submarine', 'camera', 'train', 'beach', 'car'],
    8: ['shoe', 'desert']
}

# Move the starfish and the controller and the clock from Box 4 to Box 5.
items_to_move = ['starfish', 'controller', 'clock']
for item in items_to_move:
    boxes[4].remove(item)
    boxes[5].append(item)

# Remove the shoe from Box 8.
boxes[8].remove('shoe')

# Replace the desert with the train in Box 8.
boxes[8].remove('desert')
boxes[8].append('train')

# Empty Box 6.
boxes[6] = []

# Empty Box 8.
boxes[8] = []

# Move the bag from Box 5 to Box 6.
boxes[5].remove('bag')
boxes[6].append('bag')

# Put the toothbrush and the tape and the horse into Box 8.
items_to_move = ['toothbrush', 'tape', 'horse']
for item in items_to_move:
    boxes[8].append(item)

# Remove the puzzle from Box 1.
boxes[1].remove('puzzle')

# Empty Box 5.
boxes[5] = []

# Move the belt from Box 1 to Box 3.
boxes[1].remove('belt')
boxes[3].append('belt')

# Remove the toothbrush from Box 8.
boxes[8].remove('toothbrush')

# Swap the usb in Box 1 with the car in Box 7.
boxes[1].remove('usb')
boxes[7].remove('car')
boxes[1].append('car')
boxes[7].append('usb')

# Move the camera from Box 7 to Box 6.
boxes[7].remove('camera')
boxes[6].append('camera')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")