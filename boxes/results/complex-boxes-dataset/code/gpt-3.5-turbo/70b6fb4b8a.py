# Initial state of boxes
boxes = {
    0: [],
    1: ['towel', 'tape', 'doll'],
    2: ['toothbrush', 'jacket', 'glove', 'shark'],
    3: ['umbrella', 'grinder', 'perfume'],
    4: ['wallet', 'boat', 'hat'],
    5: ['bowl'],
    6: ['tie', 'snow', 'drum', 'game', 'microscope'],
    7: [],
    8: ['bag', 'button'],
    9: ['beach'],
    10: ['storm', 'octopus', 'pillow', 'piano'],
    11: [],
    12: ['bear', 'camera', 'mirror', 'dog'],
    13: ['needle', 'bracelet', 'freezer', 'basket']
}

# Replace the glove and the shark with the shoes and the motorcycle in Box 2.
boxes[2].remove('glove')
boxes[2].remove('shark')
boxes[2].append('shoes')
boxes[2].append('motorcycle')

# Replace the motorcycle and the jacket with the bus and the guitar in Box 2.
boxes[2].remove('motorcycle')
boxes[2].remove('jacket')
boxes[2].append('bus')
boxes[2].append('guitar')

# Replace the tie and the game and the drum with the apple and the coat and the rain in Box 6.
boxes[6].remove('tie')
boxes[6].remove('game')
boxes[6].remove('drum')
boxes[6].append('apple')
boxes[6].append('coat')
boxes[6].append('rain')

# Move the storm from Box 10 to Box 7.
boxes[10].remove('storm')
boxes[7].append('storm')

# Remove the beach from Box 9.
boxes[9].remove('beach')

# Put the scissors and the pot and the comb into Box 1.
boxes[1].append('scissors')
boxes[1].append('pot')
boxes[1].append('comb')

# Put the toaster and the river and the pan into Box 8.
boxes[8].append('toaster')
boxes[8].append('river')
boxes[8].append('pan')

# Move the needle and the basket and the bracelet from Box 13 to Box 1.
boxes[13].remove('needle')
boxes[13].remove('basket')
boxes[13].remove('bracelet')
boxes[1].append('needle')
boxes[1].append('basket')
boxes[1].append('bracelet')

# Put the horn and the phone into Box 11.
boxes[11].append('horn')
boxes[11].append('phone')

# Swap the mirror in Box 12 with the horn in Box 11.
boxes[12].remove('mirror')
boxes[11].remove('horn')
boxes[12].append('horn')
boxes[11].append('mirror')

# Put the dice into Box 2.
boxes[2].append('dice')

# Remove the perfume and the umbrella from Box 3.
boxes[3].remove('perfume')
boxes[3].remove('umbrella')

# Remove the horn and the camera from Box 12.
boxes[12].remove('horn')
boxes[12].remove('camera')

# Remove the grinder from Box 3.
boxes[3].remove('grinder')

# Remove the pillow and the octopus and the piano from Box 10.
boxes[10].remove('pillow')
boxes[10].remove('octopus')
boxes[10].remove('piano')

# Remove the freezer from Box 13.
boxes[13].remove('freezer')

# Move the scissors and the bracelet and the tape from Box 1 to Box 12.
boxes[1].remove('scissors')
boxes[1].remove('bracelet')
boxes[1].remove('tape')
boxes[12].append('scissors')
boxes[12].append('bracelet')
boxes[12].append('tape')

# Replace the tape and the scissors with the wallet and the forest in Box 12.
boxes[12].remove('tape')
boxes[12].remove('scissors')
boxes[12].append('wallet')
boxes[12].append('forest')

# Replace the bowl with the razor in Box 5.
boxes[5].remove('bowl')
boxes[5].append('razor')

# Put the coat and the bird into Box 8.
boxes[8].append('coat')
boxes[8].append('bird')

# Swap the storm in Box 7 with the wallet in Box 12.
boxes[7].remove('storm')
boxes[12].remove('wallet')
boxes[7].append('wallet')
boxes[12].append('storm')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")