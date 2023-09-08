# Initial state of boxes
boxes = {
    0: ['tape', 'forest'],
    1: ['jungle', 'candle', 'wig', 'battery'],
    2: [],
    3: ['lightning', 'storm', 'lamp', 'rain'],
    4: ['octopus', 'cow', 'dice', 'helmet', 'mask'],
    5: ['blender', 'telescope', 'shorts', 'frame']
}

# Swap the rain in Box 3 with the candle in Box 1.
boxes[3].remove('rain')
boxes[1].remove('candle')
boxes[3].append('candle')
boxes[1].append('rain')

# Put the jacket and the gloves and the tie into Box 5.
items_to_move = ['jacket', 'gloves', 'tie']
for item in items_to_move:
    boxes[5].append(item)

# Empty Box 4.
boxes[4] = []

# Replace the tie with the beach in Box 5.
boxes[5].remove('tie')
boxes[5].append('beach')

# Remove the rain and the jungle and the wig from Box 1.
items_to_remove = ['rain', 'jungle', 'wig']
for item in items_to_remove:
    boxes[1].remove(item)

# Replace the tape with the jungle in Box 0.
boxes[0].remove('tape')
boxes[0].append('jungle')

# Swap the storm in Box 3 with the battery in Box 1.
boxes[3].remove('storm')
boxes[1].remove('battery')
boxes[3].append('battery')
boxes[1].append('storm')

# Replace the storm with the glove in Box 1.
boxes[1].remove('storm')
boxes[1].append('glove')

# Swap the jungle in Box 0 with the gloves in Box 5.
boxes[0].remove('jungle')
boxes[5].remove('gloves')
boxes[0].append('gloves')
boxes[5].append('jungle')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")