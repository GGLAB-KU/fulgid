# Initial state of boxes
boxes = {
    0: ['game'],
    1: ['coin', 'tree', 'cat', 'pen'],
    2: ['dolphin', 'ocean', 'whistle', 'blanket', 'coral'],
    3: ['river', 'violin', 'motorcycle', 'scarf'],
    4: ['drum', 'mountain', 'shoe', 'headphone', 'puzzle'],
    5: ['watch', 'star', 'island', 'sun'],
    6: ['boot', 'comb'],
    7: ['keyboard', 'toaster', 'charger'],
    8: ['shampoo', 'plate', 'tape', 'octopus'],
    9: ['branch', 'grass', 'book', 'battery', 'lock'],
    10: [],
    11: ['jungle', 'basket', 'soap', 'shirt', 'snow'],
    12: ['shoes', 'microscope'],
    13: ['rain', 'moon'],
    14: ['lightning', 'necklace', 'crown', 'bird']
}

# Put the rain and the rocket and the pan into Box 0.
boxes[0].extend(['rain', 'rocket', 'pan'])

# Replace the whistle and the dolphin with the storm and the bus in Box 2.
boxes[2].remove('whistle')
boxes[2].remove('dolphin')
boxes[2].append('storm')
boxes[2].append('bus')

# Remove the shirt from Box 11.
boxes[11].remove('shirt')

# Move the soap and the jungle from Box 11 to Box 13.
boxes[11].remove('soap')
boxes[11].remove('jungle')
boxes[13].extend(['soap', 'jungle'])

# Remove the bus and the coral and the blanket from Box 2.
boxes[2].remove('bus')
boxes[2].remove('coral')
boxes[2].remove('blanket')

# Empty Box 7.
boxes[7] = []

# Remove the lock and the battery from Box 9.
boxes[9].remove('lock')
boxes[9].remove('battery')

# Move the basket from Box 11 to Box 0.
boxes[11].remove('basket')
boxes[0].append('basket')

# Move the pen from Box 1 to Box 0.
boxes[1].remove('pen')
boxes[0].append('pen')

# Remove the snow from Box 11.
boxes[11].remove('snow')

# Remove the necklace and the crown from Box 14.
boxes[14].remove('necklace')
boxes[14].remove('crown')

# Put the spoon into Box 1.
boxes[1].append('spoon')

# Swap the lightning in Box 14 with the pan in Box 0.
boxes[14].remove('lightning')
boxes[0].remove('pan')
boxes[14].append('pan')
boxes[0].append('lightning')

# Remove the watch and the island and the star from Box 5.
boxes[5].remove('watch')
boxes[5].remove('island')
boxes[5].remove('star')

# Empty Box 4.
boxes[4] = []

# Swap the book in Box 9 with the shoes in Box 12.
boxes[9].remove('book')
boxes[12].remove('shoes')
boxes[9].append('shoes')
boxes[12].append('book')

# Move the moon and the soap from Box 13 to Box 6.
boxes[13].remove('moon')
boxes[13].remove('soap')
boxes[6].extend(['moon', 'soap'])

# Replace the jungle and the rain with the candle and the wire in Box 13.
boxes[13].remove('jungle')
boxes[13].remove('rain')
boxes[13].append('candle')
boxes[13].append('wire')

# Put the horn and the rock into Box 7.
boxes[7].extend(['horn', 'rock'])

# Remove the violin and the scarf and the river from Box 3.
boxes[3].remove('violin')
boxes[3].remove('scarf')
boxes[3].remove('river')

# Swap the book in Box 12 with the grass in Box 9.
boxes[12].remove('book')
boxes[9].remove('grass')
boxes[12].append('grass')
boxes[9].append('book')

# Put the helmet and the pan into Box 2.
boxes[2].extend(['helmet', 'pan'])

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")