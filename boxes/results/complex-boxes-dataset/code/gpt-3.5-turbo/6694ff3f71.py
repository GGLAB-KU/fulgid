# Initial state of boxes
boxes = {
    0: ['controller', 'flute', 'dog', 'thunder'],
    1: ['bowl', 'crown', 'ocean'],
    2: ['usb', 'oven'],
    3: [],
    4: ['storm', 'violin', 'frame', 'coin', 'toothbrush'],
    5: ['plate'],
    6: ['console', 'belt', 'lightning'],
    7: ['flower', 'rain', 'piano', 'planet'],
    8: [],
    9: ['pan', 'lock']
}

# Replace the bowl and the crown and the ocean with the plane and the shark and the needle in Box 1.
boxes[1].remove('bowl')
boxes[1].remove('crown')
boxes[1].remove('ocean')
boxes[1].append('plane')
boxes[1].append('shark')
boxes[1].append('needle')

# Remove the lock and the pan from Box 9.
boxes[9].remove('lock')
boxes[9].remove('pan')

# Replace the plate with the clock in Box 5.
boxes[5].remove('plate')
boxes[5].append('clock')

# Move the flute and the controller and the dog from Box 0 to Box 2.
items_to_move = ['flute', 'controller', 'dog']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[2].append(item)

# Replace the dog and the controller and the flute with the apple and the fork and the harmonica in Box 2.
boxes[2].remove('dog')
boxes[2].remove('controller')
boxes[2].remove('flute')
boxes[2].append('apple')
boxes[2].append('fork')
boxes[2].append('harmonica')

# Replace the thunder with the hat in Box 0.
boxes[0].remove('thunder')
boxes[0].append('hat')

# Put the makeup and the shirt and the seaweed into Box 8.
items_to_put = ['makeup', 'shirt', 'seaweed']
for item in items_to_put:
    boxes[8].append(item)

# Replace the violin and the storm and the toothbrush with the laptop and the shirt and the bus in Box 4.
boxes[4].remove('violin')
boxes[4].remove('storm')
boxes[4].remove('toothbrush')
boxes[4].append('laptop')
boxes[4].append('shirt')
boxes[4].append('bus')

# Empty Box 4.
boxes[4] = []

# Swap the hat in Box 0 with the shirt in Box 8.
boxes[0].remove('hat')
boxes[8].remove('shirt')
boxes[0].append('shirt')
boxes[8].append('hat')

# Remove the clock from Box 5.
boxes[5].remove('clock')

# Replace the usb and the oven and the harmonica with the earring and the shampoo and the lightning in Box 2.
boxes[2].remove('usb')
boxes[2].remove('oven')
boxes[2].remove('harmonica')
boxes[2].append('earring')
boxes[2].append('shampoo')
boxes[2].append('lightning')

# Remove the lightning from Box 6.
boxes[6].remove('lightning')

# Put the bicycle into Box 4.
boxes[4].append('bicycle')

# Move the bicycle from Box 4 to Box 2.
boxes[4].remove('bicycle')
boxes[2].append('bicycle')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")