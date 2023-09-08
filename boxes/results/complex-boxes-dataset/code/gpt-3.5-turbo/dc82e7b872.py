# Initial state of boxes
boxes = {
    0: ['note'],
    1: ['wig', 'planet', 'helmet'],
    2: ['crown', 'brush', 'forest', 'needle'],
    3: ['button', 'train', 'tape', 'basket'],
    4: ['coin', 'lipstick', 'wire', 'bus', 'razor'],
    5: ['toothbrush', 'plane'],
    6: ['card', 'belt'],
    7: ['motorcycle'],
    8: ['drum'],
    9: ['shoe', 'makeup', 'jungle'],
    10: ['comet', 'camera', 'fish', 'star', 'harmonica'],
    11: ['frame', 'table', 'perfume'],
    12: ['skirt', 'doll', 'speaker', 'sculpture', 'dog'],
    13: ['horse', 'microwave', 'comb'],
    14: ['mirror', 'car', 'river']
}

# Put the brush and the lock into Box 13.
boxes[13].append('brush')
boxes[13].append('lock')

# Put the pants and the watch and the pot into Box 7.
boxes[7].append('pants')
boxes[7].append('watch')
boxes[7].append('pot')

# Move the wire and the coin from Box 4 to Box 1.
boxes[4].remove('wire')
boxes[4].remove('coin')
boxes[1].append('wire')
boxes[1].append('coin')

# Move the comb from Box 13 to Box 3.
boxes[13].remove('comb')
boxes[3].append('comb')

# Replace the card and the belt with the forest and the magnet in Box 6.
boxes[6].remove('card')
boxes[6].remove('belt')
boxes[6].append('forest')
boxes[6].append('magnet')

# Put the wallet and the razor and the pan into Box 4.
boxes[4].append('wallet')
boxes[4].append('razor')
boxes[4].append('pan')

# Swap the pan in Box 4 with the plane in Box 5.
boxes[4].remove('pan')
boxes[5].remove('plane')
boxes[4].append('plane')
boxes[5].append('pan')

# Remove the car from Box 14.
boxes[14].remove('car')

# Replace the magnet and the forest with the razor and the usb in Box 6.
boxes[6].remove('magnet')
boxes[6].remove('forest')
boxes[6].append('razor')
boxes[6].append('usb')

# Remove the watch and the pants from Box 7.
boxes[7].remove('watch')
boxes[7].remove('pants')

# Remove the brush from Box 2.
boxes[2].remove('brush')

# Remove the camera and the star and the harmonica from Box 10.
boxes[10].remove('camera')
boxes[10].remove('star')
boxes[10].remove('harmonica')

# Move the table and the frame and the perfume from Box 11 to Box 6.
boxes[11].remove('table')
boxes[11].remove('frame')
boxes[11].remove('perfume')
boxes[6].append('table')
boxes[6].append('frame')
boxes[6].append('perfume')

# Put the shoes into Box 0.
boxes[0].append('shoe')

# Remove the toothbrush and the pan from Box 5.
boxes[5].remove('toothbrush')
boxes[5].remove('pan')

# Replace the perfume with the crown in Box 6.
boxes[6].remove('perfume')
boxes[6].append('crown')

# Move the river and the mirror from Box 14 to Box 7.
boxes[14].remove('river')
boxes[14].remove('mirror')
boxes[7].append('river')
boxes[7].append('mirror')

# Move the horse from Box 13 to Box 8.
boxes[13].remove('horse')
boxes[8].append('horse')

# Put the shoes and the toy into Box 5.
boxes[5].append('shoe')
boxes[5].append('toy')

# Swap the needle in Box 2 with the note in Box 0.
boxes[2].remove('needle')
boxes[0].remove('note')
boxes[2].append('note')
boxes[0].append('needle')

# Move the jungle from Box 9 to Box 7.
boxes[9].remove('jungle')
boxes[7].append('jungle')

# Move the helmet and the planet and the wire from Box 1 to Box 2.
boxes[1].remove('helmet')
boxes[1].remove('planet')
boxes[1].remove('wire')
boxes[2].append('helmet')
boxes[2].append('planet')
boxes[2].append('wire')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")