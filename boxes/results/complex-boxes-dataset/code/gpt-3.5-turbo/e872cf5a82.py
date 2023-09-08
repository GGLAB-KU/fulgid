# Initial state of boxes
boxes = {
    0: ['helmet', 'sock', 'violin'],
    1: ['bracelet', 'coat', 'bus', 'camera'],
    2: ['bicycle', 'ship', 'spoon'],
    3: ['fridge', 'bear', 'game'],
    4: ['coin', 'grass', 'razor', 'snow'],
    5: ['chair', 'motorcycle', 'cup'],
    6: []
}

# Move the snow and the grass and the coin from Box 4 to Box 0.
items_to_move = ['snow', 'grass', 'coin']
for item in items_to_move:
    boxes[4].remove(item)
    boxes[0].append(item)

# Remove the bear from Box 3.
boxes[3].remove('bear')

# Replace the razor with the mask in Box 4.
boxes[4].remove('razor')
boxes[4].append('mask')

# Move the fridge from Box 3 to Box 6.
boxes[3].remove('fridge')
boxes[6].append('fridge')

# Remove the motorcycle and the chair from Box 5.
boxes[5].remove('motorcycle')
boxes[5].remove('chair')

# Put the dolphin and the candle and the laptop into Box 1.
items_to_move = ['dolphin', 'candle', 'laptop']
for item in items_to_move:
    boxes[1].append(item)

# Swap the bus in Box 1 with the ship in Box 2.
boxes[1].remove('bus')
boxes[2].remove('ship')
boxes[1].append('ship')
boxes[2].append('bus')

# Swap the bicycle in Box 2 with the fridge in Box 6.
boxes[2].remove('bicycle')
boxes[6].remove('fridge')
boxes[2].append('fridge')
boxes[6].append('bicycle')

# Swap the bicycle in Box 6 with the camera in Box 1.
boxes[6].remove('bicycle')
boxes[1].remove('camera')
boxes[6].append('camera')
boxes[1].append('bicycle')

# Move the fridge and the spoon from Box 2 to Box 6.
boxes[2].remove('fridge')
boxes[2].remove('spoon')
boxes[6].append('fridge')
boxes[6].append('spoon')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")