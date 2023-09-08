# Initial state of boxes
boxes = {
    0: ['razor', 'needle', 'grass'],
    1: ['pants'],
    2: [],
    3: ['rain', 'grinder'],
    4: [],
    5: ['oven'],
    6: [],
    7: ['shelf', 'puzzle'],
    8: []
}

# Replace the pants with the chair in Box 1.
boxes[1].remove('pants')
boxes[1].append('chair')

# Swap the oven in Box 5 with the shelf in Box 7.
boxes[5], boxes[7] = boxes[7], boxes[5]

# Replace the oven with the candle in Box 7.
boxes[7].remove('oven')
boxes[7].append('candle')

# Swap the rain in Box 3 with the razor in Box 0.
boxes[0], boxes[3] = boxes[3], boxes[0]

# Swap the razor in Box 3 with the chair in Box 1.
boxes[1], boxes[3] = boxes[3], boxes[1]

# Put the camera and the bear into Box 8.
boxes[8].append('camera')
boxes[8].append('bear')

# Swap the razor in Box 1 with the puzzle in Box 7.
boxes[1], boxes[7] = boxes[7], boxes[1]

# Swap the camera in Box 8 with the rain in Box 0.
boxes[0], boxes[8] = boxes[8], boxes[0]

# Replace the candle and the razor with the boat and the scissors in Box 7.
boxes[7].remove('candle')
boxes[7].remove('razor')
boxes[7].append('boat')
boxes[7].append('scissors')

# Move the puzzle from Box 1 to Box 5.
boxes[1].remove('puzzle')
boxes[5].append('puzzle')

# Move the grass and the needle and the camera from Box 0 to Box 1.
items_to_move = ['grass', 'needle', 'camera']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[1].append(item)

# Replace the shelf and the puzzle with the bird and the magnet in Box 5.
boxes[5].remove('shelf')
boxes[5].remove('puzzle')
boxes[5].append('bird')
boxes[5].append('magnet')

# Remove the magnet and the bird from Box 5.
boxes[5].remove('magnet')
boxes[5].remove('bird')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")