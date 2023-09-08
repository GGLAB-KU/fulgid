# Initial state of boxes
boxes = {
    0: ['pan', 'blender', 'candle', 'tree'],
    1: ['meteor'],
    2: ['telescope', 'comet', 'sun'],
    3: ['ship', 'soap'],
    4: ['swimsuit', 'frame', 'oven', 'shampoo'],
    5: ['boot', 'clock', 'moon'],
    6: ['plate', 'coat'],
    7: ['brush'],
    8: ['belt', 'lamp'],
    9: ['flower']
}

# Remove the sun from Box 2.
boxes[2].remove('sun')

# Swap the flower in Box 9 with the brush in Box 7.
boxes[9], boxes[7] = boxes[7], boxes[9]

# Remove the meteor from Box 1.
boxes[1].remove('meteor')

# Replace the clock with the shirt in Box 5.
boxes[5].remove('clock')
boxes[5].append('shirt')

# Remove the plate from Box 6.
boxes[6].remove('plate')

# Remove the ship from Box 3.
boxes[3].remove('ship')

# Remove the oven and the shampoo from Box 4.
boxes[4].remove('oven')
boxes[4].remove('shampoo')

# Move the brush from Box 9 to Box 1.
boxes[9].remove('brush')
boxes[1].append('brush')

# Put the shark and the flute into Box 3.
boxes[3].append('shark')
boxes[3].append('flute')

# Remove the shirt from Box 5.
boxes[5].remove('shirt')

# Swap the moon in Box 5 with the coat in Box 6.
boxes[5], boxes[6] = boxes[6], boxes[5]

# Swap the blender in Box 0 with the telescope in Box 2.
boxes[0], boxes[2] = boxes[2], boxes[0]

# Put the elephant and the bowl into Box 1.
boxes[1].append('elephant')
boxes[1].append('bowl')

# Swap the boot in Box 5 with the belt in Box 8.
boxes[5], boxes[8] = boxes[8], boxes[5]

# Move the boot and the lamp from Box 8 to Box 1.
boxes[8].remove('boot')
boxes[8].remove('lamp')
boxes[1].append('boot')
boxes[1].append('lamp')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")