# Initial state of boxes
boxes = {
    0: ['shorts'],
    1: ['toaster'],
    2: ['cup', 'basket', 'grinder', 'oven', 'bus'],
    3: ['lion', 'tape', 'brush', 'button'],
    4: ['pen'],
    5: ['candle', 'whistle'],
    6: ['submarine', 'laptop', 'headphone', 'table', 'watch'],
    7: ['sun', 'meteor', 'beach'],
    8: ['ship'],
    9: ['flute', 'wire'],
    10: ['drum', 'pants', 'shoes', 'hat', 'comb'],
    11: ['glove', 'sandals'],
    12: ['lightning', 'towel', 'necklace', 'cloud'],
    13: ['pillow'],
    14: ['rocket']
}

# Put the basket and the mixer into Box 3.
boxes[3].append('basket')
boxes[3].append('mixer')

# Put the glove and the bear into Box 0.
boxes[0].append('glove')
boxes[0].append('bear')

# Swap the pillow in Box 13 with the toaster in Box 1.
boxes[13].remove('pillow')
boxes[1].remove('toaster')
boxes[13].append('toaster')
boxes[1].append('pillow')

# Replace the shoes and the pants and the drum with the desert and the tiger and the lock in Box 10.
boxes[10].remove('shoes')
boxes[10].remove('pants')
boxes[10].remove('drum')
boxes[10].append('desert')
boxes[10].append('tiger')
boxes[10].append('lock')

# Move the whistle and the candle from Box 5 to Box 0.
boxes[5].remove('whistle')
boxes[5].remove('candle')
boxes[0].append('whistle')
boxes[0].append('candle')

# Put the sculpture into Box 0.
boxes[0].append('sculpture')

# Remove the pen from Box 4.
boxes[4].remove('pen')

# Empty Box 14.
boxes[14] = []

# Move the ship from Box 8 to Box 13.
boxes[8].remove('ship')
boxes[13].append('ship')

# Replace the mixer and the brush with the tape and the tie in Box 3.
boxes[3].remove('mixer')
boxes[3].remove('brush')
boxes[3].append('tape')
boxes[3].append('tie')

# Put the game into Box 14.
boxes[14].append('game')

# Replace the glove with the island in Box 11.
boxes[11].remove('glove')
boxes[11].append('island')

# Replace the bus and the cup and the basket with the battery and the headphone and the sock in Box 2.
boxes[2].remove('bus')
boxes[2].remove('cup')
boxes[2].remove('basket')
boxes[2].append('battery')
boxes[2].append('headphone')
boxes[2].append('sock')

# Put the truck into Box 13.
boxes[13].append('truck')

# Replace the sandals with the zipper in Box 11.
boxes[11].remove('sandals')
boxes[11].append('zipper')

# Move the game from Box 14 to Box 11.
boxes[14].remove('game')
boxes[11].append('game')

# Remove the bear and the sculpture and the shorts from Box 0.
boxes[0].remove('bear')
boxes[0].remove('sculpture')
boxes[0].remove('shorts')

# Put the charger into Box 2.
boxes[2].append('charger')

# Swap the flute in Box 9 with the beach in Box 7.
boxes[9].remove('flute')
boxes[7].remove('beach')
boxes[9].append('beach')
boxes[7].append('flute')

# Swap the toaster in Box 13 with the button in Box 3.
boxes[13].remove('toaster')
boxes[3].remove('button')
boxes[13].append('button')
boxes[3].append('toaster')

# Swap the tape in Box 3 with the candle in Box 0.
boxes[3].remove('tape')
boxes[0].remove('candle')
boxes[3].append('candle')
boxes[0].append('tape')

# Put the console and the pan into Box 8.
boxes[8].append('console')
boxes[8].append('pan')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")