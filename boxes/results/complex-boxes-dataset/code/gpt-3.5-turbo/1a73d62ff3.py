# Initial state of boxes
boxes = {
    0: ['mountain'],
    1: ['belt', 'oven'],
    2: ['glasses', 'lock'],
    3: [],
    4: ['blanket', 'charger'],
    5: [],
    6: ['camera', 'scarf', 'key']
}

# Move the glasses from Box 2 to Box 5.
boxes[2].remove('glasses')
boxes[5].append('glasses')

# Put the lock into Box 0.
boxes[0].append('lock')

# Empty Box 5.
boxes[5] = []

# Put the oven and the desert into Box 1.
boxes[1].append('oven')
boxes[1].append('desert')

# Swap the desert in Box 1 with the lock in Box 2.
boxes[1].remove('desert')
boxes[2].remove('lock')
boxes[1].append('lock')
boxes[2].append('desert')

# Replace the charger and the blanket with the belt and the scissors in Box 4.
boxes[4].remove('charger')
boxes[4].remove('blanket')
boxes[4].append('belt')
boxes[4].append('scissors')

# Swap the scissors in Box 4 with the mountain in Box 0.
boxes[4].remove('scissors')
boxes[0].remove('mountain')
boxes[4].append('mountain')
boxes[0].append('scissors')

# Move the belt from Box 4 to Box 3.
boxes[4].remove('belt')
boxes[3].append('belt')

# Move the desert from Box 2 to Box 5.
boxes[2].remove('desert')
boxes[5].append('desert')

# Replace the mountain with the camera in Box 4.
boxes[4].remove('mountain')
boxes[4].append('camera')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")