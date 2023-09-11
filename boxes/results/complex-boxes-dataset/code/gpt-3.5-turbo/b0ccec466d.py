# Initial state of boxes
boxes = {
    0: ['telescope', 'candle'],
    1: ['lamp', 'glasses', 'zipper'],
    2: ['dice', 'tie', 'scissors', 'magnet'],
    3: [],
    4: [],
    5: ['vase', 'mountain', 'key'],
    6: ['drum', 'skirt'],
    7: ['usb', 'dolphin', 'pillow'],
    8: ['tape', 'shorts'],
    9: ['headphone'],
    10: [],
    11: ['octopus', 'branch'],
    12: ['pants', 'shoe', 'bear']
}

# Empty Box 9.
boxes[9] = []

# Replace the shoe with the glove in Box 12.
boxes[12].remove('shoe')
boxes[12].append('glove')

# Put the planet into Box 6.
boxes[6].append('planet')

# Replace the tape with the shoe in Box 8.
boxes[8].remove('tape')
boxes[8].append('shoe')

# Put the lamp into Box 2.
boxes[2].append('lamp')

# Remove the branch and the octopus from Box 11.
boxes[11].remove('branch')
boxes[11].remove('octopus')

# Put the drum into Box 12.
boxes[12].append('drum')

# Remove the shorts from Box 8.
boxes[8].remove('shorts')

# Put the lock into Box 9.
boxes[9].append('lock')

# Move the lamp from Box 2 to Box 8.
boxes[2].remove('lamp')
boxes[8].append('lamp')

# Remove the vase and the key and the mountain from Box 5.
boxes[5].remove('vase')
boxes[5].remove('key')
boxes[5].remove('mountain')

# Swap the lamp in Box 1 with the drum in Box 12.
boxes[1].remove('lamp')
boxes[12].remove('drum')
boxes[1].append('drum')
boxes[12].append('lamp')

# Move the glasses and the drum from Box 1 to Box 2.
boxes[1].remove('glasses')
boxes[1].remove('drum')
boxes[2].append('glasses')
boxes[2].append('drum')

# Swap the zipper in Box 1 with the lock in Box 9.
boxes[1].remove('zipper')
boxes[9].remove('lock')
boxes[1].append('lock')
boxes[9].append('zipper')

# Move the dice and the tie from Box 2 to Box 1.
boxes[2].remove('dice')
boxes[2].remove('tie')
boxes[1].append('dice')
boxes[1].append('tie')

# Swap the zipper in Box 9 with the shoe in Box 8.
boxes[9].remove('zipper')
boxes[8].remove('shoe')
boxes[9].append('shoe')
boxes[8].append('zipper')

# Put the dress and the tiger and the snow into Box 8.
boxes[8].append('dress')
boxes[8].append('tiger')
boxes[8].append('snow')

# Put the belt and the dog and the console into Box 6.
boxes[6].append('belt')
boxes[6].append('dog')
boxes[6].append('console')

# Swap the zipper in Box 8 with the candle in Box 0.
boxes[8].remove('zipper')
boxes[0].remove('candle')
boxes[8].append('candle')
boxes[0].append('zipper')

# Swap the tie in Box 1 with the candle in Box 8.
boxes[1].remove('tie')
boxes[8].remove('candle')
boxes[1].append('candle')
boxes[8].append('tie')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")