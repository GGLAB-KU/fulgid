# Initial state of boxes
boxes = {
    0: ['thunder', 'plane', 'shark', 'flute', 'microscope'],
    1: ['grass', 'swimsuit', 'headphone', 'elephant'],
    2: ['mountain', 'pillow', 'dice'],
    3: ['flower', 'tape', 'mirror', 'pen'],
    4: [],
    5: ['planet', 'grinder', 'comet', 'submarine', 'gloves'],
    6: ['moon', 'wallet', 'oven'],
    7: [],
    8: ['cloud'],
    9: ['battery'],
    10: ['beach', 'earring', 'helmet'],
    11: ['candle', 'mask'],
    12: ['sculpture', 'bus']
}

# Remove the battery from Box 9.
boxes[9].remove('battery')

# Swap the bus in Box 12 with the mirror in Box 3.
boxes[12].remove('bus')
boxes[3].remove('mirror')
boxes[12].append('mirror')
boxes[3].append('bus')

# Swap the earring in Box 10 with the cloud in Box 8.
boxes[10].remove('earring')
boxes[8].remove('cloud')
boxes[10].append('cloud')
boxes[8].append('earring')

# Swap the mirror in Box 12 with the flute in Box 0.
boxes[12].remove('mirror')
boxes[0].remove('flute')
boxes[12].append('flute')
boxes[0].append('mirror')

# Move the sculpture from Box 12 to Box 11.
boxes[12].remove('sculpture')
boxes[11].append('sculpture')

# Put the perfume and the planet and the pants into Box 0.
items_to_put = ['perfume', 'planet', 'pants']
for item in items_to_put:
    boxes[0].append(item)

# Replace the headphone and the grass with the polish and the towel in Box 1.
boxes[1].remove('headphone')
boxes[1].remove('grass')
boxes[1].append('polish')
boxes[1].append('towel')

# Remove the flute from Box 12.
boxes[12].remove('flute')

# Move the mask and the sculpture from Box 11 to Box 7.
boxes[11].remove('mask')
boxes[11].remove('sculpture')
boxes[7].append('mask')
boxes[7].append('sculpture')

# Put the fridge and the butterfly into Box 1.
boxes[1].append('fridge')
boxes[1].append('butterfly')

# Put the chair and the basket and the snow into Box 12.
items_to_put = ['chair', 'basket', 'snow']
for item in items_to_put:
    boxes[12].append(item)

# Move the pillow from Box 2 to Box 0.
boxes[2].remove('pillow')
boxes[0].append('pillow')

# Put the swimsuit and the zipper and the wig into Box 10.
items_to_put = ['swimsuit', 'zipper', 'wig']
for item in items_to_put:
    boxes[10].append(item)

# Empty Box 6.
boxes[6] = []

# Swap the candle in Box 11 with the basket in Box 12.
boxes[11].remove('candle')
boxes[12].remove('basket')
boxes[11].append('basket')
boxes[12].append('candle')

# Put the skirt and the shoe and the bracelet into Box 0.
items_to_put = ['skirt', 'shoe', 'bracelet']
for item in items_to_put:
    boxes[0].append(item)

# Empty Box 2.
boxes[2] = []

# Replace the swimsuit and the fridge with the sun and the brush in Box 1.
boxes[1].remove('swimsuit')
boxes[1].remove('fridge')
boxes[1].append('sun')
boxes[1].append('brush')

# Swap the tape in Box 3 with the brush in Box 1.
boxes[3].remove('tape')
boxes[1].remove('brush')
boxes[3].append('brush')
boxes[1].append('tape')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")