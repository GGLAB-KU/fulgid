# Initial state of boxes
boxes = {
    0: ['basket', 'bear'],
    1: ['whistle', 'rocket'],
    2: ['candle', 'planet', 'branch', 'chair', 'sun'],
    3: ['butterfly', 'pan', 'blender', 'button'],
    4: ['wallet', 'piano'],
    5: ['plate', 'shark', 'grass'],
    6: ['glove', 'gloves', 'belt', 'dolphin'],
    7: ['makeup', 'mountain', 'microscope', 'rain', 'seaweed'],
    8: [],
    9: ['cow', 'starfish', 'perfume', 'flute', 'elephant'],
    10: ['wig', 'shelf', 'headphone']
}

# Replace the whistle and the rocket with the vase and the beach in Box 1.
boxes[1].remove('whistle')
boxes[1].remove('rocket')
boxes[1].append('vase')
boxes[1].append('beach')

# Move the chair and the planet and the sun from Box 2 to Box 0.
items_to_move = ['chair', 'planet', 'sun']
for item in items_to_move:
    boxes[2].remove(item)
    boxes[0].append(item)

# Put the truck and the usb into Box 3.
boxes[3].append('truck')
boxes[3].append('usb')

# Swap the glove in Box 6 with the grass in Box 5.
boxes[6].remove('glove')
boxes[5].remove('grass')
boxes[6].append('grass')
boxes[5].append('glove')

# Move the beach from Box 1 to Box 9.
boxes[1].remove('beach')
boxes[9].append('beach')

# Swap the vase in Box 1 with the button in Box 3.
boxes[1].remove('vase')
boxes[3].remove('button')
boxes[1].append('button')
boxes[3].append('vase')

# Replace the shark with the button in Box 5.
boxes[5].remove('shark')
boxes[5].append('button')

# Replace the mountain and the rain and the makeup with the sock and the snow and the cat in Box 7.
boxes[7].remove('mountain')
boxes[7].remove('rain')
boxes[7].remove('makeup')
boxes[7].append('sock')
boxes[7].append('snow')
boxes[7].append('cat')

# Move the wallet from Box 4 to Box 3.
boxes[4].remove('wallet')
boxes[3].append('wallet')

# Replace the vase and the usb with the pillow and the cup in Box 3.
boxes[3].remove('vase')
boxes[3].remove('usb')
boxes[3].append('pillow')
boxes[3].append('cup')

# Remove the headphone from Box 10.
boxes[10].remove('headphone')

# Replace the shelf and the wig with the snow and the rock in Box 10.
boxes[10].remove('shelf')
boxes[10].remove('wig')
boxes[10].append('snow')
boxes[10].append('rock')

# Move the button from Box 1 to Box 2.
boxes[1].remove('button')
boxes[2].append('button')

# Remove the planet and the basket from Box 0.
boxes[0].remove('planet')
boxes[0].remove('basket')

# Move the sock and the cat from Box 7 to Box 2.
boxes[7].remove('sock')
boxes[7].remove('cat')
boxes[2].append('sock')
boxes[2].append('cat')

# Empty Box 5.
boxes[5] = []

# Move the candle from Box 2 to Box 5.
boxes[2].remove('candle')
boxes[5].append('candle')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")