# Initial state of boxes
boxes = {
    0: ['bicycle'],
    1: ['skirt'],
    2: ['plane', 'boat', 'soap', 'lock'],
    3: ['freezer', 'phone', 'pan'],
    4: [],
    5: ['clock', 'pants'],
    6: ['cow', 'meteor'],
    7: ['controller'],
    8: ['dice', 'lion'],
    9: ['lightning', 'cat', 'storm', 'elephant'],
    10: ['microscope']
}

# Move the cow from Box 6 to Box 5.
boxes[6].remove('cow')
boxes[5].append('cow')

# Move the lion and the dice from Box 8 to Box 5.
boxes[8].remove('lion')
boxes[8].remove('dice')
boxes[5].append('lion')
boxes[5].append('dice')

# Put the dolphin and the comet and the seaweed into Box 8.
boxes[8].append('dolphin')
boxes[8].append('comet')
boxes[8].append('seaweed')

# Move the dolphin from Box 8 to Box 9.
boxes[8].remove('dolphin')
boxes[9].append('dolphin')

# Replace the cow and the lion with the puzzle and the bear in Box 5.
boxes[5].remove('cow')
boxes[5].remove('lion')
boxes[5].append('puzzle')
boxes[5].append('bear')

# Put the watch and the razor and the card into Box 10.
boxes[10].append('watch')
boxes[10].append('razor')
boxes[10].append('card')

# Move the comet from Box 8 to Box 4.
boxes[8].remove('comet')
boxes[4].append('comet')

# Replace the lock and the soap and the plane with the guitar and the harmonica and the scarf in Box 2.
boxes[2].remove('lock')
boxes[2].remove('soap')
boxes[2].remove('plane')
boxes[2].append('guitar')
boxes[2].append('harmonica')
boxes[2].append('scarf')

# Put the hat and the battery and the tiger into Box 10.
boxes[10].append('hat')
boxes[10].append('battery')
boxes[10].append('tiger')

# Swap the skirt in Box 1 with the dice in Box 5.
boxes[1].remove('skirt')
boxes[5].remove('dice')
boxes[1].append('dice')
boxes[5].append('skirt')

# Move the comet from Box 4 to Box 0.
boxes[4].remove('comet')
boxes[0].append('comet')

# Move the dice from Box 1 to Box 0.
boxes[1].remove('dice')
boxes[0].append('dice')

# Replace the bicycle and the dice with the seaweed and the razor in Box 0.
boxes[0].remove('bicycle')
boxes[0].remove('dice')
boxes[0].append('seaweed')
boxes[0].append('razor')

# Replace the meteor with the charger in Box 6.
boxes[6].remove('meteor')
boxes[6].append('charger')

# Remove the guitar and the scarf and the boat from Box 2.
boxes[2].remove('guitar')
boxes[2].remove('scarf')
boxes[2].remove('boat')

# Remove the harmonica from Box 2.
boxes[2].remove('harmonica')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")