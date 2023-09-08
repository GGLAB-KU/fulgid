# Initial state of boxes
boxes = {
    0: ['mask', 'crown', 'sock', 'starfish'],
    1: ['storm', 'gloves', 'mixer'],
    2: ['wig', 'cup', 'swimsuit', 'violin', 'mirror'],
    3: ['sandals', 'telescope', 'lock'],
    4: ['camera', 'truck'],
    5: ['magnet', 'jacket']
}

# Remove the sandals and the telescope and the lock from Box 3.
items_to_remove = ['sandals', 'telescope', 'lock']
for item in items_to_remove:
    boxes[3].remove(item)

# Empty Box 2.
boxes[2] = []

# Swap the camera in Box 4 with the magnet in Box 5.
boxes[4].remove('camera')
boxes[5].remove('magnet')
boxes[4].append('magnet')
boxes[5].append('camera')

# Put the elephant and the clock into Box 1.
boxes[1].append('elephant')
boxes[1].append('clock')

# Replace the truck with the fridge in Box 4.
boxes[4].remove('truck')
boxes[4].append('fridge')

# Swap the fridge in Box 4 with the camera in Box 5.
boxes[4].remove('fridge')
boxes[5].remove('camera')
boxes[4].append('camera')
boxes[5].append('fridge')

# Swap the camera in Box 4 with the jacket in Box 5.
boxes[4].remove('camera')
boxes[5].remove('jacket')
boxes[4].append('jacket')
boxes[5].append('camera')

# Replace the mask with the jacket in Box 0.
boxes[0].remove('mask')
boxes[0].append('jacket')

# Remove the jacket from Box 0.
boxes[0].remove('jacket')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")