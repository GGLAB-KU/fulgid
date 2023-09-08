# Initial state of boxes
boxes = {
    0: ['fridge'],
    1: ['cow', 'card'],
    2: ['desert', 'doll', 'storm', 'scarf', 'lock'],
    3: [],
    4: ['keyboard', 'mask'],
    5: ['bus', 'clock', 'swimsuit'],
    6: [],
    7: ['sock'],
    8: ['drum', 'earring', 'game', 'bird', 'magnet'],
    9: ['oven', 'console', 'belt'],
    10: [],
    11: []
}

# Remove the clock and the swimsuit from Box 5.
boxes[5].remove('clock')
boxes[5].remove('swimsuit')

# Move the mask and the keyboard from Box 4 to Box 6.
boxes[4].remove('mask')
boxes[4].remove('keyboard')
boxes[6].append('mask')
boxes[6].append('keyboard')

# Put the horn and the perfume into Box 9.
boxes[9].append('horn')
boxes[9].append('perfume')

# Swap the keyboard in Box 6 with the card in Box 1.
boxes[6].remove('keyboard')
boxes[1].remove('card')
boxes[6].append('card')
boxes[1].append('keyboard')

# Put the bicycle and the toaster and the clock into Box 10.
boxes[10].append('bicycle')
boxes[10].append('toaster')
boxes[10].append('clock')

# Move the cow from Box 1 to Box 4.
boxes[1].remove('cow')
boxes[4].append('cow')

# Replace the sock with the mixer in Box 7.
boxes[7].remove('sock')
boxes[7].append('mixer')

# Move the cow from Box 4 to Box 10.
boxes[4].remove('cow')
boxes[10].append('cow')

# Remove the mixer from Box 7.
boxes[7].remove('mixer')

# Empty Box 2.
boxes[2] = []

# Empty Box 10.
boxes[10] = []

# Remove the perfume and the belt and the console from Box 9.
boxes[9].remove('perfume')
boxes[9].remove('belt')
boxes[9].remove('console')

# Move the fridge from Box 0 to Box 5.
boxes[0].remove('fridge')
boxes[5].append('fridge')

# Move the keyboard from Box 1 to Box 6.
boxes[1].remove('keyboard')
boxes[6].append('keyboard')

# Swap the drum in Box 8 with the horn in Box 9.
boxes[8].remove('drum')
boxes[9].remove('horn')
boxes[8].append('horn')
boxes[9].append('drum')

# Swap the mask in Box 6 with the drum in Box 9.
boxes[6].remove('mask')
boxes[9].remove('drum')
boxes[6].append('drum')
boxes[9].append('mask')

# Remove the magnet and the earring from Box 8.
boxes[8].remove('magnet')
boxes[8].remove('earring')

# Replace the bird and the game and the horn with the thunder and the freezer and the piano in Box 8.
boxes[8].remove('bird')
boxes[8].remove('game')
boxes[8].remove('horn')
boxes[8].append('thunder')
boxes[8].append('freezer')
boxes[8].append('piano')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")