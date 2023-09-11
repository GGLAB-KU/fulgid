# Initial state of boxes
boxes = {
    0: ['branch'],
    1: ['plane', 'bus'],
    2: ['battery'],
    3: ['pen', 'toothpaste', 'toothbrush', 'beach'],
    4: ['thunder', 'controller', 'clock', 'rain']
}

# Swap the rain in Box 4 with the toothbrush in Box 3.
boxes[3].remove('toothbrush')
boxes[4].remove('rain')
boxes[3].append('rain')
boxes[4].append('toothbrush')

# Replace the battery with the ocean in Box 2.
boxes[2].remove('battery')
boxes[2].append('ocean')

# Put the mask into Box 1.
boxes[1].append('mask')

# Put the tape into Box 3.
boxes[3].append('tape')

# Replace the plane and the mask and the bus with the dolphin and the laptop and the violin in Box 1.
boxes[1].remove('plane')
boxes[1].remove('mask')
boxes[1].remove('bus')
boxes[1].append('dolphin')
boxes[1].append('laptop')
boxes[1].append('violin')

# Move the branch from Box 0 to Box 2.
boxes[0].remove('branch')
boxes[2].append('branch')

# Move the controller and the thunder and the clock from Box 4 to Box 2.
items_to_move = ['controller', 'thunder', 'clock']
for item in items_to_move:
    boxes[4].remove(item)
    boxes[2].append(item)

# Replace the dolphin and the laptop with the whistle and the candle in Box 1.
boxes[1].remove('dolphin')
boxes[1].remove('laptop')
boxes[1].append('whistle')
boxes[1].append('candle')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")