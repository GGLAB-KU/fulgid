# Initial state of boxes
boxes = {
    0: ['beach', 'telescope'],
    1: [],
    2: ['frame'],
    3: ['starfish', 'sun', 'fish', 'flute'],
    4: ['apple', 'mask', 'dog', 'button', 'key'],
    5: [],
    6: [],
    7: ['pan', 'train', 'fork', 'flower'],
    8: ['shampoo', 'plane', 'perfume', 'blender'],
    9: ['shoes', 'horn', 'island', 'star', 'thunder'],
    10: ['scarf', 'note']
}

# Put the laptop and the moon and the pan into Box 5.
boxes[5].extend(['laptop', 'moon', 'pan'])

# Swap the pan in Box 7 with the telescope in Box 0.
boxes[0].remove('telescope')
boxes[7].remove('pan')
boxes[0].append('pan')
boxes[7].append('telescope')

# Put the headphone into Box 4.
boxes[4].append('headphone')

# Replace the scarf with the grass in Box 10.
boxes[10].remove('scarf')
boxes[10].append('grass')

# Replace the shampoo with the makeup in Box 8.
boxes[8].remove('shampoo')
boxes[8].append('makeup')

# Put the ship and the comb and the sculpture into Box 8.
boxes[8].extend(['ship', 'comb', 'sculpture'])

# Swap the laptop in Box 5 with the comb in Box 8.
boxes[5].remove('laptop')
boxes[8].remove('comb')
boxes[5].append('comb')
boxes[8].append('laptop')

# Replace the beach with the pillow in Box 0.
boxes[0].remove('beach')
boxes[0].append('pillow')

# Put the seaweed into Box 6.
boxes[6].append('seaweed')

# Swap the ship in Box 8 with the button in Box 4.
boxes[8].remove('ship')
boxes[4].remove('button')
boxes[8].append('button')
boxes[4].append('ship')

# Move the perfume and the button from Box 8 to Box 5.
boxes[8].remove('perfume')
boxes[8].remove('button')
boxes[5].extend(['perfume', 'button'])

# Remove the comb from Box 5.
boxes[5].remove('comb')

# Put the paint and the usb into Box 1.
boxes[1].extend(['paint', 'usb'])

# Replace the pillow and the pan with the book and the rock in Box 0.
boxes[0].remove('pillow')
boxes[0].remove('pan')
boxes[0].extend(['book', 'rock'])

# Put the button and the pants into Box 4.
boxes[4].extend(['button', 'pants'])

# Swap the flute in Box 3 with the fork in Box 7.
boxes[3].remove('flute')
boxes[7].remove('fork')
boxes[3].append('fork')
boxes[7].append('flute')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")