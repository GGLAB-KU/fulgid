# Initial state of boxes
boxes = {
    0: ['desert', 'octopus', 'drum', 'key', 'tie'],
    1: ['bear', 'telescope', 'flower'],
    2: [],
    3: ['pen', 'starfish', 'candle', 'battery'],
    4: [],
    5: ['scarf', 'oven', 'paint'],
    6: ['bracelet', 'flute', 'shoes', 'swimsuit'],
    7: ['usb', 'bowl', 'harmonica'],
    8: ['tape', 'hat', 'keyboard']
}

# Replace the hat with the bus in Box 8.
boxes[8].remove('hat')
boxes[8].append('bus')

# Move the bus and the keyboard from Box 8 to Box 6.
items_to_move = ['bus', 'keyboard']
for item in items_to_move:
    boxes[8].remove(item)
    boxes[6].append(item)

# Put the pillow and the shoe and the console into Box 7.
items_to_put = ['pillow', 'shoe', 'console']
for item in items_to_put:
    boxes[7].append(item)

# Swap the scarf in Box 5 with the harmonica in Box 7.
boxes[5].remove('scarf')
boxes[7].remove('harmonica')
boxes[5].append('harmonica')
boxes[7].append('scarf')

# Replace the candle and the battery with the pants and the button in Box 3.
boxes[3].remove('candle')
boxes[3].remove('battery')
boxes[3].append('pants')
boxes[3].append('button')

# Replace the drum and the tie and the octopus with the microscope and the pot and the sculpture in Box 0.
boxes[0].remove('drum')
boxes[0].remove('tie')
boxes[0].remove('octopus')
boxes[0].append('microscope')
boxes[0].append('pot')
boxes[0].append('sculpture')

# Put the bell and the shelf and the bicycle into Box 2.
items_to_put = ['bell', 'shelf', 'bicycle']
for item in items_to_put:
    boxes[2].append(item)

# Remove the tape from Box 8.
boxes[8].remove('tape')

# Put the coin and the watch and the scissors into Box 2.
items_to_put = ['coin', 'watch', 'scissors']
for item in items_to_put:
    boxes[2].append(item)

# Replace the paint with the candle in Box 5.
boxes[5].remove('paint')
boxes[5].append('candle')

# Remove the candle and the harmonica from Box 5.
boxes[5].remove('candle')
boxes[5].remove('harmonica')

# Replace the bus with the skirt in Box 6.
boxes[6].remove('bus')
boxes[6].append('skirt')

# Swap the sculpture in Box 0 with the shoe in Box 7.
boxes[0].remove('sculpture')
boxes[7].remove('shoe')
boxes[0].append('shoe')
boxes[7].append('sculpture')

# Swap the oven in Box 5 with the bracelet in Box 6.
boxes[5].remove('oven')
boxes[6].remove('bracelet')
boxes[5].append('bracelet')
boxes[6].append('oven')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")