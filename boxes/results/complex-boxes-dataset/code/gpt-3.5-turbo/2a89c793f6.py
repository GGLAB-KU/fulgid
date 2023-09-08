# Initial state of boxes
boxes = {
    0: [],
    1: [],
    2: ['fish'],
    3: [],
    4: [],
    5: ['horn', 'cup'],
    6: ['shampoo', 'usb'],
    7: ['ship', 'train', 'chair', 'skirt', 'speaker'],
    8: ['motorcycle', 'crown', 'glove', 'tape', 'snow'],
    9: ['tree', 'helmet', 'bear'],
    10: ['scarf', 'needle', 'wig'],
    11: ['card', 'candle'],
    12: ['swimsuit', 'planet', 'shorts', 'microwave'],
    13: ['tiger'],
    14: ['toothbrush', 'spoon', 'lightning']
}

# Put the apple into Box 1.
boxes[1].append('apple')

# Swap the tiger in Box 13 with the candle in Box 11.
boxes[13].remove('tiger')
boxes[11].remove('candle')
boxes[13].append('candle')
boxes[11].append('tiger')

# Put the forest and the lamp and the pan into Box 8.
items_to_put = ['forest', 'lamp', 'pan']
for item in items_to_put:
    boxes[8].append(item)

# Move the glove from Box 8 to Box 11.
boxes[8].remove('glove')
boxes[11].append('glove')

# Move the candle from Box 13 to Box 6.
boxes[13].remove('candle')
boxes[6].append('candle')

# Remove the lightning and the toothbrush and the spoon from Box 14.
items_to_remove = ['lightning', 'toothbrush', 'spoon']
for item in items_to_remove:
    boxes[14].remove(item)

# Move the tiger and the card from Box 11 to Box 2.
boxes[11].remove('tiger')
boxes[11].remove('card')
boxes[2].append('tiger')
boxes[2].append('card')

# Put the cloud and the shark into Box 3.
boxes[3].append('cloud')
boxes[3].append('shark')

# Put the razor into Box 7.
boxes[7].append('razor')

# Put the microscope and the freezer into Box 1.
boxes[1].append('microscope')
boxes[1].append('freezer')

# Replace the crown and the snow and the motorcycle with the bus and the hat and the chair in Box 8.
boxes[8].remove('crown')
boxes[8].remove('snow')
boxes[8].remove('motorcycle')
boxes[8].append('bus')
boxes[8].append('hat')
boxes[8].append('chair')

# Swap the swimsuit in Box 12 with the cup in Box 5.
boxes[12].remove('swimsuit')
boxes[5].remove('cup')
boxes[12].append('cup')
boxes[5].append('swimsuit')

# Move the tiger from Box 2 to Box 5.
boxes[2].remove('tiger')
boxes[5].append('tiger')

# Remove the shampoo from Box 6.
boxes[6].remove('shampoo')

# Move the bear from Box 9 to Box 0.
boxes[9].remove('bear')
boxes[0].append('bear')

# Remove the fish from Box 2.
boxes[2].remove('fish')

# Swap the tree in Box 9 with the card in Box 2.
boxes[9].remove('tree')
boxes[2].remove('card')
boxes[9].append('card')
boxes[2].append('tree')

# Put the puzzle and the bicycle into Box 11.
boxes[11].append('puzzle')
boxes[11].append('bicycle')

# Replace the skirt with the bus in Box 7.
boxes[7].remove('skirt')
boxes[7].append('bus')

# Replace the bear with the card in Box 0.
boxes[0].remove('bear')
boxes[0].append('card')

# Swap the puzzle in Box 11 with the shorts in Box 12.
boxes[11].remove('puzzle')
boxes[12].remove('shorts')
boxes[11].append('shorts')
boxes[12].append('puzzle')

# Remove the candle and the usb from Box 6.
boxes[6].remove('candle')
boxes[6].remove('usb')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")