# Initial state of boxes
boxes = {
    0: ['branch', 'chair', 'speaker'],
    1: ['wallet', 'horn', 'train', 'magnet', 'comb'],
    2: ['mixer', 'shirt', 'pen'],
    3: ['flute', 'dress', 'submarine'],
    4: ['oven', 'telescope', 'seaweed'],
    5: ['charger', 'apple', 'coat', 'star', 'spoon'],
    6: ['horse', 'lion', 'table', 'ocean'],
    7: ['thunder', 'basket', 'boot', 'gloves'],
    8: ['dog', 'rock', 'motorcycle', 'glove'],
    9: ['planet', 'coral', 'grinder'],
    10: []
}

# Move the star and the charger from Box 5 to Box 6.
boxes[5].remove('star')
boxes[5].remove('charger')
boxes[6].append('star')
boxes[6].append('charger')

# Put the mirror and the clock into Box 10.
boxes[10].append('mirror')
boxes[10].append('clock')

# Put the flower into Box 10.
boxes[10].append('flower')

# Replace the gloves and the boot with the crown and the violin in Box 7.
boxes[7].remove('gloves')
boxes[7].remove('boot')
boxes[7].append('crown')
boxes[7].append('violin')

# Remove the coral and the planet from Box 9.
boxes[9].remove('coral')
boxes[9].remove('planet')

# Remove the rock and the dog and the motorcycle from Box 8.
boxes[8].remove('rock')
boxes[8].remove('dog')
boxes[8].remove('motorcycle')

# Swap the clock in Box 10 with the grinder in Box 9.
boxes[10].remove('clock')
boxes[9].remove('grinder')
boxes[10].append('grinder')
boxes[9].append('clock')

# Replace the basket and the thunder with the necklace and the polish in Box 7.
boxes[7].remove('basket')
boxes[7].remove('thunder')
boxes[7].append('necklace')
boxes[7].append('polish')

# Replace the seaweed and the telescope with the comb and the mixer in Box 4.
boxes[4].remove('seaweed')
boxes[4].remove('telescope')
boxes[4].append('comb')
boxes[4].append('mixer')

# Put the card into Box 8.
boxes[8].append('card')

# Move the ocean from Box 6 to Box 10.
boxes[6].remove('ocean')
boxes[10].append('ocean')

# Remove the mixer from Box 2.
boxes[2].remove('mixer')

# Put the wig and the doll and the mask into Box 7.
boxes[7].append('wig')
boxes[7].append('doll')
boxes[7].append('mask')

# Replace the oven and the comb and the mixer with the horn and the controller and the coral in Box 4.
boxes[4].remove('oven')
boxes[4].remove('comb')
boxes[4].remove('mixer')
boxes[4].append('horn')
boxes[4].append('controller')
boxes[4].append('coral')

# Swap the horn in Box 4 with the submarine in Box 3.
boxes[4].remove('horn')
boxes[3].remove('submarine')
boxes[4].append('submarine')
boxes[3].append('horn')

# Swap the wallet in Box 1 with the glove in Box 8.
boxes[1].remove('wallet')
boxes[8].remove('glove')
boxes[1].append('glove')
boxes[8].append('wallet')

# Remove the branch and the speaker from Box 0.
boxes[0].remove('branch')
boxes[0].remove('speaker')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")