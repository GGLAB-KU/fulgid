# Initial state of boxes
boxes = {
    0: ['comb', 'jungle'],
    1: ['island', 'starfish', 'camera', 'branch'],
    2: ['flower', 'boot', 'comet'],
    3: ['skirt'],
    4: ['polish', 'coat'],
    5: ['shirt', 'guitar', 'pen', 'spoon'],
    6: ['rock', 'bus', 'laptop'],
    7: ['soap', 'umbrella', 'frame', 'charger', 'shelf']
}

# Swap the bus in Box 6 with the comb in Box 0.
boxes[0].remove('comb')
boxes[6].remove('bus')
boxes[0].append('bus')
boxes[6].append('comb')

# Put the dice into Box 0.
boxes[0].append('dice')

# Put the oven into Box 5.
boxes[5].append('oven')

# Put the charger and the planet and the moon into Box 1.
boxes[1].append('charger')
boxes[1].append('planet')
boxes[1].append('moon')

# Move the coat from Box 4 to Box 7.
boxes[4].remove('coat')
boxes[7].append('coat')

# Move the jungle and the dice and the bus from Box 0 to Box 4.
items_to_move = ['jungle', 'dice', 'bus']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[4].append(item)

# Replace the skirt with the note in Box 3.
boxes[3].remove('skirt')
boxes[3].append('note')

# Put the key and the flute and the tape into Box 6.
boxes[6].append('key')
boxes[6].append('flute')
boxes[6].append('tape')

# Put the shirt and the lock into Box 4.
boxes[4].append('shirt')
boxes[4].append('lock')

# Put the wallet and the bicycle and the headphone into Box 6.
boxes[6].append('wallet')
boxes[6].append('bicycle')
boxes[6].append('headphone')

# Swap the note in Box 3 with the moon in Box 1.
boxes[3].remove('note')
boxes[1].remove('moon')
boxes[3].append('moon')
boxes[1].append('note')

# Put the harmonica into Box 7.
boxes[7].append('harmonica')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")