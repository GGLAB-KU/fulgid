# Initial state of boxes
boxes = {
    0: [],
    1: ['cat', 'plane', 'grinder', 'game', 'scarf'],
    2: ['doll', 'moon'],
    3: ['perfume', 'camera', 'controller', 'button', 'tie'],
    4: [],
    5: ['lamp', 'motorcycle', 'drum', 'gloves'],
    6: ['glove', 'basket', 'sculpture', 'forest'],
    7: [],
    8: ['coral', 'telescope', 'toothpaste', 'tape'],
    9: ['whistle'],
    10: [],
    11: ['cup', 'lightning', 'bowl']
}

# Move the basket and the forest from Box 6 to Box 4.
boxes[6].remove('basket')
boxes[6].remove('forest')
boxes[4].append('basket')
boxes[4].append('forest')

# Put the card and the cup and the glasses into Box 9.
boxes[9].append('card')
boxes[9].append('cup')
boxes[9].append('glasses')

# Move the forest from Box 4 to Box 0.
boxes[4].remove('forest')
boxes[0].append('forest')

# Swap the doll in Box 2 with the plane in Box 1.
boxes[2].remove('doll')
boxes[1].remove('plane')
boxes[2].append('plane')
boxes[1].append('doll')

# Put the shark into Box 0.
boxes[0].append('shark')

# Swap the shark in Box 0 with the motorcycle in Box 5.
boxes[0].remove('shark')
boxes[5].remove('motorcycle')
boxes[0].append('motorcycle')
boxes[5].append('shark')

# Put the octopus and the skirt into Box 2.
boxes[2].append('octopus')
boxes[2].append('skirt')

# Replace the glove and the sculpture with the lipstick and the car in Box 6.
boxes[6].remove('glove')
boxes[6].remove('sculpture')
boxes[6].append('lipstick')
boxes[6].append('car')

# Move the scarf from Box 1 to Box 0.
boxes[1].remove('scarf')
boxes[0].append('scarf')

# Remove the basket from Box 4.
boxes[4].remove('basket')

# Put the harmonica into Box 10.
boxes[10].append('harmonica')

# Swap the game in Box 1 with the whistle in Box 9.
boxes[1].remove('game')
boxes[9].remove('whistle')
boxes[1].append('whistle')
boxes[9].append('game')

# Remove the car from Box 6.
boxes[6].remove('car')

# Replace the button and the tie and the camera with the starfish and the speaker and the pot in Box 3.
boxes[3].remove('button')
boxes[3].remove('tie')
boxes[3].remove('camera')
boxes[3].append('starfish')
boxes[3].append('speaker')
boxes[3].append('pot')

# Put the lion into Box 10.
boxes[10].append('lion')

# Remove the lion and the harmonica from Box 10.
boxes[10].remove('lion')
boxes[10].remove('harmonica')

# Replace the game and the cup and the card with the lamp and the beach and the sun in Box 9.
boxes[9].remove('game')
boxes[9].remove('cup')
boxes[9].remove('card')
boxes[9].append('lamp')
boxes[9].append('beach')
boxes[9].append('sun')

# Replace the moon with the cow in Box 2.
boxes[2].remove('moon')
boxes[2].append('cow')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")