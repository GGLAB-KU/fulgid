# Initial state of boxes
boxes = {
    0: ['shoes', 'rain', 'jungle'],
    1: ['cloud', 'leaf'],
    2: [],
    3: ['puzzle', 'crown', 'coat'],
    4: ['mirror', 'lamp', 'glove', 'cat', 'magnet'],
    5: ['mountain', 'bus', 'polish'],
    6: ['bag'],
    7: ['piano', 'toothpaste', 'train'],
    8: ['necklace', 'game', 'bicycle', 'branch', 'earring'],
    9: ['skirt', 'soap'],
    10: ['octopus', 'apple'],
    11: ['bracelet', 'frame'],
    12: ['candle']
}

# Move the crown from Box 3 to Box 9.
boxes[3].remove('crown')
boxes[9].append('crown')

# Empty Box 10.
boxes[10] = []

# Replace the leaf with the freezer in Box 1.
boxes[1].remove('leaf')
boxes[1].append('freezer')

# Replace the magnet and the mirror and the lamp with the bear and the branch and the microwave in Box 4.
boxes[4].remove('magnet')
boxes[4].remove('mirror')
boxes[4].remove('lamp')
boxes[4].append('bear')
boxes[4].append('branch')
boxes[4].append('microwave')

# Replace the branch and the necklace and the game with the harmonica and the butterfly and the lamp in Box 8.
boxes[8].remove('branch')
boxes[8].remove('necklace')
boxes[8].remove('game')
boxes[8].append('harmonica')
boxes[8].append('butterfly')
boxes[8].append('lamp')

# Put the comb into Box 3.
boxes[3].append('comb')

# Move the candle from Box 12 to Box 7.
boxes[12].remove('candle')
boxes[7].append('candle')

# Replace the bus with the tiger in Box 5.
boxes[5].remove('bus')
boxes[5].append('tiger')

# Put the mountain into Box 3.
boxes[3].append('mountain')

# Empty Box 5.
boxes[5] = []

# Remove the bracelet from Box 11.
boxes[11].remove('bracelet')

# Remove the bag from Box 6.
boxes[6].remove('bag')

# Move the crown and the skirt and the soap from Box 9 to Box 3.
boxes[9].remove('crown')
boxes[9].remove('skirt')
boxes[9].remove('soap')
boxes[3].append('crown')
boxes[3].append('skirt')
boxes[3].append('soap')

# Replace the frame with the toothpaste in Box 11.
boxes[11].remove('frame')
boxes[11].append('toothpaste')

# Move the freezer from Box 1 to Box 3.
boxes[1].remove('freezer')
boxes[3].append('freezer')

# Move the glove and the microwave from Box 4 to Box 5.
boxes[4].remove('glove')
boxes[4].remove('microwave')
boxes[5].append('glove')
boxes[5].append('microwave')

# Move the toothpaste from Box 11 to Box 5.
boxes[11].remove('toothpaste')
boxes[5].append('toothpaste')

# Put the crown and the mirror and the phone into Box 7.
boxes[3].remove('crown')
boxes[4].remove('mirror')
boxes[7].append('crown')
boxes[7].append('mirror')
boxes[7].append('phone')

# Replace the skirt and the mountain with the train and the lock in Box 3.
boxes[3].remove('skirt')
boxes[3].remove('mountain')
boxes[3].append('train')
boxes[3].append('lock')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")