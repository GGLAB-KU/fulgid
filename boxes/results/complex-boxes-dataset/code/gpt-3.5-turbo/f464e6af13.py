# Initial state of boxes
boxes = {
    0: ['guitar', 'dress', 'dog'],
    1: ['card', 'scarf', 'shorts', 'mountain', 'whistle'],
    2: ['desert', 'wire', 'thunder', 'seaweed', 'skirt'],
    3: ['glasses', 'rocket', 'cow', 'note'],
    4: ['magnet', 'charger', 'tiger', 'snow', 'rock'],
    5: ['necklace'],
    6: ['sculpture', 'horn', 'telescope'],
    7: ['horse', 'wig', 'microwave', 'star'],
    8: [],
    9: ['ocean'],
    10: ['shoe', 'needle'],
    11: ['sandals', 'cat', 'truck'],
    12: ['console', 'toaster', 'lion', 'drum']
}

# Put the coral into Box 11.
boxes[11].append('coral')

# Move the needle from Box 10 to Box 6.
boxes[10].remove('needle')
boxes[6].append('needle')

# Replace the dog and the dress and the guitar with the pillow and the shark and the snow in Box 0.
boxes[0].remove('dog')
boxes[0].remove('dress')
boxes[0].remove('guitar')
boxes[0].append('pillow')
boxes[0].append('shark')
boxes[0].append('snow')

# Replace the magnet with the thunder in Box 4.
boxes[4].remove('magnet')
boxes[4].append('thunder')

# Swap the shark in Box 0 with the rock in Box 4.
boxes[0].remove('shark')
boxes[4].remove('rock')
boxes[0].append('rock')
boxes[4].append('shark')

# Remove the rocket and the glasses and the note from Box 3.
boxes[3].remove('rocket')
boxes[3].remove('glasses')
boxes[3].remove('note')

# Put the meteor and the pants and the button into Box 6.
boxes[6].append('meteor')
boxes[6].append('pants')
boxes[6].append('button')

# Move the pants from Box 6 to Box 9.
boxes[6].remove('pants')
boxes[9].append('pants')

# Swap the cow in Box 3 with the mountain in Box 1.
boxes[3].remove('cow')
boxes[1].remove('mountain')
boxes[3].append('mountain')
boxes[1].append('cow')

# Put the plane and the horn into Box 0.
boxes[0].append('plane')
boxes[0].append('horn')

# Move the mountain from Box 3 to Box 7.
boxes[3].remove('mountain')
boxes[7].append('mountain')

# Swap the button in Box 6 with the coral in Box 11.
boxes[6].remove('button')
boxes[11].remove('coral')
boxes[6].append('coral')
boxes[11].append('button')

# Put the camera and the fish and the bird into Box 1.
boxes[1].append('camera')
boxes[1].append('fish')
boxes[1].append('bird')

# Replace the necklace with the boat in Box 5.
boxes[5].remove('necklace')
boxes[5].append('boat')

# Remove the tiger and the charger and the thunder from Box 4.
boxes[4].remove('tiger')
boxes[4].remove('charger')
boxes[4].remove('thunder')

# Empty Box 10.
boxes[10] = []

# Put the mixer and the whistle into Box 6.
boxes[6].append('mixer')
boxes[6].append('whistle')

# Swap the snow in Box 4 with the cow in Box 1.
boxes[4].remove('snow')
boxes[1].remove('cow')
boxes[4].append('cow')
boxes[1].append('snow')

# Put the shirt and the storm and the battery into Box 7.
boxes[7].append('shirt')
boxes[7].append('storm')
boxes[7].append('battery')

# Remove the pants and the ocean from Box 9.
boxes[9].remove('pants')
boxes[9].remove('ocean')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")